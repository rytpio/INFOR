from dicts_n_lists import sql_import_map
import general_sql
import pandas as pd


def avz_knot(project: str, file_path: str) -> None:
    table_name = 'avz_knot'

    sheets = pd.ExcelFile(file_path).sheet_names
    df = pd.read_excel(file_path, sheet_name=sheets[1])
    df['project'] = project

    # general_sql.drop_table(table_name)
    # general_sql.create_table(table_name, table_name, sql_col_dicts.avz_knot_sql_col_dict)
    general_sql.drop_table_content(table_name)  # usun stare wpisy
    general_sql.insert_into_table(table_name, df, sql_import_map.avz_knot_sql_col_dict)

    # print(general_sql.get_table(table_name))


path = r'C:\Users\rytpio\Desktop\Projekty bieżące\AVZ\4503_AVZ_knots.xlsx'
avz_knot('4503', path)
