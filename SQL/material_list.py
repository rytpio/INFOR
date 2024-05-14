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

    # general_sql.drop_table(table_name)
    # general_sql.create_table(table_name, table_name, columns | fk_columns)

    df = import_infor_data(project, standard, path_raw, path_processed)

    df_bossard_kanban_staps = general_sql.get_table_col('bossard_kanban_staps', ['id'] + list(
        reference_map.sql_col.get('bossard_kanban_staps').keys()))

    df_ktl_kanban_staps = general_sql.get_table_col('ktl_kanban_staps',
                                                    ['id'] + list(reference_map.sql_col.get('ktl_kanban_staps').keys()))

    df_ktl_kanban_stag = general_sql.get_table_col('ktl_kanban_stag',
                                                   ['id'] + list(reference_map.sql_col.get('ktl_kanban_stag').keys()))

    df_cable_quantity = general_sql.get_table_col_condition('cable_quantity',
                                                            ['id'] + list(
                                                                reference_map.sql_col.get('cable_quantity').keys()),
                                                            'project', project)

    df['fk_bossard_kanban_staps'] = df['stadler_id'] \
        .apply(lambda x: general_sql.one_step_fk(df_bossard_kanban_staps, 'stadler_id', x))
    df['fk_ktl_kanban_staps'] = df['stadler_id'] \
        .apply(lambda x: general_sql.one_step_fk(df_ktl_kanban_staps, 'stadler_id', x))
    df['fk_ktl_kanban_stag'] = df['stadler_id'] \
        .apply(lambda x: general_sql.one_step_fk(df_ktl_kanban_stag, 'stadler_id', x))
    df['fk_cable_quantity'] = df['stadler_id'] \
        .apply(lambda x: general_sql.one_step_fk(df_cable_quantity, 'stadler_id', x))

    # general_sql.drop_table_content(table_name)  # usun stare wpisy
    df = df.applymap(lambda x: x[:255] if len(str(x)) > 255 else x)  # cut characters to 255
    # TODO: initially would be best if during file import length from sql_column
    #  get's imported and column is cutted accordingly
    # for col in sql_cols:
    # if if VARCHAR in string then get () from VARCHAR
    # cut VARCHAR column to selected length
    df.to_csv(path_processed, index=False, sep=';')
    general_sql.insert_into_table(table_name, df, columns)


material_list("4547", "STAPS_single")

#
# def import_many():
#     many = ['4388', '4413', '4421', '4423','4431','4444','4473','4503','4547']
#     for proj in many:
#         print(proj)
#         material_list(str(proj), "STAPS_single")
#
#
# import_many()
