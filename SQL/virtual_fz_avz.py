import pandas as pd
import general_sql
from dicts_n_lists import sql_import_map


def tree_plot_purchased(root_level: int, root_id: str, df_x: pd.DataFrame, purchased_list: list) -> pd.DataFrame():
    '''
    function to drill down the tree, collecting list of purchased 'points'
    :param root_level: starting tree level
    :param root_id: starting tree point id
    :param df_x: tree dataframe
    :param purchased_list: list of tree points that are qualified as purchased
    :return: list of purchased tree points
    '''
    df_x = df_x[df_x['breadcrumb'].str.contains(str(root_id))]
    df_x2 = df_x[df_x['level'] == root_level]
    level_lower = df_x2['artikel_nummer'].drop_duplicates().tolist()
    root_level2 = root_level + 1

    for lvl_l in level_lower:
        purchased_list.append(df_x['breadcrumb'][df_x['artikel_nummer'] == lvl_l].values[0])
        purchased_list = tree_plot_purchased(root_level2, lvl_l, df_x, purchased_list)

    return purchased_list


def tree_plot(root_level: int, root_id: str, df_x: pd.DataFrame, purchase_level_list: list, purchased_list: list) -> pd.DataFrame():
    '''
    function to drill down tree, collecting points by which material was purchased and lower purchased points in this position
    :param root_level: starting tree level
    :param root_id: starting tree point id
    :param df_x: tree dataframe
    :param purchase_level_list: list of tree points that are qualified as level by which position was purchased (price contained)
    :param purchased_list: list of tree points that are qualified as purchased
    :return:
    '''
    df_x = df_x[df_x['breadcrumb'].str.contains(str(root_id))]
    df_x2 = df_x[df_x['level'] == root_level]
    level_lower = df_x2['artikel_nummer'].drop_duplicates().tolist()
    parts_count = len(level_lower)
    purchase_count = 0
    root_level2 = root_level + 1

    for lvl_l in level_lower:
        #print(root_level, lvl_l)
        if df_x['mnr'][df_x['artikel_nummer'] == lvl_l].any():
            purchase_count += 1
            purchase_level_list.append(df_x['breadcrumb'][df_x['artikel_nummer'] == lvl_l].values[0])
            purchased_list.append(df_x['breadcrumb'][df_x['artikel_nummer'] == lvl_l].values[0])
            #print('m/a') #if found higher lvl; do not search lower
            #do lower only for purchased list
            purchased_list = tree_plot_purchased(root_level2, lvl_l, df_x, purchased_list)
        else:
            purchase_level_list, purchased_list = tree_plot(root_level2, lvl_l, df_x, purchase_level_list, purchased_list)

    #risk with doubles
    if purchase_count == parts_count and parts_count > 0:
        prev_breadcrumb = df_x['breadcrumb'][df_x['artikel_nummer'] == level_lower[0]].values[0]
        prev_breadcrumb = prev_breadcrumb[:str(prev_breadcrumb).rfind("/")]
        #purchase_level_list.append(prev_breadcrumb)
        purchased_list.append(prev_breadcrumb)

    return purchase_level_list, purchased_list


def create_fz_avz(project: str, fz: str):
    avz_table_name = 'avz'
    matlist_table_name = 'materialliste'
    path_save = r'C:\Users\rytpio\Desktop\Projekty bieżące\AVZ'

    df_avz = general_sql.get_table_condition(avz_table_name, ['id'] + list(sql_import_map.avz_sql_col_dict.keys()), "projekt_nr", project)
    df_matlist = general_sql.get_table_multi_condition(matlist_table_name, ['id'] + list(
        sql_import_map.materialliste_sql_col_dict.keys()),
                                                       ['komm', 'fz'], [project, str(fz)])
    df_matlist_short = df_matlist[['mnr']].drop_duplicates()
    df = pd.merge(left=df_avz, right=df_matlist_short, how='left',
                  left_on=['artikel_nummer'], right_on=['mnr'],
                  suffixes=['_avz', '_materialliste'])

    df.to_excel(f'{path_save}\\test_merge.xlsx', index=False, sheet_name='avz')

    #TODO: separate function
    base_level = 0
    root_level = base_level+1
    level0 = df['artikel_nummer'][(df['level'] == base_level)].drop_duplicates().tolist()
    purchase_level_list = list()
    purchased_list = list()
    for lvl0 in level0:
        # if root level(0) prc is not empty then call 'mat/acc' and next
        if df['mnr'][df['artikel_nummer'] == lvl0].any():# or df['category'][df['artikel_nummer'] == lvl0].any():
            purchase_level_list.append(df['breadcrumb'][df['artikel_nummer'] == lvl0].values[0])
            purchased_list.append(df['breadcrumb'][df['artikel_nummer'] == lvl0].values[0])
            #print('level 0 bought: ' + lvl0)
            #search lower to mark purchased list
            purchased_list = tree_plot_purchased(root_level, lvl0, df, purchased_list)
        else:
            purchase_level_list, purchased_list = tree_plot(root_level, lvl0, df, purchase_level_list, purchased_list)

    # print(purchased_list == purchase_level_list)
    # print(purchase_level_list)
    # print(purchased_list)

    df_purchase_level = pd.DataFrame(data=purchase_level_list, columns=['breadcrumb']).drop_duplicates()
    df_purchase_level['purchase_level'] = 'x'
    df = df.merge(df_purchase_level, how='left', left_on='breadcrumb', right_on='breadcrumb')

    df_purchased = pd.DataFrame(data=purchased_list, columns=['breadcrumb']).drop_duplicates()
    df_purchased['purchased_status'] = 'ok'
    df = df.merge(df_purchased, how='left', left_on='breadcrumb', right_on='breadcrumb')
    cat_ok_list = ['bolts_misc', 'chemicals', 'diverse', 'hoses_pneumatic', 'nuts', 'screws',
                   'specification', 'washers', 'unassigned', 'struct_mechanic', 'struct_electric', 'struct_pneumatic']
    df['purchased_status_'] = df.apply(lambda row: 'ok' if row.pos_nr_category_bu_1951939 in cat_ok_list else row.purchased_status, axis=1)

    df.to_excel(f'{path_save}\\test_avz_mat.xlsx', index=False, sheet_name='avz')


#create_fz_avz('4473', '12')

def substract_mat(quantity: float, prices: pd.DataFrame, df_matlist: pd.DataFrame, df_we: pd.DataFrame) -> [list, list, float, str, pd.DataFrame]:
    #prices can be different; take price 1 if is enough; if completed from more than 1 then flag and take average
    #one order can be insufficient for avz completion
    #two orders can be done in different currencies; default is EUR if more than 1
    supplier_list = []
    order_list = []
    price_list = []
    we_list = []
    count = len(prices)
    i = 0
    for tpl in prices.itertuples():
        #print(tpl)
        index = df_matlist[(df_matlist['mnr'] == tpl.mnr) & (df_matlist['beleg_nr_best'] == tpl.beleg_nr_best)].index
        #print(df_matlist['quantity_per_order'][index], 1)
        if float(tpl.quantity_per_order_without_avz) >= quantity: #order is enough or more
            price_list.append(float(tpl.acppart_preis) / float(tpl.f_preisbasis))
            we_list.append(str(tpl.we).upper()) #currency
            order_list.append(tpl.beleg_nr_best)  #order
            supplier_list.append(tpl.ext_ktxt) #supplier
            #substract and end function
            df_matlist['quantity_per_order'][index] = float(tpl.quantity_per_order_without_avz) - quantity
            #print(df_matlist['quantity_per_order'][index], 2)
            return order_list, supplier_list, price_list[0], we_list[0], df_matlist
        elif float(tpl.quantity_per_order_without_avz) > 0: #order is not enough but not 0
            if int(tpl.quantity_per_order) == 0:
                we_qt = 1
            else:
                we_qt = abs(int(tpl.quantity_per_order))

            for j in range(0, we_qt):
                price_list.append(float(tpl.acppart_preis) / float(tpl.f_preisbasis))
                we_list.append(str(tpl.we).upper()) #currency

            supplier_list.append(tpl.ext_ktxt) #supplier
            order_list.append(tpl.beleg_nr_best) #order
            #substract and go for next if no next then -
            if i <= count:
                #substract all quantity
                df_matlist['quantity_per_order'][index] = float(tpl.quantity_per_order_without_avz) - quantity
            else:
                #substract part
                quantity = quantity - float(tpl.quantity_per_order_without_avz)
                df_matlist['quantity_per_order'][index] = 0
        else: #order is 0 or - ;  #if no next then -; will get all negative to last order
            price_list.append(float(tpl.acppart_preis) / float(tpl.f_preisbasis))
            we_list.append(str(tpl.we).upper()) #currency
            order_list.append(tpl.beleg_nr_best)  #order
            supplier_list.append(tpl.ext_ktxt) #supplier
            if i >= count:
                # substract all leftover quantity
                df_matlist['quantity_per_order'][index] = float(tpl.quantity_per_order_without_avz) - quantity
            pass
        i += 1


        #TODO: Universal function
        # check if we different and recount price to EUR if yes
        we_check = ([1 if we_list[0] == we else 0 for we in we_list])

        if len(we_check) == 0:
            print(tpl)
            print(we_list, '\n', we_check)
            we_check = ['EUR']


        if ((sum(we_check) / len(we_check)) == 1):
            we = we_list[0]
        else: #convert everything to EUR

            for x in range(0, len(we_list)):
                price_list[x] = price_list[x] * float(df_we['eur'][df_we['we'] == we_list[x]].values[0])
                we_list[x] = 'EUR'
            we = we_list[0]

    return order_list, supplier_list, sum(price_list)/len(price_list), we, df_matlist


def avz_matlist_setup(project: str, fz: str):
    #IMPORT OK
    matlist_table_name = 'materialliste'
    path_save = r'C:\Users\rytpio\Desktop\Projekty bieżące\AVZ'

    df_matlist = general_sql.get_table_multi_condition(matlist_table_name,
                                                       ['id'] + list(sql_import_map.materialliste_sql_col_dict.keys()),
                                                       ['komm', 'fz'], [project, str(fz)])
    # sum quantities on same positions in same order; 2 or more positions in same order
    # matlist has to be summed quantities by order_mnr - hoping that there are no different prices in an order
    df_matlist['quantity_per_fz'] = df_matlist['quantity_per_fz'].apply(lambda x: float(x))
    df_matlist['quantity_per_order'] = df_matlist.groupby(by=['mnr', 'beleg_nr_best'], sort=False)['quantity_per_fz'].transform('sum')
    df_matlist['quantity_per_order_without_avz'] = df_matlist['quantity_per_order']
    df_matlist = df_matlist.drop_duplicates(subset=['mnr', 'beleg_nr_best'])

    df = pd.read_excel(f'{path_save}\\test_avz_mat.xlsx')#, nrows=200)
    # df_purchased = df[df['purchase_level'] == 'x']
    df_purchased = df[df['mnr'].notnull()]

    df_we = general_sql.get_table('currency', True)
    df_we = df_we.set_axis(labels=['id'] + list(sql_import_map.currency_sql_col_dict.keys()), axis=1)
    df_we.sort_values(by=[list(sql_import_map.currency_sql_col_dict.keys())[2]], ascending=False, inplace=True)  # date
    df_we.drop_duplicates(subset=[list(sql_import_map.currency_sql_col_dict.keys())[0]], inplace=True)  # currency


    #TODO: Separate function
    #dla każdego zakupionego w AVZ;
    #df_purchased.to_excel(f'{path_save}\\test_avz_mat_purchased.xlsx', index=True, sheet_name='avz')
    order_list_master = []
    order_lst = []
    supplier_lst = []
    price_lst = []
    we_lst = []
    for row in df_purchased.itertuples(): #18121038
        prices = pd.DataFrame(df_matlist[df_matlist['mnr'] == str(row.artikel_nummer)])
        order_list, supplier_list, price, we,  df_matlist = substract_mat(float(row.anzahl_struct), prices, df_matlist, df_we)
        order_list_master = order_list_master + order_list
        order_lst.append(str.join(", ", order_list))
        supplier_lst.append(str.join(", ", supplier_list))
        price_lst.append(price)
        we_lst.append(we)

    df_purchased['order'] = pd.Series(order_lst)
    df_purchased['supplier'] = pd.Series(supplier_lst)
    df_purchased['price'] = pd.Series(price_lst)
    df_purchased['we'] = pd.Series(we_lst)

    df_purchased.to_excel(f'{path_save}\\test_avz_mat_purchased.xlsx', index=False, sheet_name='avz')

    df = df.join(df_purchased[['order', 'supplier', 'price', 'we']])
    df.to_excel(f'{path_save}\\test_avz_mat_price_incl.xlsx', index=False, sheet_name='avz')

    #spew summed up raports by knots ##sum
    #merge knot list; sum by breadcrumb lower every knot

    #spew not ordered parts



    df_not_ordered = df[(df['purchased_status_'] != 'ok')]
    df_not_ordered.to_excel(f'{path_save}\\test_avz_mat_not_ordered.xlsx', index=False, sheet_name='avz')

    df_matlist['avz'] = df_matlist['beleg_nr_best'].apply(lambda x: True if str(x) in order_list_master else False)
    df_matlist['quantity_delta'] = df_matlist.apply(lambda row: float(row.quantity_per_order) - float(row.quantity_per_order_without_avz), axis=1)
    df_matlist.to_excel(f'{path_save}\\test_avz_mat_after.xlsx', index=True, sheet_name='avz')


    #df.to_excel(f'{path_save}\\test_avz_mat_prices.xlsx', index=False, sheet_name='avz')

avz_matlist_setup('4473',  '12')
#TESTY TESTY i usprawnienia; usprawnienia - prędkość
#Wyjatki
#Na każdy pojazd projektu?
