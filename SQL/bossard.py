import pandas as pd
from dicts_n_lists import reference_map
from dicts_n_lists import file_import_map
from SQL import general_sql


def bossard_price_staps():
    """ Tylko cena z numerami SP/STADLER ID """
    table_name = 'bossard_price_staps'
    path = reference_map.file_path_dicts.get(table_name)
    columns = reference_map.sql_col.get(table_name)
    fk_columns = reference_map.sql_fk_col.get(table_name)

    #general_sql.drop_table(table_name)
    #general_sql.create_table(table_name, table_name, columns | fk_columns)

    df = pd.read_excel(path)
    df.drop_duplicates(subset=['stadler_id'], inplace=True)
    df.dropna(subset=['stadler_id'], inplace=True)

    df_bossard_kanban_staps = general_sql.get_table_col('bossard_kanban_staps', ['id'] + list(
        reference_map.sql_col.get('bossard_kanban_staps').keys()))
    df['fk_bossard_kanban_staps'] = df['stadler_id'].apply(
        lambda x: general_sql.one_step_fk(df_bossard_kanban_staps, 'stadler_id', x))

    general_sql.drop_table_content(table_name)  # usun stare wpisy
    general_sql.insert_into_table(table_name, df, columns)

    #general_sql.get_table(table_name)


def bossard_stock_staps():
    table_name = 'bossard_kanban_staps'
    path = reference_map.file_path_dicts.get(table_name)
    columns = reference_map.sql_col.get(table_name)
    short_columns = file_import_map.bossard_short_col_dict

    #general_sql.drop_table(table_name)
    #general_sql.create_table(table_name, table_name, columns)


    #df = pd.read_excel(path)
    #df.to_excel(path, encoding='utf-8')
    df = pd.read_excel(path, header=5, usecols='A:AD',)
    df.columns = [str(x).lower().replace(' ', '_').replace('.', '_') for x in df.columns.tolist()]
    df = df[list(short_columns.keys())]
    df.rename(columns=short_columns, inplace=True)
    df.drop_duplicates(subset=['stadler_id'], inplace=True)
    df.dropna(subset=['stadler_id'], inplace=True)

    general_sql.drop_table_content(table_name)  # usun stare wpisy

    general_sql.insert_into_table(table_name, df, columns)

    #general_sql.get_table(table_name)



#bossard_stock_staps()

#bossard_price_staps()
general_sql.update_fk(['wz', 'device_list', 'material_list','avz', 'wz'],
                      'bossard_kanban_staps','fk_bossard_kanban_staps','')


#wrzuc do listy "update_list" id klucza parent list, w kolumne podana na projekcie x