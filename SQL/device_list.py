import pandas as pd
from dicts_n_lists import reference_map
from dicts_n_lists import file_import_map
from SQL import general_sql
import re

def device_list(project: str):
    """"""
    table_name = 'device_list'
    path = reference_map.file_path_dicts.get(project).get(table_name)
    columns = reference_map.sql_col.get(table_name)
    fk_columns = reference_map.sql_fk_col.get(table_name)
    col_change_dict = file_import_map.device_dict_project.get(project).get('col_change_dict')
    col_complete_list = file_import_map.device_dict_project.get(project).get('col_complete_list')
    col_cutout_list = file_import_map.device_dict_project.get(project).get('col_cutout_list')


    translate_dict = {'.': '_',
                      '/': '_',
                      ' ': '_',
                      '-': '_'
                      }

    #general_sql.drop_table_cascade(table_name)
    #general_sql.create_table(table_name, table_name, columns | fk_columns)

    df = pd.read_excel(path, sheet_name='ap')
    df.columns = ([x.lower().translate(x.maketrans(translate_dict)).
                   replace('\n', '_').
                   replace('___', '_').replace('__', '_').
                   replace('ä', 'a') for x in df.columns.tolist()])

    df = df[col_cutout_list]

    df.rename(columns=col_change_dict, inplace=True)
    sum_col_list = [x for x in df.columns if 'stk_' in x[:4]]
    df['stk_sum'] = df[sum_col_list].sum(axis=1)
    for col in col_complete_list:
        if col not in df.columns:
            sql_col_type = reference_map.sql_col[table_name].get(col)
            if sql_col_type.upper() == 'FLOAT':
                df[col] = 0.0
            elif sql_col_type.upper() == 'INTEGER' or 'BIGINT':
                df[col] = 0
            else:
                df[col] = ''

    df['project'] = project

    df_bossard_prc = general_sql.get_table_col('bossard_price_staps',
                                               ['id'] + list(reference_map.sql_col.get('bossard_price_staps').keys()))
    df_bossard_kanban_staps = general_sql.get_table_col('bossard_kanban_staps', ['id'] + list(
        reference_map.sql_col.get('bossard_kanban_staps').keys()))
    df_ktl_kanban_staps = general_sql.get_table_col('ktl_kanban_staps',
                                                    ['id'] + list(reference_map.sql_col.get('ktl_kanban_staps').keys()))
    df_ktl_kanban_stag = general_sql.get_table_col('ktl_kanban_stag',
                                                   ['id'] + list(reference_map.sql_col.get('ktl_kanban_stag').keys()))

    df['fk_bossard_prc'] = df['stadler_id'].apply(lambda x: general_sql.one_step_fk(df_bossard_prc, 'stadler_id', x))
    df['fk_bossard_kanban_staps'] = df['stadler_id'].apply(
        lambda x: general_sql.one_step_fk(df_bossard_kanban_staps, 'stadler_id', x))
    df['fk_ktl_kanban_staps'] = df['stadler_id'].apply(lambda x:
                                                       general_sql.one_step_fk(df_ktl_kanban_staps, 'stadler_id', x))
    df['fk_ktl_kanban_stag'] = df['stadler_id'].apply(lambda x:
                                                      general_sql.one_step_fk(df_ktl_kanban_stag, 'stadler_id', x))
    df['fk_wz'] = None
    df['fk_material_list'] = None
    # DOTO: SQL Zestawienie danych z listy aparatów z komponentami, cenami
    # DOTO: SQL Zestawienie KTL/Kanban zawierających się w liscie aparatów

    # kontrola długosci poszczególnych VARCHAR
    # df_len = df.applymap (lambda x: 'NOTOK' if len(str(x)) > 255 else 'OK')
    # df_len.to_excel(r'C:\Users\rytpio\Desktop\Projekty bieżące\APPARATELISTE\apcheck.xlsx',index=False)
    df = df.applymap(lambda x: x[:254] if len(str(x)) > 255 else x)  # zetnij do 255 znaków
    #df['stadler_id'] = df['stadler_id'].apply(lambda x: str(x).replace("_x000D_", ""))
    df['stadler_id'] = df['stadler_id'].apply(lambda x: re.match(r"^ *\d[\d ]*$", str(x)).group(0))

    general_sql.drop_table_rows(table_name,[[project]],['project'], column_type=['varchar'])  # usun stare wpisy

    # for col in columns.keys():
    #     col_val = str(columns.get(col))
    #     if col_val.find("(")>0:
    #         col_len = int(col_val[col_val.find('(')+1:col_val.rfind(')')])
    #         df[col] = df[col].apply(lambda x: x[:col_len] if len(str(x)) > col_len else x)

    general_sql.insert_into_table(table_name, df, columns)


    #general_sql.get_table(table_name, True)

project = '4556'
device_list(project)
