import pandas as pd
from psycopg2 import DatabaseError

import general_sql


def test_for_doubled_rows():
    """
    test if given tables contain double imported position which will result in incorrect query results later
    :return:
    """

    table_dict = {#"avz": ['breadcrumb', 'project', 'stadler_id'],
                   # "avz_knot": ['avz_breadcrumb', 'project'], #raczej pochodne avz dubli - wynik powinien być zbliżony
                   # "avz_mat_knot": ['avz_breadcrumb', 'project'], #raczej pochodne avz dubli - wynik powienien byc zbliżony
                   # "bossard_kanban_staps": ['stadler_id'],
                   # "bossard_price_staps": ['stadler_id'],
                   # "cable_data": ['stadler_id', 'stadler_id_supplier'],  # zastanowić się nad przypadkiem - kilka różnych danych pod stadler_id L+S/H+S/inne zamawiane - scalanie po stronie zakupów
                   # "ktl_kanban_staps": ['stadler_id'],
                   # "ktl_kanban_stag": ['stadler_id'],
                   #"cable_quantity": ['stadler_id', 'project'],
                   # "currency_data": ['currency', 'date'],
                  #"device_list": ['stadler_id', 'schematic_position', 'project', 'car_area'],
                  #"wz": ['stadler_id', 'breadcrumb', 'project'],
                  "material_list": ['stadler_id', 'order_id', 'project', 'fz'],
                  # "material_list_leftover": ['stadler_id', 'order_id', 'project'], #pochodna materialisty i avz
                  }

    conn = general_sql.connect()
    cursor = conn.cursor()

    for table_name in table_dict.keys():
        #table_name = 'cable_data'
        group_list = table_dict.get(table_name)
        counted_col = group_list[0]



        query = f'SELECT DISTINCT COUNT({counted_col})>1 as "double_check", {str.join(", ", group_list)}  FROM {table_name} GROUP BY {str.join(", ", group_list)}'
        try:
            cursor.execute(query)
            conn.commit()
            df = pd.DataFrame(cursor.fetchall(), columns=['double_check', *group_list])
            df = df[df['double_check']]

            if 'project' in group_list:
                query_check = f'SELECT DISTINCT project, COUNT({counted_col}) FROM {table_name} GROUP BY project'
                cursor.execute(query_check)
                conn.commit()
                df_count = pd.DataFrame(cursor.fetchall(), columns=['project', 'row_count'])

                if 'stadler_id' in group_list:
                    dummy_count_col = 'stadler_id'
                elif 'avz_breadcrumb' in group_list:
                    dummy_count_col = 'avz_breadcrumb'
                df_result_count = pd.DataFrame(df.groupby('project')[dummy_count_col].count().reset_index()).set_axis(
                    ['project', 'row_count'], axis=1)
                df_result_count = df_result_count.merge(df_count, how='left', on='project', suffixes=("_double", "_all"))
                if df_result_count.shape[0] >0:
                    df_result_count['err_ratio'] = df_result_count.apply(lambda row: int(row.row_count_double) / int(row.row_count_all), axis=1 )
                    df = df.merge(df_result_count[['project', 'err_ratio']], on='project', how='left')
                else:
                    df_result_count['err_ratio'] = 0

            if df.shape[0] == 0:  # df_shape first axis=0 rows(x), then axis=1, columns (y)
                print(table_name, 'ok')
            else:
                if 'project' in group_list:
                    print("nok na projektach: \n" ,df_result_count['project'][df_result_count['err_ratio'] > 0.1]) #jeśli projekt większy niż 10% dubli to trzeba sprawdzić koniecznie
                else:
                    print(table_name, 'nok')
                df.to_excel(f'C:\\Users\\rytpio\\Desktop\\Projekty bieżące\\DATA\\CHECK\\{table_name}.xlsx', index=False)

        except(Exception, DatabaseError) as error:
            print("Error: %s" % error)


test_for_doubled_rows()
