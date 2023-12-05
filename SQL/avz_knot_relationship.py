import pandas as pd
from dicts_n_lists import reference_map
from SQL import general_sql


def avz_knot_relationship(project: str) -> None:
    """  """
    table_name = 'avz_knot_relationship'

    columns = reference_map.sql_col.get(table_name)
    fk_columns = reference_map.sql_fk_col.get(table_name)

    # general_sql.drop_table(table_name)
    general_sql.create_table(table_name, table_name, columns | fk_columns)

    df_avz_knot = pd.DataFrame(
        general_sql.get_table_condition('avz_knot', ['fk'] + list(reference_map.sql_col.get('avz_knot').keys()),
                                        'project', project), dtype=str)

    df_avz = pd.DataFrame(
        general_sql.get_table_condition('avz', ['fk'] + list(reference_map.sql_col.get('avz').keys()), 'project',
                                        project), dtype=str)
    df_avz = df_avz[['fk', 'project', 'stadler_id']]

    df = pd.merge(left=df_avz_knot, right=df_avz, how='inner',
                  left_on=['project', 'stadler_id'], right_on=['project', 'stadler_id'],
                  validate="one_to_many")
    df.drop(labels=['project'], axis=1, inplace=True)
    # df['fk_materialliste]'.astype(dtype=int)
    # df.to_csv(r'C:\Users\rytpio\Desktop\Projekty bieżące\AVZ\dumpX.csv')
    # print(df)

    general_sql.insert_into_table(table_name, df, columns)
    # avz update klucza fk_avz_knot
    # print(general_sql.get_table(table_name))


avz_knot_relationship('4473')
