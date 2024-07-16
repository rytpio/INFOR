import pandas as pd
from SQL import general_sql
from dicts_n_lists import sql_import_map

def fast_matlist(project: str):
    query_2 = ("SELECT * FROM material_list"
               " WHERE "
               f"material_list.project = '{project}'")

    # query_2 = ("SELECT * FROM material_list"
    #            )

    query_2_col_list = list(sql_import_map.material_list_sql_col_dict.keys())

    df_matlist = general_sql.get_query(query_2, ['id'] + query_2_col_list)


    df_matlist.to_excel(
        f'C:\\Users\\rytpio\\Desktop\\Projekty bieżące\\DATA\\MATERIAL_LIST_LEFTOVER\\df_matlist_{project}.xlsx',
        index=False)

    # df_matlist.to_csv(
    #     f'C:\\Users\\rytpio\\Desktop\\Projekty bieżące\\DATA\\MATERIAL_LIST_LEFTOVER\\df_matlist_{project}.csv',
    #     index=False, sep=';')
    #

def complete_matlist(project: str):
    #import materiallist - complete
    #get leftover keys

    col_list_dev = list(sql_import_map.device_list_sql_col_dict.keys())
    df_dev = general_sql.get_table_condition('device_list', (['id'] + col_list_dev),
                                             'project', project)
    df_dev['src'] = 'dev'
    df_dev = df_dev[['stadler_id', 'group_mask', 'src']].drop_duplicates()

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

    df_group_mask = df_group_mask.groupby('stadler_id')['group_mask'].agg(lambda x: list(x))
    df_group_mask = pd.DataFrame(df_group_mask).reset_index()

    def list_to_str(x, limit: bool) -> str:
        x = list(dict.fromkeys(x))
        x_out = ''
        if len(x) > 3 and limit:
            return "UNIVERSAL_PART"  # add limit for more than 3
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

    # smear on order
    # take all group_masks assigned to order and make list assign to order itself
    df_matlist = df_matlist[['order_id', 'group_mask']].drop_duplicates()
    df_matlist = df_matlist.groupby('order_id')['group_mask'].agg(lambda x: list(x)).reset_index()
    df_matlist['group_mask'] = df_matlist['group_mask'].apply(lambda x: list_to_str(x, False))

    #pobierz left-over i scal; tam gdzie nie ma wpisz
    col_list_leftover = list(sql_import_map.material_list_leftover_sql_col_dict.keys())
    df_leftover = general_sql.get_table_condition('material_list_leftover', (['id'] + col_list_leftover),
                                                  'project', project)
    df_leftover = df_leftover[
        ['bg_set', 'should_be_included', 'group_mask', 'order_id', 'stadler_id', 'leftover_Acomp']].drop_duplicates()

    df_matlist = (pd.concat(objs=[df_matlist, df_leftover], axis=0, join='outer', ignore_index=True, levels=None)
                  .drop_duplicates(subset=['order_id']))

    # df_matlist.to_excel(
    #     r'C:\Users\rytpio\Desktop\Projekty bieżące\DATA\MATERIAL_LIST_LEFTOVER\df_matlist_check_dict.xlsx',
    #     index=False)

    query_2 = ("SELECT * FROM material_list"
               " WHERE "
               f"material_list.project = '{project}'")

    query_2_col_list = list(sql_import_map.material_list_sql_col_dict.keys())

    df_matlist_leftover = general_sql.get_query(query_2, ['id'] + query_2_col_list)

    #print(query_2)
    df_matlist_leftover = pd.merge(left=df_matlist_leftover, right=df_matlist, left_on='order_id', right_on='order_id',
                                   how='left', copy=True).drop_duplicates()
    df_matlist_leftover['single_group'] = df_matlist_leftover['group_mask'].apply(lambda x: len(str(x).split(',')) == 1)
    #print(df_matlist_leftover)

    df_matlist_leftover.to_excel(
        f'C:\\Users\\rytpio\\Desktop\\Projekty bieżące\\DATA\\MATERIAL_LIST_LEFTOVER\\df_matlist_3_{project}.xlsx',
        index=False)


#print(df)

#complete_matlist('4541')
fast_matlist('4541')