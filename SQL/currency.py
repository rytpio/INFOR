import pandas as pd
import general_sql
from dicts_n_lists import sql_import_map
from dicts_n_lists import reference_map

def import_currency_calc():

    table_name = 'currency_data'
    file_path = reference_map.file_path_dicts.get(table_name)
    df = pd.read_excel(file_path)
    df.sort_values(by=[list(sql_import_map.currency_sql_col_dict.keys())[2]], ascending=False, inplace=True)  # date

    # print(df)
    general_sql.create_table(table_name, table_name, sql_import_map.currency_sql_col_dict)

    general_sql.drop_table_content(table_name)
    general_sql.insert_into_table(table_name, df, sql_import_map.currency_sql_col_dict)

    #print(general_sql.get_table(table_name))


import_currency_calc()
