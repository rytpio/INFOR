from pyjstat import pyjstat
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import requests
from collections import OrderedDict
import json

def eurostat_test():
    #EXAMPLE_URL = 'http://json-stat.org/samples/galicia.json'
    format='JSON'
    unit='I15'
    s_adj = 'NSA'
    indic_bt ='PRON'
    EXAMPLE_URL = f'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sts_inpp_q?format=' \
                  f'{format}&unit={unit}&s_adj={s_adj}&indic_bt={indic_bt}&' \
                  f'nace_r2=C302&nace_r2=C2815&nace_r2=C274&nace_r2=C272&nace_r2=C2711&nace_r2=C27&nace_r2=C2593&nace_r2=C2562&nace_r2=C256&nace_r2=C2511&nace_r2=C245&nace_r2=C2442&nace_r2=C2314&nace_r2=C2221&nace_r2=C22&nace_r2=C20&nace_r2=C2825&nace_r2=C13&nace_r2=C1621&nace_r2=C2011&nace_r2=C203&nace_r2=C2219&nace_r2=C231&nace_r2=C241&nace_r2=C2444&nace_r2=C251&nace_r2=C2512&nace_r2=C2561&nace_r2=C2591&nace_r2=C2594&nace_r2=C271&nace_r2=C2712&nace_r2=C2732&nace_r2=C2813&nace_r2=C2931'


    #data = requests.get(EXAMPLE_URL)
    dataset = pyjstat.Dataset.read(EXAMPLE_URL)
    df = dataset.write('dataframe')
    #print(df)
    df = pd.DataFrame(df)
    df.to_excel(r'C:\Users\rytpio\Desktop\Projekty bieżące\EuroSTAT.xlsx')

    # # read from dataframe
    # dataset_from_df = pyjstat.Dataset.read(df)
    # # write to json-stat
    # print(dataset_from_df.write())

#TODO: Add Czech, German, Austrian, Italian, Polish steel data sources for price estimations data

eurostat_test()

#TODO: ostatecznie to scraping danych z eurostat, systemów STAPS, techniki STAPS (koncept), ofert dostawców i przedstawianie w postaci produktu(wyceny)
#TODO: Eurostat - automat, system STAPS - automat + kategoryzacja własna lub start-up, technika staps-bid mngr, oferty-zakupy; scalenie całości - interfejs i system