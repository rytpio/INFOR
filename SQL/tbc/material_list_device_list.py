import pandas as pd
from dicts_n_lists import reference_map
from SQL import general_sql


def material_list_device_list_relationship(project: str):
    """  """
    table_name = 'material_list_device_list_relationship'

    columns = reference_map.sql_col.get(table_name)
    fk_columns = reference_map.sql_fk_col.get(table_name)

    # general_sql.drop_table(table_name)
    # general_sql.create_table(table_name, table_name, columns | fk_columns)

    df_apparateliste = pd.DataFrame(general_sql.get_table_condition('device_list', ['fk'] +
                                                                    (reference_map.sql_col.get('device_list').keys()),
                                                                    'project', project), dtype=str)
    df_apparateliste = df_apparateliste[['fk', 'project', 'stadler_id']]

    df_matlist = pd.DataFrame(general_sql.get_table_condition('material_list', ['fk'] +
                                                              list(reference_map.sql_col.get('materialliste').keys()),
                                                              'project', project), dtype=str)
    df_matlist = df_matlist[['fk', 'project', 'stadler_id']]

    df = pd.merge(left=df_apparateliste, right=df_matlist, how='inner',
                  left_on=['project', 'stadler_id'], right_on=['project', 'stadler_id'],
                  suffixes=['_device_list', '_material_list'], validate="many_to_many")  # mnoży zamiast dodawac
    df.drop(labels=['stadler_id', 'project'], axis=1, inplace=True)

    df.to_csv(r'C:\Users\rytpio\Desktop\Projekty bieżące\APPARATELISTE\dumpX.csv')

    # print(df)
    general_sql.insert_into_table(table_name, df, columns)

    general_sql.get_table(table_name)


material_list_device_list_relationship('4473')

# Zestaw stadler_id z WZ z stadler_id Matlist
# stadler_id - fk(wz(n)->stadler(id), matlist(n)->stadler_id(1))
# Wszystkie WZ ID - odrazu fk_key do których należą
# Wszystkie MATLIST ID - odrazu fk_key do których należą
# Tylko pokrywające się dla każdego WZ które jest w matlist ID
# Explode by fk_wz i matlist_id
# Wynik: tabela połączeń pomiędzy wz a matlist #grupy i inne muszą być za pomocą zapytań SQL
# -- stworzyć listę zapytań SQL
# DOTO: SQL Wszystkie nazwy WZ które są w matlist; do sprawdzenia czy materiał schodzi na obecnych wz;
# pomyśleć jak drobny materiał na kilku WZ rozgraniczyć
# DOTO: SQL Wszystkie ilości stadlerID z WZ na pojazd; do szacowania ilości w matlist na pojazd

#
# df_relationship = pd.DataFrame(columns=columns)
# #for every project_stadler_id row create row supplier_stadler_id
# for q in df_kabel_quantity.itertuples():
#     df_kabel_data_temp = df_kabel_data['supplier'][df_kabel_data['stadler_id'] == str(q.stadler_id)]
#     for d in df_kabel_data_temp:
#         x = pd.DataFrame({'stadler_id': q.stadler_id, 'project': q.project, 'supplier': d}, index=[0])
#         df_relationship = pd.concat([df_relationship, x], ignore_index=True)
#
#
# df_relationship['fk_kabel_quantity'] = df_relationship.apply(lambda row:
# two_step_fk(df_kabel_quantity, 'project', 'stadler_id', row.project, row.stadler_id), axis=1)
# df_relationship['fk_kabel_data'] = df_relationship.apply(
#     lambda row: two_step_fk(df_kabel_data, 'supplier', 'stadler_id', row.supplier, row.stadler_id), axis=1)
#
# #print(df_relationship)
#
# general_sql.drop_table_content(table_name) #usun stare wpisy
# general_sql.insert_into_table(table_name, df_relationship, columns)
#
# general_sql.get_table(table_name)
