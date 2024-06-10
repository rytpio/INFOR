import pandas as pd
import general_sql
from dicts_n_lists import sql_import_map
import os


def tree_plot_purchased(root_level: int, root_id: str, df_x: pd.DataFrame, purchased_list: list) -> pd.DataFrame():
    """
    function to drill down the tree, collecting list of purchased 'points'
    :param root_level: starting tree level
    :param root_id: starting tree point id
    :param df_x: tree dataframe
    :param purchased_list: list of tree points that are qualified as purchased
    :return: list of purchased tree points
    """
    df_x = df_x[df_x['breadcrumb'].str.contains(str(root_id))]
    df_x2 = df_x[df_x['level'] == root_level]
    level_lower = df_x2['stadler_id'].drop_duplicates().tolist()
    root_level2 = root_level + 1

    for lvl_l in level_lower:
        purchased_list.append(df_x['breadcrumb'][df_x['stadler_id'] == lvl_l].values[0])
        purchased_list = tree_plot_purchased(root_level2, lvl_l, df_x, purchased_list)

    return purchased_list


def tree_plot(root_level: int, root_id: str, df_x: pd.DataFrame, purchase_level_list: list,
              purchased_list: list) -> pd.DataFrame():
    """
    function to drill down tree, collecting points by which material was purchased and lower purchased points in this position
    :param root_level: starting tree level
    :param root_id: starting tree point id
    :param df_x: tree dataframe
    :param purchase_level_list: list of tree points that are qualified as level by which position was purchased (price contained)
    :param purchased_list: list of tree points that are qualified as purchased
    :return:
    """
    df_x = df_x[df_x['breadcrumb'].str.contains(str(root_id))]
    df_x2 = df_x[df_x['level'] == root_level]
    level_lower = df_x2['stadler_id'].drop_duplicates().tolist()
    parts_count = len(level_lower)
    purchase_count = 0
    root_level2 = root_level + 1

    for lvl_l in level_lower:
        # print(root_level, lvl_l)
        if df_x['material_list'][df_x['stadler_id'] == lvl_l].any():
            purchase_count += 1
            purchase_level_list.append(df_x['breadcrumb'][df_x['stadler_id'] == lvl_l].values[0])
            purchased_list.append(df_x['breadcrumb'][df_x['stadler_id'] == lvl_l].values[0])
            # print('m/a') #if found higher lvl; do not search lower
            # do lower only for purchased list
            purchased_list = tree_plot_purchased(root_level2, lvl_l, df_x, purchased_list)
        else:
            purchase_level_list, purchased_list = tree_plot(root_level2, lvl_l, df_x, purchase_level_list,
                                                            purchased_list)

    # risk with doubles
    if purchase_count == parts_count and parts_count > 0:
        prev_breadcrumb = df_x['breadcrumb'][df_x['stadler_id'] == level_lower[0]].values[0]
        prev_breadcrumb = prev_breadcrumb[:str(prev_breadcrumb).rfind("/")]
        # purchase_level_list.append(prev_breadcrumb)
        purchased_list.append(prev_breadcrumb)

    return purchase_level_list, purchased_list


def create_fz_avz(project: str, fz: str):
    avz_table_name = 'avz'
    matlist_table_name = 'material_list'
    path_save = r'C:\Users\rytpio\Desktop\Projekty bieżące\DATA'

    df_avz = general_sql.get_table_condition(avz_table_name, ['id'] + list(sql_import_map.avz_sql_col_dict.keys()),
                                             "project", project)

    df_matlist = general_sql.get_table_multi_condition(matlist_table_name, ['id'] + list(
        sql_import_map.material_list_sql_col_dict.keys()), ['project', 'fz'], [project, str(fz)])

    df_matlist_short = df_matlist[['stadler_id']].drop_duplicates()
    df_matlist_short['material_list'] = 'x'
    # df_matlist_short = df_matlist.drop_duplicates(subset=['stadler_id'])
    df = pd.merge(left=df_avz, right=df_matlist_short, how='left',
                  on=['stadler_id'], suffixes=['_avz', '_material_list'])
    # merge to mark avz positions which have corresponding matlist counterparts with x

    # df.to_excel(f'{path_save}\\test_merge.xlsx', index=False, sheet_name='avz')

    # TODO: separate function
    base_level = 0
    root_level = base_level + 1
    level0 = df['stadler_id'][(df['level'] == base_level)].drop_duplicates().tolist()  # list of first level list of id
    purchase_level_list = list()
    purchased_list = list()
    for lvl0 in level0:  # for each id in id list
        # if root level(0) prc is not empty then call 'mat/acc' and next
        if df['material_list'][df['stadler_id'] == lvl0].any():  # or df['category'][df['stadler_id'] == lvl0].any():
            purchase_level_list.append(df['breadcrumb'][df['stadler_id'] == lvl0].values[0])
            purchased_list.append(df['breadcrumb'][df['stadler_id'] == lvl0].values[0])
            # print('level 0 bought: ' + lvl0)
            # search lower to mark purchased list
            purchased_list = tree_plot_purchased(root_level, lvl0, df, purchased_list)
        else:
            purchase_level_list, purchased_list = tree_plot(root_level, lvl0, df, purchase_level_list, purchased_list)

    # print(purchased_list == purchase_level_list)
    # print(purchase_level_list)
    # print(purchased_list)

    df_purchase_level = pd.DataFrame(data=purchase_level_list, columns=['breadcrumb']).drop_duplicates()
    df_purchase_level['purchase_level'] = 'x'
    df = df.merge(df_purchase_level, how='left', left_on='breadcrumb',
                  right_on='breadcrumb')  # merge with x what was purchased

    df_purchased = pd.DataFrame(data=purchased_list, columns=['breadcrumb']).drop_duplicates()
    df_purchased['purchased_status_exact'] = 'ok'
    df = df.merge(df_purchased, how='left', left_on='breadcrumb', right_on='breadcrumb')
    cat_ok_list = ['bolts_misc', 'chemicals', 'diverse', 'hoses_pneumatic', 'nuts', 'screws',
                   'specification', 'washers', 'unassigned', 'struct_mechanic', 'struct_electric', 'struct_pneumatic']
    df['purchased_status_general'] = df.apply(lambda row: 'ok' if row.pos_nr_category_bu_1951939 in cat_ok_list
    else row.purchased_status_exact, axis=1)

    df.to_excel(f'{path_save}\\{project}_avz_mat.xlsx', index=False, sheet_name='avz')
    #  ??? Purchase level is not working.


def substract_mat(quantity: float, prices: pd.DataFrame, df_matlist: pd.DataFrame, df_we: pd.DataFrame) -> \
        [list, list, float, float, float, str, pd.DataFrame]:
    """
    prices can be different; take price 1 if is enough; if completed from more than 1 then flag and take average
    one order can be insufficient for avz completion
    two orders can be done in different currencies; default is EUR if more than 1

    take quantity from avz position, price list from materiallist for position, materiallist, currency
    take first price & quantity; substract from order; if not enough take price and quantity from next

    :param quantity:
    :param prices:
    :param prices:
    :param prices:
    :param df_matlist:
    :param df_we:
    :return:
    """
    quantity_org = quantity
    supplier_list = []
    order_list = []
    price_list = []
    we_list = []
    we = None  # no option for no we in case of correct data; otherwise will result in error
    count = len(prices)
    i = 0
    for tpl in prices.itertuples():
        # print(tpl)
        index = df_matlist[
            (df_matlist['stadler_id'] == tpl.stadler_id) & (df_matlist['order_id'] == tpl.order_id)].index
        # print(df_matlist['quantity_per_order'][index], 1)
        if float(tpl.quantity_order_minus_avz) >= quantity:  # order is enough then substract
            price_list.append(float(tpl.unit_price) / float(tpl.unit_price_basis))
            we_list.append(str(tpl.currency).upper())  # currency
            order_list.append(tpl.order_id)  # order
            if tpl.supplier not in supplier_list: supplier_list.append(tpl.supplier)  # supplier
            # substract and end function
            df_matlist['quantity_order_minus_avz'][index] = float(tpl.quantity_order_minus_avz) - quantity
            # print(df_matlist['quantity_order_minus_avz'][index], 2)
            price_eur = price_list[0] * float(df_we['EUR'][df_we['CURRENCY'] == we_list[0]])
            price_eur_sum = price_eur * quantity_org
            return order_list, supplier_list, price_list[0], price_eur, price_eur_sum, we_list[0], df_matlist
        elif float(tpl.quantity_order_minus_avz) > 0:
            # order is not enough but not 0 #not necessarily works with different orders 12035922
            # on if was take from order without avz instead of order
            if int(tpl.quantity_order_minus_avz) == 0:
                we_qt = 1
            else:
                we_qt = abs(int(tpl.quantity_order_minus_avz))

            for j in range(0, we_qt):
                price_list.append(float(tpl.unit_price) / float(tpl.unit_price_basis))
                we_list.append(str(tpl.currency).upper())  # currency

            if tpl.supplier not in supplier_list: supplier_list.append(tpl.supplier)  # supplier
            order_list.append(tpl.order_id)  # order
            # substract and go for next if no next then -
            if i >= count:
                # substract all leftover quantity
                df_matlist['quantity_order_minus_avz'][index] = float(tpl.quantity_order_minus_avz) - quantity
            else:
                # substract part
                quantity = quantity - float(tpl.quantity_order_minus_avz)
                df_matlist['quantity_order_minus_avz'][index] = 0
        else:  # order is 0 or - ;  #if no next then -; will get all negative to last order
            price_list.append(float(tpl.unit_price) / float(tpl.unit_price_basis))
            we_list.append(str(tpl.currency).upper())  # currency
            order_list.append(tpl.order_id)  # order
            if tpl.supplier not in supplier_list: supplier_list.append(tpl.supplier)  # supplier
            if i >= count:
                # substract all leftover quantity
                df_matlist['quantity_order_minus_avz'][index] = float(tpl.quantity_order_minus_avz) - quantity  #w/o
            else:
                quantity = quantity - float(tpl.quantity_order_minus_avz)
                df_matlist['quantity_order_minus_avz'][index] = 0
                #print('Count not reached and no quantity left - error in algorithm. SubstractMat')
        i += 1

        # TODO: Universal function
        # check if currecny is different and recount price to EUR if yes
        we_check = ([1 if we_list[0] == we else 0 for we in we_list])

        if len(we_check) == 0:
            print(tpl)
            print(we_list, '\n', we_check)
            we_check = ['EUR']

        if (sum(we_check) / len(we_check)) == 1:
            we = we_list[0]
        else:  # convert everything to EUR

            for x in range(0, len(we_list)):
                price_list[x] = price_list[x] * float(df_we['EUR'][df_we['CURRENCY'] == we_list[x]].values[0])
                we_list[x] = 'EUR'
            we = we_list[0]

    price_we = sum(price_list) / len(price_list)
    price_eur = price_we * float(df_we['EUR'][df_we['CURRENCY'] == we])
    price_eur_sum = price_eur * quantity_org
    return order_list, supplier_list, price_we, price_eur, price_eur_sum, we, df_matlist


def avz_matlist_setup(project: str, fz: str):
    """
    Take material_list and avz; see what was purchased.
    Based on purchased AVZ parts; remove avz quantities from materiallist.
    Discrepancies should result in NRC, extra/unassigned to documentation orders, AP/C-mat orders or
    orders outside doc-tree. (main component + subcomponents bought) - all to be assigned manually
    :param project:
    :param fz:
    :return:
    """

    # IMPORT OK
    matlist_table_name = 'material_list'
    path_save = r'C:\Users\rytpio\Desktop\Projekty bieżące\DATA'

    df_matlist = general_sql.get_table_multi_condition(matlist_table_name,
                                                       ['id'] + list(sql_import_map.material_list_sql_col_dict.keys()),
                                                       ['project', 'fz'], [project, str(fz)])

    #TODO: Test if sql non empty
    #print(df_matlist.shape)
    # sum quantities on same positions in same order; 2 or more positions in same order
    # matlist has to be summed quantities by order_mnr - hoping that there are no different prices in an order
    df_matlist['quantity_per_fz'] = df_matlist['quantity_per_fz'].apply(lambda x: float(x))
    df_matlist['quantity_per_order'] = df_matlist.groupby(by=['stadler_id', 'order_id'], sort=False)[
        'quantity_per_fz'].transform('sum')  # sum of all ordered quantities
    df_matlist['quantity_order_minus_avz'] = df_matlist['quantity_per_order']
    df_matlist = df_matlist.drop_duplicates(subset=['stadler_id', 'order_id'])

    df = pd.read_excel(
        f'{path_save}\\{project}_avz_mat.xlsx')  #, nrows=500) ##SQL avz doesn't have purchase level column of cross reference with matlist
    # df = general_sql.get_table_condition('avz', ['id'] + list(sql_import_map.avz_sql_col_dict.keys()),
    #                                      'project', project)
    df_purchased = df[df['purchase_level'] == 'x']
    #df_purchased = df[df['stadler_id'].notnull()]
    #print(df_purchased.shape)

    df_we = general_sql.get_table('currency_data', True)
    df_we = df_we.set_axis(labels=['id'] + list(sql_import_map.currency_sql_col_dict.keys()), axis=1)
    df_we.sort_values(by=[list(sql_import_map.currency_sql_col_dict.keys())[2]], ascending=False, inplace=True)  # date
    df_we.drop_duplicates(subset=[list(sql_import_map.currency_sql_col_dict.keys())[0]], inplace=True)  # currency

    # TODO: Separate function
    # dla każdego zakupionego w AVZ;
    df_purchased.to_excel(f'{path_save}\\{project}_avz_mat_purchased_1.xlsx', index=True, sheet_name='avz')
    order_list_master = []
    order_lst = []
    supplier_lst = []
    price_lst = []
    price_eur_lst = []
    price_eur_sum_lst = []
    we_lst = []

    for row in df_purchased.itertuples():  # 18121038

        if str(row.stadler_id) == '12035922':
            print('x')
        prices = pd.DataFrame(df_matlist[df_matlist['stadler_id'] == str(row.stadler_id)])
        #wybierz stadler_id - teoretycznie kilkukrotnie wybierze ten sam,
        # teoretycznie ma zwrócić tylko dane do zamówienia dla danej pozycji i resztę materiallisty po przepatrzeniu
        order_list, supplier_list, price_we, price_eur, price_eur_sum, we, df_matlist = \
            substract_mat(float(row.avz_quantity_in_tree), prices, df_matlist, df_we)

        order_list_master = order_list_master + order_list
        order_lst.append(str.join(", ", order_list))
        supplier_lst.append(str.join(", ", supplier_list))
        price_lst.append(price_we)
        we_lst.append(we)
        price_eur_lst.append(price_eur)
        price_eur_sum_lst.append(price_eur_sum)

    #print(y, len(order_lst), len(supplier_lst), len(price_lst), len(we_lst))
    #46 list out of 46- something doesnt' work in series
    df_purchased['order'] = pd.Series(order_lst).values
    df_purchased['supplier'] = pd.Series(supplier_lst).values
    df_purchased['price'] = pd.Series(price_lst).values
    df_purchased['currency'] = pd.Series(we_lst).values
    df_purchased['price_eur'] = pd.Series(price_eur_lst).values
    df_purchased['price_eur_sum'] = pd.Series(price_eur_sum_lst).values

    df_purchased.to_excel(f'{path_save}\\{project}_avz_mat_purchased_2.xlsx', index=False, sheet_name='avz')
    df_pur = df_purchased[
        ['order', 'supplier', 'price', 'currency', 'price_eur', 'price_eur_sum', 'avz_struct_index', 'id']]
    #df = df.join(df_pur, on='avz_struct_index', how='left', rsuffix='_material_list', validate='1:1')
    df = df.merge(df_pur, on=['avz_struct_index', 'id'], how='left', validate='1:1')
    #right, inner should be same, outside always 0

    df.to_excel(f'{path_save}\\{project}_avz_mat_price_incl.xlsx', index=False, sheet_name='avz')

    # spew summed up raports by knots ##sum
    # merge knot list; sum by breadcrumb lower every knot

    # spew not ordered parts

    df_not_ordered = df[(df['purchased_status_general'] != 'ok')]
    df_not_ordered.to_excel(f'{path_save}\\{project}_avz_mat_not_ordered.xlsx', index=False, sheet_name='avz')

    df_matlist['avz'] = df_matlist['order_id'].apply(lambda x: True if str(x) in order_list_master else False)
    df_matlist.to_excel(f'{path_save}\\{project}_avz_mat_after.xlsx', index=True, sheet_name='avz')

    df.to_excel(f'{path_save}\\{project}_avz_mat_prices.xlsx', index=False, sheet_name='avz')
    # mat_prices - avz with order_supplier_price_currency info
    # avz_mat_after - materiallist after crosscheck with avz
    # mat_not_ordered - potentially missing data (is in avz, not in materiallist)

    #import to mat_fz_avz_knot list
    general_sql.drop_table_rows('avz_mat_knot', [[project], [fz]],
                                ['project', 'fz'], column_type=[['varchar'],['']])  #usun stare wpisy

    df_mat_knot = df[['project', 'id', 'breadcrumb', 'purchase_level', 'purchased_status_exact',
                      'purchased_status_general', 'order', 'supplier_y', 'price', 'currency',
                      'price_eur', 'price_eur_sum']]
    df_mat_knot.columns = ['project', 'avz_id', 'avz_breadcrumb', 'purchase_level', 'purchased_status_exact',
                           'purchased_status_general', 'order_id', 'supplier_mat', 'price', 'currency',
                           'price_eur', 'price_eur_sum']
    df_mat_knot['fz'] = fz
    df_mat_knot['fk_avz'] = None

    general_sql.insert_into_table('avz_mat_knot', df_mat_knot, sql_import_map.avz_mat_knot_sql_col_dict)

    general_sql.update_fk(['avz_mat_knot'], 'avz', 'fk_avz', project, 'id',
                          'avz_id')  # ten sam plik powinno się dać wygenerować


project = '4503'
fz = '1'
create_fz_avz(project, fz)
avz_matlist_setup(project, fz)

#---------------------------------------------------------------
#For each in AVZ / matlist - take quantity and orders written
#First order find and take quantity into new df with avz knot1/2/3 /MASK
#If any quantity left then go next; if quantity exact then leave out 0; if quantity not enough go for next order
#Do for whole AVZ in matlist; copy leftover materiallist - later to add on apparateliste/cable/bossard/ktl-kanban/leftover description
#If mask completed then add mask on top - result should be for complete materiallist grouped for each project
#IMPORTANT: Write all that quantity on last order is still not reached (possible material movement)
#Similar needs to be done on apparateliste as it can be n:n;

