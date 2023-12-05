import pandas as pd
from dicts_n_lists import reference_map
from SQL import general_sql


def ktl_kanban_stag():
    """Tylko typ z numerami SP/STADLER ID"""
    table_name = 'ktl_kanban_stag'
    path = reference_map.file_path_dicts.get(table_name)
    columns = reference_map.sql_col.get(table_name)

    general_sql.drop_table(table_name)
    general_sql.create_table(table_name, table_name, columns)

    df = pd.read_excel(path)
    df.drop_duplicates(subset=['stadler_id'], inplace=True)  # DOTO: duble, ewentualnie do wylapania i raportu
    df.dropna(subset=['stadler_id'], inplace=True)
    general_sql.drop_table_content(table_name)  # usun stare wpisy
    general_sql.insert_into_table(table_name, df, columns)

    # general_sql.get_table(table_name)


ktl_kanban_stag()
