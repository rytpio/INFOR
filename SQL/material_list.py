import pandas as pd
from dicts_n_lists import reference_map
from SQL import general_sql
from import_materialliste import import_infor_data

def material_list(project: str, standard: str):
    """ """
    table_name = 'material_list'
    path_raw = reference_map.file_path_dicts.get(project).get('material_list_raw')
    path_processed = reference_map.file_path_dicts.get(project).get('material_list_processed')
    columns = reference_map.sql_col.get(table_name)
    fk_columns = reference_map.sql_fk_col.get(table_name)

    #general_sql.drop_table(table_name)
    general_sql.create_table(table_name, table_name, columns | fk_columns)

    df = import_infor_data(project, standard, path_raw, path_processed)

    df_bossard_kanban_staps = general_sql.get_table_col('bossard_kanban_staps', ['id'] + list(
        reference_map.sql_col.get('bossard_kanban_staps').keys()))

    df_ktl_kanban_staps = general_sql.get_table_col('ktl_kanban_staps',
                                                    ['id'] + list(reference_map.sql_col.get('ktl_kanban_staps').keys()))

    df_ktl_kanban_stag = general_sql.get_table_col('ktl_kanban_stag',
                                                   ['id'] + list(reference_map.sql_col.get('ktl_kanban_stag').keys()))

    df_kabel_quantity = general_sql.get_table_col_condition('cable_quantity',
                                                            ['id'] + list(
                                                                reference_map.sql_col.get('cable_quantity').keys()),
                                                            'project', project)

    df['fk_bossard_kanban_staps'] = df['stadler_id']\
        .apply(lambda x: general_sql.one_step_fk(df_bossard_kanban_staps, 'stadler_id', x))
    df['fk_ktl_kanban_staps'] = df['stadler_id']\
        .apply(lambda x: general_sql.one_step_fk(df_ktl_kanban_staps, 'stadler_id', x))
    df['fk_ktl_kanban_stag'] = df['stadler_id']\
        .apply(lambda x: general_sql.one_step_fk(df_ktl_kanban_stag, 'stadler_id', x))
    df['fk_kabel_quantity'] = df['stadler_id']\
        .apply(lambda x: general_sql.one_step_fk(df_kabel_quantity, 'stadler_id', x))

    ## kontrola długosci poszczególnych VARCHAR // NIE - używać TEXT zamiast VARCHAR
    # df_len = df.applymap(lambda x: 'NOTOK' if len(str(x)) > 255 else 'OK')
    # df_len.to_excel(r'C:\Users\rytpio\Desktop\Projekty bieżące\4423_TEST\other_data\apcheck.xlsx',index=False)

    # general_sql.drop_table_content(table_name)  # usun stare wpisy
    general_sql.insert_into_table(table_name, df, columns)

    general_sql.get_table(table_name)


material_list("4473", "STAPS_single")
