import pandas as pd
from SQL import general_sql
from dicts_n_lists import sql_import_map


def material_leftovers(project: str):
    """

    :param project:
    :return:
    """

    col_list_dev = list(sql_import_map.device_list_sql_col_dict.keys())
    df_dev = general_sql.get_table_condition('device_list', (['id'] + col_list_dev),
                                             'project', project)
    df_dev['src'] = 'dev'
    df_dev = df_dev[['stadler_id', 'group_mask', 'src']].drop_duplicates()
    df_dev['stadler_id'] = df_dev['stadler_id'].apply(lambda x: str(x).replace("_x000D_", ""))


    col_list_avz_knot = list(sql_import_map.avz_knot_sql_col_dict.keys())
    df_avz_knot = general_sql.get_table_condition('avz_knot', (['id'] + col_list_avz_knot),
                                                  'project', project)

    df_avz_knot = df_avz_knot[['avz_breadcrumb', 'group_mask']].drop_duplicates()
    df_avz_knot['stadler_id'] = df_avz_knot.apply(
        lambda row: str(row.avz_breadcrumb)[str(row.avz_breadcrumb).rfind("/") + 1:], axis=1)
    df_avz_knot['src'] = 'avz'
    df_avz_knot = df_avz_knot[['stadler_id', 'group_mask', 'src']].drop_duplicates()

    df_group_mask = pd.concat(objs=[df_dev, df_avz_knot], axis=0, join='outer',
                              ignore_index=False, levels=None).drop_duplicates()
    # df_group_mask.to_excel(r'C:\Users\rytpio\Desktop\Projekty bieżące\DATA\MATERIAL_LIST_LEFTOVER\df_group_mask.xlsx',
    #                              index=False)

    #usun puste-ew. do wygenerowania pozniej
    #df_group_mask.dropna(subset='group_mask', inplace=True)

    #TODO: Powtórzyć sobie nauke i przećwiczyć pandas group/agg/map oraz regex

    df_group_mask = df_group_mask.groupby('stadler_id')['group_mask'].agg(lambda x: list(x))
    df_group_mask = pd.DataFrame(df_group_mask).reset_index()

    def list_to_str(x, limit: bool) -> str:
        x = list(dict.fromkeys(x))
        x_out = ''
        if len(x) > 6 and limit:
            return "UNIVERSAL_PART"  #add limit for more than 6
        elif len(x) > 0:
            x_out = str.join(",", [str(y) for y in x])
        else:
            x_out = ''

        dbl_check = list(dict.fromkeys(str(x_out).split(',')))
        try:
            dbl_check.pop(dbl_check.index('nan'))
            dbl_check.pop(dbl_check.index(''))
        except (Exception):
            pass
        x_out = str.join(",", [str(y) for y in dbl_check])

        return str(x_out)

    df_group_mask['group_mask'] = df_group_mask['group_mask'].apply(lambda x: list_to_str(x, True))

    query = ("SELECT DISTINCT material_list.project, material_list.stadler_id, material_list.order_id "
             "FROM material_list "
             f"WHERE material_list.project = '{project}' "
             "ORDER BY material_list.order_id ASC")

    query_col_list = ['project', 'stadler_id', 'order_id']
    df_matlist = general_sql.get_query(query, query_col_list)

    df_matlist = pd.merge(left=df_matlist, right=df_group_mask, how='left',
                          left_on='stadler_id', right_on='stadler_id', copy=True)

    #add according to stadler id and order and then only smear on order data
    #take all group_masks assigned to order and make list assign to order itself
    df_matlist = df_matlist[['stadler_id', 'order_id', 'group_mask']].drop_duplicates()
    # df_matlist_stadler_id = df_matlist.groupby('stadler_id', 'order_id')['group_mask'].agg(
    #     lambda x: list(x)).reset_index()  # Tutaj grupuje po zamówieniach
    df_matlist_order_id = df_matlist.groupby('order_id')['group_mask'].agg(lambda x: list(x)).reset_index() #Tutaj grupuje po zamówieniach

    #df_matlist_stadler_id['group_mask'] = df_matlist_stadler_id['group_mask'].apply(lambda x: list_to_str(x, False))
    df_matlist_order_id['group_mask'] = df_matlist_order_id['group_mask'].apply(lambda x: list_to_str(x, False))


    # df_matlist.to_excel(r'C:\Users\rytpio\Desktop\Projekty bieżące\DATA\MATERIAL_LIST_LEFTOVER\df_matlist_2.xlsx',
    #                              index=False)

    query_2 = ("SELECT DISTINCT "
    "CAST(material_list.unit_price AS FLOAT) / CAST(material_list.unit_price_basis AS FLOAT) * SUM(CAST(material_list.quantity_per_fz AS FLOAT)) as \"order_sum\","
    "material_list.currency, material_list.bg_general,"
    "SUM(CAST(material_list.quantity_per_fz AS FLOAT)) as \"fz_quantity\", "
    "material_list.project, material_list.nrc, material_list.order_id,"
    "material_list.stadler_id, material_list.description_1, material_list.supplier_id,"
    "material_list.supplier_description_1, material_list.supplier"
    " FROM material_list"
    " WHERE "
    f"material_list.project = '{project}' and "
    "material_list.fk_bossard_kanban_staps IS NULL and "
    "material_list.fk_ktl_kanban_staps IS NULL and "
    "material_list.fk_device_list IS NULL and "
    "material_list.fk_avz IS NULL and "
    "material_list.fk_cable_quantity IS NULL"
    " GROUP BY "
    "material_list.order_id, material_list.stadler_id, material_list.project,material_list.description_1, material_list.supplier_id,"
    "material_list.supplier_description_1, material_list.supplier, material_list.currency, material_list.bg_general,"
    "material_list.nrc,material_list.unit_price, unit_price_basis, material_list.order_quantity")

    query_2_col_list = ['order_sum', 'currency', 'bg_general', 'fz_quantity', 'project', 'nrc', 'order_id', 'stadler_id',
                        'description_1', 'supplier_id', 'supplier_description_1', 'supplier']

    df_matlist_leftover = general_sql.get_query(query_2, query_2_col_list)
    #df_matlist_leftover.to_excel(r'C:\Users\rytpio\Desktop\Projekty bieżące\DATA\MATERIAL_LIST_LEFTOVER\df_matlist_leftover_1.xlsx', index=False)

    #supply only non-0 matlist-leftover
    df_matlist_leftover = pd.merge(left=df_matlist_leftover, right=df_matlist_order_id, left_on='order_id', right_on='order_id',
                                   how='left', copy=True).drop_duplicates(subset=['order_id', 'stadler_id'])
    df_matlist_leftover['single_group'] = df_matlist_leftover['group_mask'].apply(lambda x: len(str(x).split(',')) == 1)



    df_matlist_leftover.to_excel(f'C:\\Users\\rytpio\\Desktop\\Projekty bieżące\\DATA\\MATERIAL_LIST_LEFTOVER\\{project}_leftover_draft2.xlsx',
                                 index=False)


# get materiallist all and interwind with group (unique order_stadler_id)
# -> multiply for all order ID - flatten :O
# can be multi for some orders - take biggest
# filter out all not cable/avz/dev/ktl/bossard


material_leftovers('4541')

#TODO: Need to place "empty" positions in case of not yet bought material example. 1-15 L-4541 Sarajevo vs 16-25 Sarajevo