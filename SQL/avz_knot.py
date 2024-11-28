from dicts_n_lists import sql_import_map
from dicts_n_lists import reference_map
import general_sql
import pandas as pd


def avz_knot(project: str) -> None:
    table_name = 'avz_knot'
    file_path = reference_map.file_path_dicts.get(project).get(table_name)

    # sheets = pd.ExcelFile(file_path).sheet_names
    df = pd.read_excel(file_path, sheet_name='knot',na_filter=False)
    df['project'] = project
    df['fk_avz'] = None

    #general_sql.drop_table(table_name)
    #general_sql.create_table(table_name, table_name, sql_import_map.avz_knot_sql_col_dict)
    #TODO: Test kompletności po wgraniu w SQL
    general_sql.drop_table_rows(table_name, [[project]], ['project'], column_type=['varchar'])  # usun stare wpisy
    general_sql.insert_into_table(table_name, df, sql_import_map.avz_knot_sql_col_dict)

    #print(general_sql.get_table(table_name))


project = '4444'
avz_knot(project)
#Relacje ustalane w PBI więc nie ma potrzeby tutaj chwilowo aktualizować.
# general_sql.update_fk(['avz_knot'], 'avz', 'fk_avz', project, 'breadcrumb',
#                       'avz_breadcrumb') ## jeśli breadcrumb się pokrywa to nie ma sensu; chyba że fk_key
