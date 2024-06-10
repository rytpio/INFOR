import pandas as pd
from dicts_n_lists import reference_map
from SQL import general_sql


def cable_quantity(project: str):
    """ cable position quantities for project """
    table_name = 'cable_quantity'
    path = reference_map.file_path_dicts.get(project).get(table_name)
    columns = reference_map.sql_col.get(table_name)

    #general_sql.drop_table(table_name)
    #general_sql.create_table(table_name, table_name, columns)

    df = pd.read_excel(path)
    df.drop_duplicates(subset=['stadler_id'], inplace=True)
    df.dropna(subset=['stadler_id'], inplace=True)
    df = df.convert_dtypes()  # remove issues with psycopg2 "can't adapt type 'numpy.int64'"
    df['project'] = project
    # DOTO: SQL zapytanie pobierające dane tylko 1 producenta
    # DOTO: SQL zestawienie produktów w matlist (rozgraniczyć na podstawie dostawcy H+S, L+S-jak inny to H+S)
    # zamówionych i suma szacowanych

    # general_sql.drop_table_content(table_name) #usun stare wpisy
    general_sql.insert_into_table(table_name, df, columns)

    # general_sql.update_table_fk_one_step('cable_quantity', 'materialliste',
    #                                      list(reference_map.sql_col.get('cable_quantity').keys()),
    #                                      list(reference_map.sql_col.get('materialliste').keys()),
    #                                      'stadler_id', 'mnr', 'fk_cable_quantity','project', 'komm', project)
    #                                      #need project

    # two-step update needed many-to-many relationship; update relationship table;
    # update data table-only for kable data
    # general_sql.update_table_fk_one_step('cable_quantity', 'materialliste',
    # list(reference_map.sql_col.get('materialliste').keys()),
    # list(reference_map.sql_col.get('cable_quantity').keys()),
    # 'stadler_id', 'stadler_id', 'fk_cable_quantity')

    # general_sql.get_table(table_name)


def cable_data():
    """ cable position details"""
    table_name = 'cable_data'
    path = reference_map.file_path_dicts.get(table_name)
    columns = reference_map.sql_col.get(table_name)
    fk_columns = reference_map.sql_fk_col.get(table_name)

    #general_sql.drop_table(table_name)
    #general_sql.create_table(table_name, table_name, columns)  # | fk_columns)

    df = pd.read_excel(path)
    df.drop_duplicates(subset=['stadler_id', 'supplier'],
                       inplace=True)  # TODO: duble, ewentualnie do wylapania i raportu
    df.dropna(subset=['stadler_id'], inplace=True)

    # df_cable = general_sql.get_table_col('cable_quantity',
    #                                      ['id'] + list(reference_map.sql_col.get('cable_quantity').keys()))
    # df['fk_cable_quantity'] = df['stadler_id'](lambda x: general_sql.one_step_fk(df_cable, 'stadler_id', x))

    # general_sql.drop_table_content(table_name) #usun stare wpisy
    general_sql.insert_into_table(table_name, df, columns)

    general_sql.get_table(table_name)


def cable_relationship():
    """ cable joining n-to-n table"""
    table_name = 'cable_relationship'

    columns = reference_map.sql_col.get(table_name)
    fk_columns = reference_map.sql_fk_col.get(table_name)

    general_sql.drop_table(table_name)
    general_sql.create_table(table_name, table_name, columns | fk_columns)

    df_cable_quantity = pd.DataFrame(
        general_sql.get_table_col('cable_quantity', ['id'] + list(reference_map.sql_col.get('cable_quantity').keys())))
    df_cable_data = pd.DataFrame(
        general_sql.get_table_col('cable_data', ['id'] + list(reference_map.sql_col.get('cable_data').keys())))

    df_relationship = pd.DataFrame(columns=columns)
    # for every project_stadler_id row create row supplier_stadler_id
    for q in df_cable_quantity.itertuples():
        df_cable_data_temp = df_cable_data['supplier'][df_cable_data['stadler_id'] == str(q.stadler_id)]
        for d in df_cable_data_temp:
            x = pd.DataFrame({'stadler_id': q.stadler_id, 'project': q.project, 'supplier': d}, index=[0])
            df_relationship = pd.concat([df_relationship, x], ignore_index=True)

    df_relationship['fk_cable_quantity'] = df_relationship.apply(
        lambda row: general_sql.two_step_fk(df_cable_quantity, 'project', 'stadler_id', row.project, row.stadler_id),
        axis=1)
    df_relationship['fk_cable_data'] = df_relationship.apply(
        lambda row: general_sql.two_step_fk(df_cable_data, 'supplier', 'stadler_id', row.supplier, row.stadler_id),
        axis=1)

    # print(df_relationship)

    general_sql.drop_table_content(table_name)  # usun stare wpisy
    general_sql.insert_into_table(table_name, df_relationship, columns)

    general_sql.get_table(table_name)


# for x in ['4382', '4355', '4421', '4423', '4433', '4444', '4468', '4541', '4542', '4547', '4577', '4388']:
#     cable_quantity(x)
cable_quantity('4503')
# cable_relationship()
#cable_data()
