import datetime
import os.path

import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

from math import floor as rounddown
from dicts_n_lists import file_import_map


def nrc_sieve(ktxt, fzvon) -> str:
    nrc_ktxt_list = [
        'kosten',
        'muster'
        'dienstleistung',
        'mehrleistungen',
        'abnahmepruefzeugnis',
        'datenblatt',
        'RAM',
        'dokumentation',
        'transport',
        'zuschlag',
        'stunden',
        'brandschutzanforderung',
        'schulung',
        'AR00'
    ]
    # TODO: rozdzielać NRC gdzie są pojazdy i przypisywać do pozycji NRC/RC na pojazd
    # ewentualnie dopasowac jeszcze po numerze zamówienia do jakiego komponentu należy NRC/RC
    # wautowac liste na zewnatrz

    func_list_in_str = lambda text, list_: any(filter(lambda x: x in text, list_))
    if str(fzvon) == '0':
        return "NRC"
    elif func_list_in_str(str(ktxt), nrc_ktxt_list):
        return "NRC"
    else:
        return "M"

def group_position_sieve(order :str, stadler_id :str, price :str, group_orderd_list :list) -> bool:
    """ Grupppenpostion do oflagowania na poziomie importu materiallisty
1. Gruppenposition scenariusz - jest jako pozycja w zamówieniu to w kolumnie grupp - dodaj flagę gruppen dla wszystkich pozycji o cenie 0 wewnątrz zamówienia; pozostałe sa jako zwykłe
Wydzieli się w ten sposób lista gruppenposition na projekcie na poszczególne pojazdy """
    if order in group_orderd_list and price == '0':
        return True
    elif stadler_id == '12004576':
        return True
    else:
        return False
   


def import_infor_data(project: str, standard: str, path_material: str) -> pd.DataFrame:

    #!!!!!!!!!!!!!!!1 IMPORT
    df_material = pd.read_excel(path_material, dtype='string')

    match standard:
        case "STAG":
            df_material = df_material.rename(columns=col_dicts.infor_col_dict_STAG)  # STAG
        case "STAPS":
            df_material = df_material.rename(columns=col_dicts.infor_col_dict_STAPS)  # STAPS
        case 'STAPS_single':
            df_material = df_material.rename(columns=col_dicts.infor_col_dict_STAPS_single)  # STAPS_single project
        case _:
            print("Brak pasującego standardu.")  # TODO: Log error and end.

    df_material = df_material[col_dicts.infor_col_dict_short]

    #!!!!!!!!!!!!!!! CHECK AND REPORT - correct data source and only standard mistakes
    df_material = df_material.dropna(subset='komm')
    df_material = df_material.dropna(subset='segm3_term')
    df_material = df_material.dropna(subset='beleg_nr_best')
    df_material['f_preisbasis'] = df_material['f_preisbasis'].apply \
        (lambda x: 1 if float(x) <= 0 else x)  # correction
    df_material['fzvon'] = df_material.apply \
        (lambda row: rounddown(float(row.fzvon)) if float(row.fzvon) <= float(row.fzbis) else
         rounddown(float(row.fzbis)), axis=1)  # correction
    df_material['fzbis'] = df_material.apply \
        (lambda row: rounddown(float(row.fzbis)) if float(row.fzvon) <= float(row.fzbis) else
         rounddown(float(row.fzvon)), axis=1)  # correction

    # TODO: load - check - report or go further
    # check von - bis errors
    # check if car_max is not missed
    # generate report

    # !!!!!!!!!!!!!!! PROCESS
    df_material['inlkto'] = df_material['inlkto'].apply(lambda x: str(x)[1:4])
    df_material['createdate'] = df_material['createdate'].apply \
        (lambda x: datetime.date(int(str(x)[:4]), int(str(x)[5:7]), int(str(x)[8:10])))
    df_material['segm3_term'] = df_material['segm3_term'].apply \
       (lambda x: datetime.date(int(str(x)[:4]), int(str(x)[5:7]), int(str(x)[8:10])))
    df_material['NRC'] = df_material.apply(lambda row: nrc_sieve(str(row.ktxt).lower(), row.fzvon), axis=1)

    def fz_list(von, bis) -> list:
        fz = []
        for x in range(von, bis + 1):
            fz.append(x)
        return fz
    df_material['fz_list'] = df_material.apply(lambda row: fz_list(row.fzvon, row.fzbis), axis=1)
    df_material['fz_count'] = df_material['fz_list'].apply(lambda x: len(list(x)))

    df_material['quantity_per_fz'] = df_material.apply(lambda row: 0 if float(row.segm3_meng) == 0.0 else
    float(row.segm3_meng) / float(row.fz_count), axis=1)

    df_material['price_per_fz'] = df_material.apply(
        lambda row: float(row.acppart_preis) / float(row.f_preisbasis) * row.quantity_per_fz, axis=1)

    def order_category(order_id: str) -> str:
        if order_id.isnumeric():
            return 'standard'
        else:
            return order_id.rstrip('1234567890.,')
    df_material['order_category'] = df_material['beleg_nr_best'].apply(lambda x: order_category(x))

    #df_material_list = df_material['mnr'].drop_duplicates().tolist()
    #material_col_list = df_material.columns.tolist()

    #teoretycznie karuzela po projektant STAPR z wprowadzeniem w dany komponent
    #głównie typy i proces produkcji zabudowy, obudowy
    #materiały katalogowe nie potrzeba
    #kalkulator zapotrzebowania i cen kabli / projekt
    #kalkulator zapotrzebowania materiału elektrycznego i ktl/kanban na projekt
    #bogie - plt
    #kasten - plt
    #420 - plt
    #brakes - plt pneum (vit)
    #410/430 - plt antrieb (florian)
    #klasy klejenia, typy materiału, szkło, siedzenia, podłogi, sufity, luftkanal, elementy spawane, drewniane elementy
    #lakierowanie, malowanie, okleiny typ

    #gruppenposition sieve #12004576
    order_group_list = df_material['beleg_nr_best'][df_material['mnr'] == '12004576']
    order_group_list = order_group_list.drop_duplicates().tolist()

    df_material['group'] = df_material.apply(lambda row: group_position_sieve(
        row.beleg_nr_best, row.mnr, row.acppart_preis, order_group_list), axis=1)


    #df_material_fz0 = df_material[df_material['NRC'] != 'M'].copy()
    df_material['fz'] = df_material['fz_list']
    df_material = df_material.explode(column='fz', ignore_index=True)

    #path_save = os.path.join(os.path.dirname(path_material), f'{project}_material_exploded.xlsx')
    #df_material.to_excel(path_save, index=False) #chyba się coś przywiesza 4503; 4499
    path_save = os.path.join(os.path.dirname(path_material), f'{project}_material_grouppositions_exploded.xlsx')
    df_material[df_material['group']].sort_values(by=['beleg_nr_best', 'acppart_preis'], ascending=False).\
        to_excel(path_save, index=False)

    return df_material #, df_material_fz0


import_infor_data('4423', 'STAPS_single', os.path.join(r'C:\Users\rytpio\Desktop\Projekty bieżące\MATLIST', '4423_Matlist.xlsx'))

