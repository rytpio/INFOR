import pandas as pd
from dicts_n_lists import reference_map
from SQL import general_sql


def ktl_kanban_staps():
    """ pozycje """
    table_name = 'ktl_kanban_staps'
    path = reference_map.file_path_dicts.get(table_name)
    columns = reference_map.sql_col.get(table_name)

    general_sql.drop_table(table_name)
    general_sql.create_table(table_name, table_name, columns)

    df = pd.read_excel(path)
    df.drop_duplicates(subset=['stadler_id'], inplace=True)  # DOTO: duble, ewentualnie do wylapania i raportu
    df.dropna(subset=['stadler_id'], inplace=True)
    # general_sql.insert_into_table(table_name, df, columns)
    # general_sql.get_table(table_name)
    general_sql.insert_into_table_new_one_step(table_name, df, list(columns), 'stadler_id', 'stadler_id')

    # Update foreign keys on tables related
    # general_sql.update_table_fk_one_step('ktl_kanban_staps', 'device_list',
    #                                      list(reference_map.sql_col.get('ktl_kanban_staps').keys()),
    #                                      list(reference_map.sql_col.get('device_list').keys()),
    #                                      'stadler_id', 'stadler_id', 'fk_ktl_kanban_staps')
    #
    # general_sql.update_table_fk_one_step('ktl_kanban_staps', 'wz',
    #                                      list(reference_map.sql_col.get('ktl_kanban_staps').keys()),
    #                                      list(reference_map.sql_col.get('wz').keys()),
    #                                      'stadler_id', 'stadler_id', 'fk_ktl_kanban_staps')
    #
    # general_sql.update_table_fk_one_step('ktl_kanban_staps', 'material_list',
    #                                      list(reference_map.sql_col.get('ktl_kanban_staps').keys()),
    #                                      list(reference_map.sql_col.get('material_list').keys()),
    #                                      'stadler_id', 'stadler_id', 'fk_ktl_kanban_staps')


ktl_kanban_staps()

general_sql.update_fk(['wz', 'device_list', 'material_list','avz', 'wz'],
                      'ktl_kanban_staps','fk_ktl_kanban_staps','')


