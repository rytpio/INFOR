import pandas as pd
from dicts_n_lists import reference_map
from SQL import general_sql
from import_WZ import import_struktur


def wz_struktur_staps(project: str, project_location: str):  # tylko zrzut "nur 01er Listen? NEIN" = aktualny stan materiału który schodzi na WZ
    table_name = 'wz'
    #path = source_dicts.file_path_dicts.get(table_name)
    columns = reference_map.sql_col.get(table_name)
    path_read = reference_map.file_path_dicts.get(project).get('wz_raw')
    path_save = reference_map.file_path_dicts.get(project).get('wz_processed')

    #general_sql.drop_table(table_name)
    general_sql.create_table(table_name, table_name, columns)

    df = import_struktur(project, project_location, path_read, path_save)
    #  df = pd.read_csv(path_df, sep=';', low_memory=False)

    for col in df.columns.tolist():
        if col in ['level', 'sort', 'sort_1']:
            df[col] = df[col].astype(int)
        elif col in ['wz_quantity', 'wz_quantity_tree', 'wz_quantity_tree_total']:
            df[col] = df[col].astype(float)
        else:
            df[col] = df[col].astype(str)

    df_x = general_sql.get_table_col('bossard_kanban_staps', ['id'] + list(
        reference_map.sql_col.get('bossard_kanban_staps').keys()))
    df['fk_bossard_kanban_staps'] = df['stadler_id'].apply(lambda x: general_sql.one_step_fk(df_x, 'stadler_id', x))

    df_y = general_sql.get_table_col('ktl_kanban_staps', ['id'] + list(
        reference_map.sql_col.get('ktl_kanban_staps').keys()))
    df['fk_ktl_kanban_staps'] = df['stadler_id'].apply(lambda x: general_sql.one_step_fk(df_y, 'stadler_id', x))

    df_z = general_sql.get_table_col('ktl_kanban_stag', ['id'] + list(
        reference_map.sql_col.get('ktl_kanban_stag').keys()))
    df['fk_ktl_kanban_stag'] = df['stadler_id'].apply(lambda x: general_sql.one_step_fk(df_z, 'stadler_id', x))


    # df = df.convert_dtypes() #remove issues with psycopg2 "can't adapt type 'numpy.int64'"; #error if all columns are na/none type #remove or cast manually column to type
    # DOTO: SQL Szacowany koszt pojazdu na podstawie wszystkich WZ * ceny // czego nie ma na WZ poza pudłami ? 1. NRC 2. Kanban 3. KTL jest zdublowany 4. Groupposition 5?

    # general_sql.drop_table_content(table_name) #usun stare wpisy
    general_sql.insert_into_table(table_name, df, columns)

    general_sql.get_table(table_name)


wz_struktur_staps('4547', 'STAPS')
