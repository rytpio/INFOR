from pyjstat import pyjstat
import pandas as pd
from dicts_n_lists import ref_lists

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Eurostat Q1.2024 pierwszy rzut w 30.04.2024; update 15.05.2024; update 07.06.2024
# czyżby Eurostat wrzucał miesiąc po zakończeniu danego kwartału dane ?
#1-3//04 - Q1, 4-6//07 - Q2, 7-9//10 - Q3, 10-12//1 - Q4

import requests
from collections import OrderedDict
import json
import unicodedata

def eurostat():
    """"""
    indicator_list = ref_lists.eurostat_indicator_list
    format_file = 'JSON'
    unit = 'I15'
    s_adj = 'NSA'
    indic_bt = 'PRON'
    url = f'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sts_inpp_q?format=' \
          f'{format_file}&unit={unit}&s_adj={s_adj}&indic_bt={indic_bt}' \
          f'&nace_r2={str("&nace_r2=").join(indicator_list)}'

    dataset = pyjstat.Dataset.read(url)
    df = dataset.write('dataframe')
    df = pd.DataFrame(df)
    df.to_csv(r'C:\Users\rytpio\Desktop\Projekty bieżące\EuroSTAT_x.csv', index=False, sep=';')#, encoding='iso-8859-1') # has special character accents uoa
    df[['Year', 'Quarter']] = df.apply(lambda x: str(x.Time).split('-'), result_type="expand", axis=1)
    df.dropna(subset=['Year'])
    df = df[df['value'] > 0]
    df['Year'] = df['Year'].astype(int)
    df = df[df['Year'] >= 2015]
    df['value'] = df['value'].apply(lambda x: str(x).replace('.', ','))
    cols = ['Statistical classification of economic activities in the European Community (NACE Rev. 2)',
             'Geopolitical entity (reporting)', 'value', 'Year', 'Quarter']
    df = df[cols]
    for col in cols:
        df[col] = df[col].apply(lambda x: unicodedata.normalize('NFKD', str(x)).encode('ascii', 'ignore').decode('utf-8'))  # działa


    df.to_csv(r'C:\Users\rytpio\Desktop\Projekty bieżące\EuroSTAT_3.csv', index=False, sep=';', encoding="iso-8859-1")
    #  excel chart creation

    # select year / quarter as axis x - need to be
    # for each classification; for each geo group select values;

    # group #cat #geo-group #quarter
    # value  #price output
    # diagram in #year and #quarter


eurostat()

# TODO: Add Czech, German, Austrian, Italian, Polish steel data sources for price estimations data
# TODO: Eurostat - automat, system STAPS - automat + kategoryzacja własna lub start-up, technika staps-bid mngr, oferty-zakupy; scalenie całości - interfejs i system

# Zrobić  wskaźnik update dla każdego indeksu od danego roku a najlepiej kwartału
#
# For each country and Group variables
# if country values empty then go to group values but notice
#
#
# 2015 -100%
# Requested source purchase date with quarter or year,
# requested supplier country, requested purchase date in list with weight (
# 2023-Q3
# Search for closest to requested
# Prognose missing quarters based on previous quarters average; check with inflation from previous quarters

# year of purchase / quarter percent eg. 108% to 2015; year closest 116%; 116%-108% +100% is price level% acc. to eurostat
# quarters * average_quarter% + price level% is prognosed price level

# project in batches - average price for batches
# get price for every batch and assign weight (2 for 2023, 3 for 2024, 1 for 2026); get average
