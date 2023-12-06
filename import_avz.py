import pandas as pd
from dicts_n_lists import file_import_map
from math import prod


def clear_din(x: str):
    x = x.strip()

    if x and x[0] != '_':
        din = x[:1] + x[2:3]
        din_txt = x[4:]
    else:
        din = '_'
        # TODO: Zwraca nn domyślnie dla pustych x pomimo ze fkcja zwraca pusty string;
        #  #gdzies w lambda albo replace albo extend leży problem
        if not x:
            din_txt = 'not_assigned'
        else:
            din_txt = x

    return din, din_txt


def assign_category_bu_1951939(x: int) -> str:
    """  co drugi #jesli w range to len(key)-2 """
    range_list = list(file_import_map.avz_pos_ranges.values())
    key_list = list(file_import_map.avz_pos_ranges.keys())
    y = None
    for value_range in range(1, len(range_list), 2):
        if x in range(range_list[value_range - 1], range_list[value_range] + 1):
            y = key_list[value_range][:-2]
            break
        else:
            y = 'unassigned'

    return y


def lvl_headers(df: pd.DataFrame) -> [list, list, list, list]:
    lvl_1 = []
    lvl_2 = []
    lvl_3 = []
    lvl_4 = []
    lvl1 = lvl2 = lvl3 = lvl4 = None
    for lvl in df.itertuples():
        if int(lvl.level) == 0:
            lvl1 = lvl2 = lvl3 = lvl4 = None
        if int(lvl.level) == 1:
            lvl1 = lvl.description_1
            lvl2 = lvl3 = lvl4 = None
        if int(lvl.level) == 2:
            lvl2 = lvl.description_1
            lvl3 = lvl4 = None
        if int(lvl.level) == 3:
            lvl3 = lvl.description_1
            lvl4 = None
        if int(lvl.level) == 4:
            lvl4 = lvl.description_1
        lvl_1.append(lvl1)
        lvl_2.append(lvl2)
        lvl_3.append(lvl3)
        lvl_4.append(lvl4)
    return lvl_1, lvl_2, lvl_3, lvl_4


def import_avz_data(path_read: str, path_save: str) -> pd.DataFrame:
    """
    Scal pobrane AVZ w jeden plik
    :return:
    """

    df = pd.DataFrame()

    # for file in os.listdir(path_read):
    #     if file[-4:] == '.csv':
    #         csv = pd.read_csv(os.path.join(path_read, file), encoding='ISO-8859-2', low_memory=False, sep=';',
    #                           skip_blank_lines=True)
    #         df = pd.concat(objs=[df, csv], axis=0, ignore_index=True, copy=True)
    df = pd.read_csv(path_read, encoding='ISO-8859-2', low_memory=False, sep=';', skip_blank_lines=True)

    df = df.rename(columns=file_import_map.avz_col_dict)
    df = df[file_import_map.avz_col_short_list]

    df[['din', 'din_txt']] = df.apply(lambda x: clear_din(str(x.din)), axis=1, result_type='expand')
    df.replace(r'\r+|\n+|\t+', '', regex=True, inplace=True)
    df['position_number'] = df['position_number'].fillna(0)
    df['pos_nr_category_bu_1951939'] = df['position_number'].apply(lambda x: assign_category_bu_1951939(x))
    df['quantity'] = df['quantity'].fillna(0)  # TODO: Get and inform on empty values
    df['weight'] = df['weight'].fillna(0)

    df.astype(file_import_map.avz_col_type_dict, copy=True)
    df.sort_values(by=['root_article', 'avz_struct_index', 'level', 'position_number'], inplace=True)

    breadcrumb_list = []
    breadcrumb = ''
    din_list = []
    din_txt_list = []
    din = ''
    din_txt = ''
    for row in df.iterrows():
        if str(row[1]['din']) != 'nn':
            din = str(row[1]['din'])
            din_txt = str(row[1]['din_txt'])
            din_list.append(din)
            din_txt_list.append(din_txt)
        else:
            din_list.append(din)
            din_txt_list.append(din_txt)
        stk_id = str(row[1]['stadler_id'])
        level = row[1]['level']
        if level == 0:
            breadcrumb = [stk_id]
        else:
            breadcrumb = breadcrumb[:level]
            breadcrumb.append(stk_id)
        breadcrumb_list.append('/'.join(breadcrumb))
    df['din'] = din_list
    df['din_txt'] = din_txt_list
    df['breadcrumb'] = breadcrumb_list

    lvl_1, lvl_2, lvl_3, lvl_4 = lvl_headers(df[['level', 'description_1']])

    df['lvl1'] = lvl_1
    df['lvl2'] = lvl_2
    df['lvl3'] = lvl_3
    df['lvl4'] = lvl_4

    multiplier_list = []
    quantity_list = []

    for row in df.itertuples():
        lvl = int(row.level)
        quantity = 0
        if lvl == 0:  # menge 0
            quantity = 1
            multiplier_list = [1]
        elif lvl == len(multiplier_list):  # same level = same multiplier; add in case next position is higher level
            multiplier_list = multiplier_list[:lvl - 1]
            quantity = float(row.quantity) * prod(multiplier_list)
            multiplier_list.append(float(row.quantity))
        elif lvl > len(multiplier_list):  # higher level = higher multiplier;
            quantity = float(row.quantity) * prod(multiplier_list)
            multiplier_list.append(float(row.quantity))
        elif lvl < len(multiplier_list):  # lower level = lower multiplier; 5-6-4
            multiplier_list = multiplier_list[:lvl - 1]
            quantity = float(row.quantity) * prod(multiplier_list)
            multiplier_list.append(float(row.quantity))

        quantity_list.append(quantity)

    df['avz_quantity_in_tree'] = quantity_list

    # case 1; len=1 = multiply and add in case of lower level
    # case 2; len=2 = multiply and add in case of lower level ' if higher
    # case 2; len=3 = reverse to len=2; multiply and add in case of lower level 'if lower and if next
    # case 3; len=3 = multiply and add in case of lower level 'same level
    # case 1; len=4 = reverse to len=1; multiply and add in case of lower level

    # TODO: add structure check if level doesn't skip; 4-5-7;
    #  need to be ascending by one with cuts; can be descending in whatever form

    df.to_excel(path_save, index=False)

    return df

