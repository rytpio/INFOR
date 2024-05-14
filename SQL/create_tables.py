import pandas as pd
from dicts_n_lists import reference_map
from SQL import general_sql

def create_tables():
    """
    Creates tables at initial stage of SQL set-up
    // target is to move databases without dropping tables
    // target is to "update" filled databases without droping / creating new ones - is time consuming in case of materiallist with many
    relations to other tables with cascade removal / update
    :return:
    """
    table_names_lst = ['currency_data', 'bossard_price_staps', 'bossard_kanban_staps', 'cable_data', 'cable_quantity',
                       'ktl_kanban_stag','ktl_kanban_staps', 'device_list', 'avz', 'wz', 'material_list']
    fk_list = [False, False, False, False, False, False, False, True, False, False, True]

    for table_name in table_names_lst:
        columns = reference_map.sql_col.get(table_name)
        general_sql.drop_table(table_name)
        if fk_list[table_names_lst.index(table_name)]:
            fk_columns = reference_map.sql_fk_col.get(table_name)
            general_sql.create_table(table_name, table_name, columns | fk_columns)
        else:
            general_sql.create_table(table_name, table_name, columns)
            pass

create_tables()