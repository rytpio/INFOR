import pandas as pd
from dicts_n_lists import reference_map
from dicts_n_lists import file_import_map
import general_sql


def material_leftover(project: str):
    """

    :return:
    """
    table_name = 'material_list_leftover'
    path = reference_map.file_path_dicts.get(project).get(table_name)
    columns = reference_map.sql_col.get(table_name)
    #fk_columns = reference_map.sql_fk_col.get(table_name)

    #general_sql.drop_table_cascade(table_name)
    #general_sql.create_table(table_name, table_name, columns)

    df = pd.read_excel(path)
    df = df[['bg_set', 'should_be_included', 'group_mask', 'order_id', 'stadler_id', 'leftover_Acomp']]

    df = df.applymap(lambda x: x[:254] if len(str(x)) > 255 else x)  # zetnij do 255 znaków
    #TODO: Logowanie zcietych znaków
    df['project'] = project

    general_sql.drop_table_rows(table_name, [[project]], ['project'], column_type=['varchar'])  # usun stare wpisy
    general_sql.insert_into_table(table_name, df, columns)


material_leftover('4444')
