from dicts_n_lists import sql_import_map
import general_sql


def avz_mat_knot() -> None:
    table_name = 'avz_mat_knot'

    # general_sql.drop_table(table_name)
    general_sql.create_table(table_name, table_name, sql_import_map.avz_mat_knot_sql_col_dict)


avz_mat_knot()
