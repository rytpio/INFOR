import psycopg2

import pandas as pd
import timeit

from dicts_n_lists import reference_map


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


def drop_table_rows(table_name: str, ref_list: list, column: list, column_type: list) -> bool:
    for y in column:
        i = column.index(y)
        bag = ref_list[i]
        if isinstance(bag, list) and len(bag) > 1:
            bag = ref_list[i]
        else:
            bag = [ref_list[i]]

            #TODO: Dodać ten bag gdzieś :D?

        for x in ref_list[column.index(y)]:  # need list otherwise take 1 element and divides into subelements
            column_type_x = column_type[column.index(y)]
            if column_type_x != "":
                column_type_x = f'::{column_type_x}'
            conn = connect()
            cursor = conn.cursor()
            command = f'DELETE FROM {table_name} WHERE {y} = {x}{column_type_x};'
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
    # tuples = [tuple(x) for x in df.to_numpy()]
    # tuples = []
    # for x in df.to_numpy():
    #     tuples.append(tuple(x))
    # tuples = set(tuples)
    # tuples = list(tuples)
    #tuples = list(set([tuple(x) for x in df.to_numpy()])) #usuwa duplikaty :S; w materialliscie wystepuja duplikaty występują duplikaty
    tuples = list([tuple(x) for x in df.to_numpy()])
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


def update_table_fk_one_step(source_table_name: str, target_table_name: str, source_columns: list, target_columns: list,
                             id_source: str, id_target: str, id_fk_col: str, project: str,
                             source_proj_col='project', target_proj_col='project') -> bool:
    conn = connect()
    cursor = conn.cursor()

    if project == '':
        df_source = get_table_col(source_table_name, (['id'] + source_columns))
        df_target = get_table_col(target_table_name, (['id'] + target_columns))
    else:
        df_source = get_table_col_condition(source_table_name, (['id'] + source_columns), source_proj_col, project)
        df_target = get_table_col_condition(target_table_name, (['id'] + target_columns), target_proj_col, project)

    # target_id_list = df_target[id_target].tolist()  # target table with duplicates to keep order
    target_id_list = df_target[id_target].drop_duplicates().tolist()  # target table with duplicates to keep order
    source_id_list = df_source[id_source].drop_duplicates().tolist()  # assumption that source id is unique

    fk_list = []
    id_list = []
    for x in target_id_list:
        if x in source_id_list:
            id_list.append(x)  # lista id where, update
            part_list = (df_source['id'][df_source[id_source] == x]).tolist()
            if len(part_list) < 2:
                fk_list.append(*part_list)  # dla unikatowych wartości 1:n wpisać 1 liczbę
            else:
                fk_list.append(0)  # dla apparatelisty, avz, materiallisty są relacje n:n a więc tylko wpisać '0'
            # lista wartosci fk_id do wpisania z tabeli docelowej
            #  fk_list.extend(df_source['id'][df_source[id_source] == x].tolist()) # list index 0->; sql index 1->
        else:
            pass
            # fk_list.append('Null')

    print(f'Update of {len(fk_list)} positions in {target_table_name}')

    try:
        # reset indexes to NULL
        if project == '':
            query = f"UPDATE {target_table_name} SET {id_fk_col}=NULL"
        else:
            query = f"UPDATE {target_table_name} SET {id_fk_col}=NULL WHERE " \
                    f"{target_table_name}.{target_proj_col}='{project}'"
        cursor.execute(query)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)

    try:
        # set only not null fk keys to values
        for x in range(1, len(fk_list)):
            if project == '':
                query = f"UPDATE {target_table_name} SET {id_fk_col}={fk_list[x - 1]} WHERE " \
                        f"{target_table_name}.{id_target}='{id_list[x - 1]}'"
            else:
                query = f"UPDATE {target_table_name} SET {id_fk_col}={fk_list[x - 1]} WHERE " \
                        f"{target_table_name}.{id_target}='{id_list[x - 1]}' " \
                        f"AND {target_table_name}.{target_proj_col}='{project}'"
            print(f'{x} of {len(fk_list)} positions')

            cursor.execute(query)
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
    return False


def update_fk(target_table: list, source_table: str, target_fk: str, project: str,
              id_source='stadler_id', id_target='stadler_id') -> None:
    """
    :param target_table: data into which id is to be added
    :param source_table: source data from which it is added
    :param target_fk:  targeted columns to add fk_
    :param project: project
    :param id_source: id col of source_list
    :param id_target: id col of target
    :return: None
    """

    for target in target_table:
        update_table_fk_one_step(source_table, target,
                                 list(reference_map.sql_col.get(source_table).keys()),
                                 list(reference_map.sql_col.get(target).keys()),
                                 id_source, id_target, target_fk, project)
        print(f'Finished updating {source_table} fk keys on {target}')


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

    except (Exception, psycopg2.DatabaseError) as error:
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


def get_table_multi_condition(table_name: str, col_list: list, condition_col_list: list,
                              condition_value_list: list) -> pd.DataFrame:
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


def get_query(query: str, col_list: list) -> pd.DataFrame:
    conn = connect()
    cursor = conn.cursor()
    cols = ','.join(list(col_list))
    command_get = query
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


def update_based_on_partial_string(target_table_name:str, set_col:str, category:str, condition_col:str, partial_str:str
                                   ,excluded_str_lst:list, project:str)->None:
    conn = connect()
    cursor = conn.cursor()
    try:
        if len(excluded_str_lst) > 1:
            query_list = str.join("", [f" and not LOWER({target_table_name}.{condition_col}) like '%{x}%'" for x in
                                       excluded_str_lst])
            if project != '':
                query = (f"UPDATE {target_table_name} SET {set_col} = '{category}' "
                         f"WHERE project='{project}' and LOWER({target_table_name}.{condition_col}) like '%{partial_str}%'") + query_list
            else:
                query = (f"UPDATE {target_table_name} SET {set_col} = '{category}' "
                     f"WHERE LOWER({target_table_name}.{condition_col}) like '%{partial_str}%'") + query_list

            # query2 = (f"SELECT * FROM {target_table_name} "
            #          f"WHERE LOWER({target_table_name}.{condition_col}) like '%{partial_str}%'") + query_list
        else:
            if project != '':
                query = (f"UPDATE {target_table_name} SET {set_col} = '{category}' "
                     f"WHERE project='{project}' and LOWER({target_table_name}.{condition_col}) like '%{partial_str}%'")
            else:
                query = (f"UPDATE {target_table_name} SET {set_col} = '{category}' "
                     f"WHERE LOWER({target_table_name}.{condition_col}) like '%{partial_str}%'")

        # cursor.execute(query2)
        # conn.commit()
        # x = cursor.fetchall()

        cursor.execute(query)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)

    return None

def run_query_get(query: str) -> pd.DataFrame:
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        table = pd.DataFrame(cursor.fetchall())
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        return pd.DataFrame()
    conn.close()
    return table

def run_query_set(query: str) -> pd.DataFrame:
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        return pd.DataFrame()
    conn.close()
    return None
