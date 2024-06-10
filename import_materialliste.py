import datetime
import os.path
import pandas as pd
from math import floor as rounddown
from dicts_n_lists import file_import_map
from dicts_n_lists import ref_lists
from dicts_n_lists import reference_map

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def only_used_rows_n_cols(df:pd.DataFrame)->[int,list]:
    """ Searchers 100 first df headers and returns first used row and used columns name list of those row
    Assumes that 1st row is a column name row"""
    i = 0
    for row in df.itertuples():
        i += 1
        if str(row[5]).upper() not in ['<NA>', 'NAN']:
            break

    file_col_list = []
    if (i - 1) > 0:
        for column in df.iloc[i - 1]:
            if str(column).upper() not in ['<NA>', 'NAN']:
                file_col_list.append(column)
    else:
        for column in df.columns:
            if str(column).upper() not in ['<NA>', 'NAN']:
                file_col_list.append(column)

    return i, file_col_list

def nrc_sieve(ktxt, fzvon) -> str:
    nrc_ktxt_list = ref_lists.material_list_nrc_ktxt

    func_list_in_str = lambda text, list_: any(filter(lambda x: x in text, list_))
    if str(fzvon) == '0':
        return "NRC"
    elif func_list_in_str(str(ktxt), nrc_ktxt_list):
        return "NRC"
    else:
        return "M"


def group_position_sieve(order: str, stadler_id: str, price: str, group_orderd_list: list) -> bool:
    """ Grupppenpostion do oflagowania na poziomie importu materiallisty 1. Gruppenposition scenariusz-jest jako
    pozycja w zamówieniu to w kolumnie grupp-dodaj flagę gruppen dla wszystkich pozycji o cenie 0 wewnątrz
    zamówienia; pozostałe są jako zwykłe Wydzieli się w ten sposób lista gruppenposition na projekcie na poszczególne
    pojazdy"""
    if str(order) in group_orderd_list and str(price) == '0':
        return True
    elif str(stadler_id) == '12004576':
        return True
    else:
        return False

def fz_correction(von:str, bis:str, bis_project=0) -> [int, int]:
    # float correction
    von = rounddown(float(von))
    bis = rounddown(float(bis))
    # empty values correction
    if von == '':
        von = 0
    if bis == '':
        bis = 0
    # negative values correction
    if von < 0 <= bis:
        von = abs(von)
    if von >= 0 > bis:
        bis = abs(bis)
    if von < 0 and 0 > bis > von:
        von = abs(von)
        bis = abs(bis)
    if 0 > von > bis and bis < 0:
        von = abs(von)
        bis = abs(bis)

    # reverse correction
    if von > bis:
        start = bis
        end = von
    else:
        start = von
        end = bis
    # correct to not be higher than project max
    if 0 < bis_project < end:
        end = bis_project

    return start, end

def fz_list(von, bis) -> str:
    fz = []
    for x in range(von, bis + 1):
        fz.append(str(x))
    return str.join(', ', fz)

def order_category(order_id: str) -> str:
    if str(order_id).isnumeric():
        return 'standard'
    else:
        return order_id.rstrip('1234567890.,')

def import_infor_data(project: str, standard: str, path_material: str, path_save:str) -> pd.DataFrame:
    """"""

    skipped_rows, used_col_names = only_used_rows_n_cols(pd.read_excel(path_material, dtype='string', nrows=100))
    if skipped_rows > 1:
        df_material = pd.read_excel(path_material, dtype='string', skiprows=skipped_rows, usecols=used_col_names)
    else:
        df_material = pd.read_excel(path_material, dtype='string', usecols=used_col_names)

    match standard:
        case "STAG":
            df_material = df_material.rename(columns=file_import_map.infor_col_dict_STAG)  # STAG
        case "STAPS":
            df_material = df_material.rename(columns=file_import_map.infor_col_dict_STAPS)  # STAPS
        case 'STAPS_single':
            df_material = df_material.rename(
                columns=file_import_map.infor_col_dict_STAPS_single)  # STAPS_single project
        case _:
            print("Defined standard not included in script..")  # TODO: Log error and end.

    df_material = df_material[file_import_map.infor_col_list_short]
    project_fz_max = reference_map.file_path_dicts.get(str(project)).get('fz_max')
    # !!!!!!!!!!!!!!! CHECK AND REPORT - correct data source and only standard mistakes
    df_material = df_material.dropna(subset='project')
    df_material = df_material.dropna(subset='order_delivery_date')
    df_material = df_material.dropna(subset='order_id')
    df_material['unit_price_basis'] = df_material['unit_price_basis'].apply(lambda x:
                                                                            1 if float(x) <= 0 else x)  # correction
    df_material[['fz_start', 'fz_end']] = df_material\
        .apply(lambda row: fz_correction(row.fz_start, row.fz_end, project_fz_max), axis=1, result_type='expand')  # correction

    # TODO: load - check - report or go further
    # preisbasis errors
    # check von - bis errors
    # check if car_max is not missed
    # generate report

    # !!!!!!!!!!!!!!! PROCESS
    df_material['bg_general'] = df_material['bg_general'].apply(lambda x: str(x)[1:4])
    df_material['order_create_date'] = df_material['order_create_date'] \
        .apply(lambda x: datetime.date(int(str(x)[:4]), int(str(x)[5:7]), int(str(x)[8:10])))
    df_material['order_delivery_date'] = df_material['order_delivery_date'] \
        .apply(lambda x: datetime.date(int(str(x)[:4]), int(str(x)[5:7]), int(str(x)[8:10])))
    df_material['NRC'] = df_material.apply(lambda row: nrc_sieve(str(row.description_1).lower(), row.fz_start), axis=1)

    df_material['fz_list'] = df_material.apply(lambda row: fz_list(row.fz_start, row.fz_end), axis=1)
    df_material['fz_count'] = df_material['fz_list'].apply(lambda x: len(str(x).split(sep=',')))

    df_material['quantity_per_fz'] = df_material.apply(lambda row:
                                                       0 if float(row.order_quantity) == 0.0
                                                       else float(row.order_quantity) / float(row.fz_count), axis=1)

    df_material['price_per_fz'] = df_material \
        .apply(lambda row: float(row.unit_price) / float(row.unit_price_basis) * row.quantity_per_fz, axis=1)

    df_material['order_category'] = df_material['order_id'].apply(lambda x: order_category(x))

    # gruppenposition sieve #12004576
    order_group_list = df_material['order_id'][df_material['stadler_id'] == '12004576']
    order_group_list = order_group_list.drop_duplicates().tolist()
    order_group_list = [str(x) for x in order_group_list]

    df_material['group'] = df_material.apply(lambda row: group_position_sieve(
        row.order_id, row.stadler_id, row.unit_price, order_group_list), axis=1)

    # df_material_fz0 = df_material[df_material['NRC'] != 'M'].copy()
    df_material['fz'] = df_material['fz_list'].apply(lambda x: str(x).split(sep=','))
    df_material = df_material.explode(column='fz', ignore_index=True)



    # df_material[df_material['group']].sort_values(by=['beleg_nr_best', 'acppart_preis'], ascending=False). \
    #     to_excel(path_save, index=False)
    df_material['fz'] = df_material['fz'].apply(lambda x: str(x).strip())
    df_material = df_material.fillna('')

    if path_save:
        df_material.to_excel(path_save, index=False)  # chyba się coś przywiesza 4503; 4499

    return df_material
