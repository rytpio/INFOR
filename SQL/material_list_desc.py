import pandas as pd
import general_sql
from dicts_n_lists import sql_import_map


def device_list_description(project: str, fz: int) -> None:
    '''
    :return:
    '''
    col_list_dev = list(sql_import_map.device_list_sql_col_dict.keys())
    df_dev = general_sql.get_table_condition('device_list', [['id'] + col_list_dev],
                                             'project', project)

    query = ('SELECT SUM(stk_sum) as "stk_sum",'
             'device_list.project, device_list.stadler_id, device_list.main_group, '
             'device_list.secondary_group, device_list.description_1, device_list.description_2, device_list.type,'
             'device_list.supplier, device_list.supplier_id'
             'FROM device_list'
             'WHERE'
             f'device_list.project = {project} and '
             'NOT device_list.fk_material_list IS NULL '
             'and device_list.fk_ktl_kanban_staps IS NULL'
             'GROUP BY device_list.project,device_list.stadler_id, device_list.main_group, device_list.secondary_group,'
             'device_list.description_1, device_list.description_2, device_list.type,'
             'device_list.supplier, device_list.supplier_id')

    col_list_mat = list(sql_import_map.material_list_sql_col_dict.keys())
    df_mat = general_sql.get_table_multi_condition('material_list', [['id'] + col_list_mat],
                                                   ['project', 'fz'], [project, fz])

    #get ap
    #get matlist for fz
    #assing device list keys to matlist - divide order
    #to co robie to tak naprawdę tworzę funkcje 1:n dla relacji między bazami;
    # ---- TODO: Po uporządkowaniu zmienić w relacje?

    #1st ap where matlist
    #for each ap found create new matlist_lines; modify previous matlist quantity lines
    #if not enough quantity then add -
    #after completed ap add leftover non-0 quantity matlist


    print(df_mat)


def avz_description():
    pass


def leftover_material():
    pass


device_list_description("4547", "1")
