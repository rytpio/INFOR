import pandas as pd
from dicts_n_lists import reference_map
from SQL import general_sql
import import_avz


def avz(project: str) -> None:
    '''
    opens raw, process and save as processed, import to sql
    :param project:
    :return:
    '''
    table_name = 'avz'
    columns = reference_map.sql_col.get(table_name)
    fk_columns = reference_map.sql_fk_col.get(table_name)
    path_read = reference_map.file_path_dicts.get(project).get('avz_raw')
    path_save = reference_map.file_path_dicts.get(project).get('avz_processed')

    # general_sql.drop_table_cascade(table_name)
    # general_sql.create_table(table_name, table_name, columns | fk_columns)

    df = import_avz.import_avz_data(path_read, path_save)

    df['project'] = project
    df_x = general_sql.get_table_col('bossard_kanban_staps',
                                     ['id'] + list(reference_map.sql_col.get('bossard_kanban_staps').keys()))
    df['fk_bossard_kanban_staps'] = df['stadler_id'].apply(lambda x: general_sql.one_step_fk(df_x, 'stadler_id', x))

    df_y = general_sql.get_table_col('ktl_kanban_staps',
                                     ['id'] + list(reference_map.sql_col.get('ktl_kanban_staps').keys()))
    df['fk_ktl_kanban_staps'] = df['stadler_id'].apply(lambda x: general_sql.one_step_fk(df_y, 'stadler_id', x))

    df_z = general_sql.get_table_col('ktl_kanban_stag',
                                     ['id'] + list(reference_map.sql_col.get('ktl_kanban_stag').keys()))
    df['fk_ktl_kanban_stag'] = df['stadler_id'].apply(lambda x: general_sql.one_step_fk(df_z, 'stadler_id', x))

    df = df.applymap(lambda x: x[:255] if len(str(x)) > 255 else x)  # zetnij do 255 znaków
    # general_sql.drop_table_content(table_name) #usun stare wpisy
    general_sql.insert_into_table(table_name, df, columns)

    # general_sql.get_table(table_name)

avz('4547')

# Milesteine1 - Wgranie wszystkiego do SQL !ok
# Milesteine2 - Proste zrzuty jako widoki dla backend !ok
# Milesteine3 - Zrzut materiału-testy!ok
# Milesteine4 - wyjątki i obsługa (grouppositions etc.) !!!!
# Milesteine5 - Ilości i porównywanie !!!
# Milesteine6 - Wgrywanie innych projektów !!
# Milesteine7 - Testy funkcji i refactor kodu !ok
# Milesteine8 - Wrzucenie interfejsu graficznego 0
# Milesteine9 - Postawienie na serwerze 0
# Milesteine10 - Migracja na serwer 0
# Mielsteine11 - opcjonalnie poziomy dostępu 0
