import psycopg2
import pandas as pd
import timeit


def two_step_fk(df_source: pd.DataFrame, searched1: str, searched2: str, var1: str, var2: str):
    x = df_source['id'][(df_source[searched1] == str(var1)) & (df_source[searched2] == str(var2))].tolist()
    # założenie, że jest tylko 1 numer stadler id w projekcie; nie ma dubli
    if len(x) == 1:
        return str(*x)
    elif len(x) > 1:
        print(len(x), str(x))
        return None
    else:
        return None


def one_step_fk(df: pd.DataFrame, searched1: str, var1: str):
    x = df['id'][df[searched1] == str(var1)].tolist()
    if len(x) == 1:
        return str(*x)
    elif len(x) > 1:
        print(len(x), str(x))
        return None
    else:
        return None


def connect():
    conn = psycopg2.connect(
        database="MY_TEST", user='admin', password='', host='localhost', port='5432'
    )
    return conn


def drop_table(table_name: str) -> bool:
    conn = connect()
    cursor = conn.cursor()
    command = f'DROP TABLE {table_name};'
    try:
        cursor.execute(command)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        return False
    conn.close()
    return True


def drop_table_cascade(table_name: str) -> bool:
    conn = connect()
    cursor = conn.cursor()
    command = f'DROP TABLE {table_name} CASCADE;'
    try:
        cursor.execute(command)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        return False
    conn.close()
    return True


def drop_table_content(table_name: str) -> bool:
    conn = connect()
    cursor = conn.cursor()

    command = f'DELETE FROM {table_name};'
    try:
        cursor.execute(command)
        # print(cursor.rowcount)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        conn.rollback()
        return False

    conn.close()

    return True


def drop_table_rows(table_name: str, ref_list: list, column: str) -> bool:
    conn = connect()
    cursor = conn.cursor()

    for x in ref_list:
        command = f'DELETE FROM {table_name} WHERE {column} = {x}::varchar;'
        try:
            cursor.execute(command)
            # print(cursor.rowcount)
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Error: %s' % error)
            conn.rollback()
            return False

    conn.close()

    return True


def create_table(table_name: str, id_name: str, col_dict: dict) -> bool:
    conn = connect()
    cursor = conn.cursor()

    command = f'CREATE TABLE {table_name} ({id_name} SERIAL PRIMARY KEY,'
    for col in col_dict:
        command += f'{col} {col_dict.get(col)},'
    command = command[:-1] + ');'
    try:
        cursor.execute(command)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        return False
    conn.close()
    print(f'created table {table_name}')

    return True


def insert_into_table(table_name: str, df: pd.DataFrame, columns: dict) -> bool:
    conn = connect()
    cursor = conn.cursor()

    df = df[columns.keys()]
    #tuples = [tuple(x) for x in df.to_numpy()]
    # tuples = []
    # for x in df.to_numpy():
    #     tuples.append(tuple(x))
    # tuples = set(tuples)
    # tuples = list(tuples)
    tuples = list(set([tuple(x) for x in df.to_numpy()]))
    cols = ','.join(list(df.columns))
    query = f'INSERT INTO {table_name}({cols}) VALUES ({",".join(["%s"] * len(df.columns))})'

    try:
        cursor.executemany(query, tuples)
        # cursor.execute(query, tuples[0])
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        conn.rollback()
        return False

    conn.close()
    print(f'inserted into table {table_name} data.')
    return True


def update_table_fk_one_step(parent_table_name: str, child_table_name: str, parent_columns: list, child_columns: list,
                             id_parent: str, id_child: str, id_fk_col: str,
                             parent_proj_col='project', child_proj_col='project', project='') -> bool:
    conn = connect()
    cursor = conn.cursor()

    if project == '':
        df_parent = get_table_col(parent_table_name, (['id'] + parent_columns))
        df_child = get_table_col(child_table_name, (['id'] + child_columns))
    else:
        df_parent = get_table_col_condition(parent_table_name, (['id'] + parent_columns), parent_proj_col, project)
        df_child = get_table_col_condition(child_table_name, (['id'] + child_columns), child_proj_col, project)

    child_id_list = df_child[id_child].tolist()  # child table with duplicates to keep order
    parent_id_list = df_parent[id_parent].drop_duplicates().tolist()  # assumption that parent id is unique

    fk_list = []
    for x in child_id_list:
        if x in parent_id_list:
            # print(df_parent['id'][df_parent[id_parent] == id])
            # print(*df_parent['id'][df_parent[id_parent] == id])
            fk_list.append(*df_parent['id'][df_parent[id_parent] == x])  # list index 0->; sql index 1->
        else:
            fk_list.append('Null')

    try:
        # cursor.executemany(query, fk_list)
        for x in range(1, len(fk_list)):
            if project == '':
                query = f"UPDATE {child_table_name} SET {id_fk_col}={fk_list[x - 1]} WHERE " \
                        f"{child_table_name}.{id_child}='{child_id_list[x - 1]}'"
            else:
                query = f"UPDATE {child_table_name} SET {id_fk_col}={fk_list[x - 1]} WHERE " \
                        f"{child_table_name}.{id_child}='{child_id_list[x - 1]}' " \
                        f"AND {child_table_name}.{child_proj_col}='{project}'"
            print(f'{x} of {len(fk_list)} positions')  # strasznie wolno działa; 5 pozycji na sekunde; jakies 3h

            cursor.execute(query)
            conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
    return False


def insert_into_table_new_one_step(table_name: str, df: pd.DataFrame, columns: list, id_col: str,
                                   id_col_source: str) -> bool:
    conn = connect()
    cursor = conn.cursor()

    cols = ['id'] + columns
    df_source = get_table_col(table_name, cols)
    # df_source = df_source[df_source[id_col_source].apply(lambda x: isinstance(x, (int, np.int64)))]
    id_list = df_source[id_col_source].drop_duplicates().tolist()

    __l = df.columns.tolist()  # dodaj tylko pozycje, których już nie ma w liście
    col_nr = __l.index(id_col_source)
    for row in df.itertuples():
        if str(row[col_nr + 1]) in id_list:
            df.drop(row[0], axis='index', inplace=True)

    # df = df[columns.keys()]
    tuples = list(set([tuple(x) for x in df.to_numpy()]))
    cols = ','.join(columns)
    query = f'INSERT INTO {table_name}({cols}) VALUES ({",".join(["%s"] * len(df.columns))})'

    try:
        cursor.executemany(query, tuples)
        # cursor.execute(query, tuples[0])
        conn.commit()

    except(Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        conn.rollback()
        return False

    conn.close()
    print(f'inserted into table {table_name} new data')


def get_table_col(table_name: str, col_list: list) -> pd.DataFrame:
    conn = connect()
    cursor = conn.cursor()
    command_get = f'SELECT * FROM {table_name};'
    try:
        cursor.execute(command_get)
        conn.commit()
        table = pd.DataFrame(cursor.fetchall(), columns=col_list)
        # table = pd.read_sql(f'SELECT * FROM {table_name};', conn)
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        return pd.DataFrame()
    conn.close()
    return table
    # print(table)


def get_table_col_condition(table_name: str, col_list: list, condition_col: str, condition_value: str) -> pd.DataFrame:
    conn = connect()
    cursor = conn.cursor()
    command_get = f'SELECT * FROM {table_name} WHERE {table_name}.{condition_col}={condition_value}::varchar;'
    try:
        cursor.execute(command_get)
        conn.commit()
        table = pd.DataFrame(cursor.fetchall(), columns=col_list)
        # table = pd.read_sql(f'SELECT * FROM {table_name};', conn)
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        return pd.DataFrame()
    conn.close()
    return table


def get_table(table_name: str, show_time: bool = False) -> pd.DataFrame:
    start = timeit.default_timer()
    conn = connect()
    time = ['conn ' + str(timeit.default_timer() - start)]
    cursor = conn.cursor()
    command_get = f'SELECT * FROM {table_name};'
    time.append('cursor ' + str(timeit.default_timer() - start))
    try:
        cursor.execute(command_get)
        time.append('execute ' + str(timeit.default_timer() - start))
        conn.commit()
        time.append('commit ' + str(timeit.default_timer() - start))
        table = pd.DataFrame(cursor.fetchall())
        time.append('table ' + str(timeit.default_timer() - start))
        # table = pd.read_sql(f'SELECT * FROM {table_name};', conn)
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        return pd.DataFrame()
    conn.close()
    if not show_time:
        print(str(time).join('\n'))
    return table
    # print(table)


def get_table_condition(table_name: str, col_list: list, condition_col: str, condition_value: str) -> pd.DataFrame:
    conn = connect()
    cursor = conn.cursor()
    command_get = f'SELECT * FROM {table_name} WHERE {table_name}.{condition_col}={condition_value}::varchar;'
    try:
        cursor.execute(command_get)
        conn.commit()
        table = pd.DataFrame(cursor.fetchall(), columns=col_list)
        # table = pd.read_sql(f'SELECT * FROM {table_name};', conn)
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        return pd.DataFrame()
    conn.close()
    return table


def get_table_multi_condition(table_name: str, col_list: list, condition_col_list: str,
                              condition_value_list: str) -> pd.DataFrame:
    conn = connect()
    cursor = conn.cursor()
    if len(condition_col_list) == len(condition_value_list):
        condition_list = []
        for i in range(0, len(condition_value_list)):
            condition_list.append(f'{table_name}.{condition_col_list[i]}={condition_value_list[i]}::varchar')
        condition = ' and '.join(condition_list)
        command_get = f'SELECT * FROM {table_name} WHERE {condition};'

        try:
            cursor.execute(command_get)
            conn.commit()
            table = pd.DataFrame(cursor.fetchall(), columns=col_list)
            # table = pd.read_sql(f'SELECT * FROM {table_name};', conn)
        except (Exception, psycopg2.DatabaseError) as error:
            print('Error: %s' % error)
            return pd.DataFrame()

    else:
        print(f'Listy kolumn i wartości są różnej długości')
        table = pd.DataFrame()

    conn.close()
    return table


# 'get_dataset('apparateliste', col_list: list, condition_col: str, condition_value: str)'
# 'apparateliste_col_list =
# [bg,din,main_group,secondary_group, description, description_2, type, supplier_id, supplier, stadler_id]'
def get_dataset(table_name: str, col_list: list) -> pd.DataFrame:
    conn = connect()
    cursor = conn.cursor()
    cols = ",".join(list(col_list))
    command_get = f'SELECT {cols} FROM {table_name};'
    try:
        cursor.execute(command_get)
        conn.commit()
        table = pd.DataFrame(cursor.fetchall(), columns=col_list)
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        return pd.DataFrame()
    conn.close()
    return table

    # # #Add fk key
    # table_name_src = 'infor_matlist'
    # column_name = 'project_stadler_id' #'mnr'
    # reference_table_name = 'ktl_STAPS'
    # reference_column_name = 'project_stadler_id'
    # fk_column_name = 'fk_ktl_STAPS'
    # command_add_fk = f'ALTER TABLE {table_name_src}
    # ADD CONSTRAINT NULL {fk_column_name} FOREIGN KEY({column_name})
    # REFERENCES {reference_table_name}({reference_column_name})
    # ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;'
    # cursor.execute(command_add_fk)
    # conn.commit()

    # create id
    # adding an extra column
    # table_name_src ='infor_matlist' #'ktl_STAPS' #
    # column_name = 'project_stadler_id'
    # column_name1 = 'komm'#'auftrag' #
    # column_name2 = 'mnr' ##'stadler_id'
    # command_create_column = f'''ALTER TABLE {table_name_src} ADD COLUMN {column_name} VARCHAR(255) NULL;'''#UNIQUE
    # command_update_column = f'''UPDATE {table_name_src} SET
    # {column_name} = CONCAT({column_name1},'_', {column_name2});'''
    # cursor.execute(command_create_column)
    # cursor.execute(command_update_column)
    # conn.commit()

    # #drop column
    # table_name_src = 'infor_matlist'# 'ktl_STAPS'
    # column_name = 'project_stadler_id'
    # command_drop_column = f'''ALTER TABLE {table_name_src} DROP COLUMN {column_name};'''
    # cursor.execute(command_drop_column)
    # conn.commit()
