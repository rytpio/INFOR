from dicts_n_lists import sql_import_map

default_data_path = r'C:\Users\rytpio\Desktop\Projekty bieżące\DATA'
file_path_dicts = {
    'currency_data': f'{default_data_path}\\Currency.xlsx',
    'bossard_price_staps': f'{default_data_path}\\BOSSARD\\bossard_stadlerID_list.xlsx',
    'bossard_kanban_staps': f'{default_data_path}\\BOSSARD\\Bossard 17.04.2024.xlsx',
    'ktl_kanban_staps': f'{default_data_path}\\KTL_KANBAN\\ktl_kanban_staps.xlsx',
    'ktl_kanban_stag': f'{default_data_path}\\KTL_KANBAN\\kanban_ktl_stag_stadlerID_list.xlsx',
    'cable_data': f'{default_data_path}\\CABLE\\cable_data.xlsx',

    '2371': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\2371_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\2371_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\2371_CABLE_QUANTITY.xlsx',
             'fz_max': 51  # Arriva Refit
             },
    '4292': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4292_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4292_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'',#no wz OLD PROJECT
             # 'wz_processed': f'',#no wz OLD PROJECT
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4292_CABLE_QUANTITY.xlsx',
             'fz_max': 20
             },
    '4336': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4336_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4336_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4336_CABLE_QUANTITY.xlsx',
             'fz_max': 10
             },
    '4337': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4337_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4437_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4337_CABLE_QUANTITY.xlsx',
             'fz_max': 10
             },
    # '4341': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4341_MATERIAL_LIST.xlsx',
    #          'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4341_MATERIAL_LIST_EXPLODED.csv',
    #          # 'avz_raw': f'',
    #          # 'avz_processed': f'',
    #          # 'wz_raw': f'',#no wz STAMI
    #          # 'wz_processed': f'',#no wz STAMI
    #          # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
    #          'cable_quantity': f'{default_data_path}\\CABLE\\4341_CABLE_QUANTITY.xlsx',
    #             'fz_max': 7 #TrenItalia - tutaj tylko Outsourcing + czesc materiału
    #          },
    '4353': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4353_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4353_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4353_CABLE_QUANTITY.xlsx',
             'fz_max': 15  # teoretycznie do potwierdzenia
             },
    '4354': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4354_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4354_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4354_CABLE_QUANTITY.xlsx',
             'fz_max': 8
             },
    '4355': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4355_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4355_MATERIAL_LIST_EXPLODED.csv',
             'material_list_leftover': f'{default_data_path}\\MATERIAL_LIST_LEFTOVER\\4355_leftover.xlsx',
             'avz_raw': f'{default_data_path}\\AVZ\\4355_AVZ_raw.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4355_AVZ_processed.xlsx',
             'avz_knot': f'{default_data_path}\\AVZ_KNOT\\4355_knot.xlsx',  # recznie przyporzadkowane knot
             'fz_mat_avz_knot': f'{default_data_path}\\AVZ_knots\\4355_AVZ_knot.xlsx',  # pozycje cen dla kazdego fz
             'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4355_01erNEIN.xlsx',
             'wz_processed': f'{default_data_path}\\WZ\\4355_WZ.xlsx',
             'device_list': f'{default_data_path}\\DEVICE_LIST\\4355_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4355_CABLE_QUANTITY.xlsx',



             'fz_max': 11  # FLIRT 3 car (initial from 2018 was 13 fz's ?)
             },
    '4362': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4362_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4362_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4362_CABLE_QUANTITY.xlsx',
             'fz_max': 7  #TPER
             },
    '4382': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4382_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4382_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'',#no wz OLD PROJECT
             # 'wz_processed': f'',#no wz OLD PROJECT
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4382_CABLE_QUANTITY.xlsx',
             'fz_max': 10,  #4 tlg FLIRT EMU
             },
    '4388': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4388_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4388_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4388_CABLE_QUANTITY.xlsx',
             'fz_max': 40
             },
    '4413': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4413_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4413_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4413_CABLE_QUANTITY.xlsx',
             'fz_max': 10
             },
    '4421': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4421_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4421_MATERIAL_LIST_EXPLODED.csv',
             'avz_raw': f'{default_data_path}\\AVZ\\4421_AVZ_raw.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4421_AVZ_processed.xlsx',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4421_CABLE_QUANTITY.xlsx',
             'fz_max': 35  # a nie 21 ?? gesamtlista z 2018
             },
    '4423': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4423_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4423_MATERIAL_LIST_EXPLODED.csv',
             'avz_raw': f'{default_data_path}\\AVZ\\4423_AVZ_raw.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4423_AVZ_processed.xlsx',
             'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4423KM_01erNEIN.xlsx',
             'wz_processed': f'{default_data_path}\\WZ\\4423_WZ.xlsx',
             'device_list': f'{default_data_path}\\DEVICE_LIST\\4423_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             'fz_max': 61
             },
    '4431': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4431_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4431_MATERIAL_LIST_EXPLODED.csv',
             'avz_raw': f'{default_data_path}\\AVZ\\4431_AVZ_raw.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4431_AVZ_processed.xlsx',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             'device_list': f'{default_data_path}\\DEVICE_LIST\\4431_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx', # cable STAMI
             'fz_max': 21
             },
    '4432': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4432_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4432_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             'fz_max': 10
             },
    '4433': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4433_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4433_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4473_01erNEIN.xlsx',
             # 'wz_processed': f'{default_data_path}\\WZ\\4473_WZ.xlsx',
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             'fz_max': 21
             },
    '4444': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4444_MATERIAL_LIST.xlsx',  # new-not full
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4444_MATERIAL_LIST_EXPLODED.csv',
             'material_list_leftover': f'{default_data_path}\\MATERIAL_LIST_LEFTOVER\\4444_leftover.xlsx',
             'avz_raw': f'{default_data_path}\\AVZ\\4444_AVZ_raw.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4444_AVZ_processed.xlsx',
             'avz_knot': f'{default_data_path}\\AVZ_KNOT\\4444_knot.xlsx',  # recznie przyporzadkowane knot
             'fz_mat_avz_knot': f'{default_data_path}\\AVZ_knots\\4444_AVZ_knot.xlsx',  # pozycje cen dla kazdego fz
             'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4444_01erNEIN.xlsx',
             'wz_processed': f'{default_data_path}\\WZ\\4444_WZ.xlsx',
             'device_list': f'{default_data_path}\\DEVICE_LIST\\4444_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4444_CABLE_QUANTITY.xlsx',
             'fz_max': 30
             },
    '4450': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4450_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4450_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             'fz_max': 1  # SOB - cabling confection; only in STAPS!
             },
    '4453': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4453_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4453_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             'fz_max': 7  # SOB - cabling confection; only in STAPS!
             },
    '4454': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4454_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4454_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             'fz_max': 7  # SOB - cabling confection; only in STAPS!
             },
    # '4465': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4465_MATERIAL_LIST.xlsx',
    #          'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4465_MATERIAL_LIST_EXPLODED.csv',
    #          # 'avz_raw': f'',
    #          # 'avz_processed': f'',
    #          # 'wz_raw': f'',#no wz STAMI
    #          # 'wz_processed': f'',#no wz STAMI
    #          # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
    #          # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
    #         'fz_max': 0 # LKA additional car C;
    #          },
    '4468': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4468_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4468_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             'fz_max': 5  #EAV FNM - same as L-4444; even documentation 1:1
             },
    '4471': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4471_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4471_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             'fz_max': 62
             #SBH - Hannover from Pankow; non standard FLIRT; can be also without single fz's (made in STAP)
             },
    '4473': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4473_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4473_MATERIAL_LIST_EXPLODED.csv',
             'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4473_01erNEIN.xlsx',
             'wz_processed': f'{default_data_path}\\WZ\\4473_WZ.xlsx',
             'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             'fz_max': 12
             },
    '4497': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4497_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4497_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             'fz_max': 5  # 3 car diagnostic RFI
             },
    '4499': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4499_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4499_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4473_01erNEIN.xlsx',
             # 'wz_processed': f'{default_data_path}\\WZ\\4473_WZ.xlsx',
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             'fz_max': 3  #3 car, diagnostic ADIF
             },
    '4503': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4503_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4503_MATERIAL_LIST_EXPLODED.csv',
             'material_list_leftover': f'{default_data_path}\\MATERIAL_LIST_LEFTOVER\\4503_leftover.xlsx',
             'avz_raw': f'{default_data_path}\\AVZ\\4503_AVZ_raw+bogies.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4503_AVZ_processed.xlsx',
             'avz_knot': f'{default_data_path}\\AVZ_KNOT\\4503_knot.xlsx',  # recznie przyporzadkowane knot
             #'fz_mat_avz_knot': f'{default_data_path}\\AVZ_knots\\4503_AVZ_knot.xlsx',  # pozycje cen dla kazdego fz
             'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4503_01erNEIN.xlsx',
             'wz_processed': f'{default_data_path}\\WZ\\4503_WZ.xlsx',
             'device_list': f'{default_data_path}\\DEVICE_LIST\\4503_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4503_CABLE_QUANTITY.xlsx',
             'fz_max': 60
             #60 pojazdów, 2 pojazdy 61,62 dodane do zakresu jako KRK3 i TINA; 1 bląd w zam. 10-593226 zamiast 10-12
             },
    '4533': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4533_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4533_MATERIAL_LIST_EXPLODED.csv',
             'material_list_leftover': f'{default_data_path}\\MATERIAL_LIST_LEFTOVER\\4533_leftover.xlsx',
             'avz_raw': f'{default_data_path}\\AVZ\\4533_AVZ_raw.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4533_AVZ_processed.xlsx',
             'avz_knot': f'{default_data_path}\\AVZ_KNOT\\4533_knot.xlsx',  # recznie przyporzadkowane knot
             'fz_mat_avz_knot': f'{default_data_path}\\AVZ_knots\\4533_AVZ_knot.xlsx',  # pozycje cen dla kazdego fz
             # 'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4473_01erNEIN.xlsx',
             # 'wz_processed': f'{default_data_path}\\WZ\\4473_WZ.xlsx',
             'device_list': f'{default_data_path}\\DEVICE_LIST\\4533_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4533_CABLE_QUANTITY.xlsx',
             'fz_max': 4
             },
    '4541': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4541_MATERIAL_LIST.xlsx',  # new - not full
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4541_MATERIAL_LIST_EXPLODED.csv',
             'material_list_leftover': f'{default_data_path}\\MATERIAL_LIST_LEFTOVER\\4541_leftover.xlsx',
             'avz_raw': f'{default_data_path}\\AVZ\\4541_AVZ_raw.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4541_AVZ_processed.xlsx',
             'avz_knot': f'{default_data_path}\\AVZ_KNOT\\4541_knot.xlsx',  # recznie przyporzadkowane knot
             'fz_mat_avz_knot': f'{default_data_path}\\AVZ_knots\\4541_AVZ_knot.xlsx',  # pozycje cen dla kazdego fz
             'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4541_01erNEIN.xlsx',
             'wz_processed': f'{default_data_path}\\WZ\\4541_WZ.xlsx',
             'device_list': f'{default_data_path}\\DEVICE_LIST\\4541_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4541_CABLE_QUANTITY.xlsx',
             'fz_max': 25  #25 pojazdów 15+opt10 - wpisane 60 i 61 na niektórych zamówieniach.
             },
    '4542': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4542_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4542_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4473_01erNEIN.xlsx',
             # 'wz_processed': f'{default_data_path}\\WZ\\4473_WZ.xlsx',
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             },
    '4547': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4547_MATERIAL_LIST.xlsx',  # new-not full
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4547_MATERIAL_LIST_EXPLODED.csv',
             'material_list_leftover': f'{default_data_path}\\MATERIAL_LIST_LEFTOVER\\4547_leftover.xlsx',
             'avz_raw': f'{default_data_path}\\AVZ\\4547_AVZ_raw.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4547_AVZ_processed.xlsx',
             'avz_knot': f'{default_data_path}\\AVZ_KNOT\\4547_knot.xlsx',  # recznie przyporzadkowane knot
             'fz_mat_avz_knot': f'{default_data_path}\\AVZ_knots\\4547_AVZ_knot.xlsx',  # pozycje cen dla kazdego fz
             'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4547_01erNEIN.xlsx',
             'wz_processed': f'{default_data_path}\\WZ\\4547_WZ.xlsx',
             'device_list': f'{default_data_path}\\DEVICE_LIST\\4547_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4547_CABLE_QUANTITY.xlsx',
             'fz_max': 18
             },
    '4556': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4556_MATERIAL_LIST.xlsx',  # new-not full
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4556_MATERIAL_LIST_EXPLODED.csv',
             'material_list_leftover': f'{default_data_path}\\MATERIAL_LIST_LEFTOVER\\4556_leftover.xlsx',
             'avz_raw': f'{default_data_path}\\AVZ\\4556_AVZ_raw.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4556_AVZ_processed.xlsx',
             'avz_knot': f'{default_data_path}\\AVZ_KNOT\\4556_knot.xlsx',  # recznie przyporzadkowane knot
             'fz_mat_avz_knot': f'{default_data_path}\\AVZ_knots\\4556_AVZ_knot.xlsx',  # pozycje cen dla kazdego fz
             'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4556_01erNEIN.xlsx',
             'wz_processed': f'{default_data_path}\\WZ\\4556_WZ.xlsx',
             'device_list': f'{default_data_path}\\DEVICE_LIST\\4556_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4556_CABLE_QUANTITY.xlsx',
             'fz_max': 29  # 3 wagony; Tram; 2024
             },
    '4557': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4557_MATERIAL_LIST.xlsx',  # new-not full
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4557_MATERIAL_LIST_EXPLODED.csv',
             'material_list_leftover': f'{default_data_path}\\MATERIAL_LIST_LEFTOVER\\4557_leftover.xlsx',
             'avz_raw': f'{default_data_path}\\AVZ\\4557_AVZ_raw.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4557_AVZ_processed.xlsx',
             'avz_knot': f'{default_data_path}\\AVZ_KNOT\\4557_knot.xlsx',  # recznie przyporzadkowane knot
             'fz_mat_avz_knot': f'{default_data_path}\\AVZ_knots\\4557_AVZ_knot.xlsx',  # pozycje cen dla kazdego fz
             'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4557_01erNEIN.xlsx',
             'wz_processed': f'{default_data_path}\\WZ\\4557_WZ.xlsx',
             #'device_list': f'{default_data_path}\\DEVICE_LIST\\4557_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4557_CABLE_QUANTITY.xlsx',
             'fz_max': 17  # 5 wagonow; Tram; 2024
             },
    '4568': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4568_MATERIAL_LIST.xlsx',  # new-not full
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4568_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4473_01erNEIN.xlsx',
             # 'wz_processed': f'{default_data_path}\\WZ\\4473_WZ.xlsx',
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             'fz_max': 20  # FLIRT 4 car
             },
    '4577': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4547_MATERIAL_LIST.xlsx',  # new-not full
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4547_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4473_01erNEIN.xlsx',
             # 'wz_processed': f'{default_data_path}\\WZ\\4473_WZ.xlsx',
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             'fz_max': 18
             },
    '10308100': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\10308100_MATERIAL_LIST.xlsx',
                 # new-not full
                 'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\10308100_MATERIAL_LIST_EXPLODED.csv',
                 # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
                 # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
                 # 'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4473_01erNEIN.xlsx',
                 # 'wz_processed': f'{default_data_path}\\WZ\\4473_WZ.xlsx',
                 # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
                 # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
                 },

}

sql_col = {
    'currency_data': sql_import_map.currency_sql_col_dict,
    'material_list': sql_import_map.material_list_sql_col_dict,
    'material_list_wz_relationship': sql_import_map.material_list_wz_relationship_sql_col_dict,
    'material_list_leftover': sql_import_map.material_list_leftover_sql_col_dict,
    'avz': sql_import_map.avz_sql_col_dict,
    'avz_knot': sql_import_map.avz_knot_sql_col_dict,
    'avz_mat_knot': sql_import_map.avz_mat_knot_sql_col_dict,
    'avz_knot_relationship': sql_import_map.avz_knot_relationship_sql_col_dict,

    'wz': sql_import_map.wz_staps_sql_col_dict,

    'ktl_kanban_staps': sql_import_map.ktl_staps_sql_col_dict,
    'ktl_kanban_stag': sql_import_map.ktl_stag_sql_col_dict,

    'bossard_price_staps': sql_import_map.bossard_price_sql_short_col_dict,
    'bossard_kanban_staps': sql_import_map.bossard_sql_short_col_dict,

    'device_list': sql_import_map.device_list_sql_col_dict,
    'material_list_device_list_relationship': sql_import_map.material_list_device_list_relationship_sql_col_dict,

    'cable_data': sql_import_map.cable_data_sql_col_dict,
    'cable_quantity': sql_import_map.cable_quantity_sql_col_dict,
    'cable_relationship': sql_import_map.cable_relationship_sql_col_dict
}

#TODO: Zastanowić się nad relacjami na przyszłość - potrzeba wtedy dużo tabel pośrednich oraz przerobienia ze sprawdzeniem większosci skryptów SQL
sql_fk_col = {
    'avz': sql_import_map.avz_sql_col_fk_dict,
    'avz_knot_relationship': sql_import_map.avz_knot_relationship_fk_sql_col_dict,

    'material_list': sql_import_map.material_list_sql_col_fk_dict,
    'material_list_wz_relationship': sql_import_map.material_list_wz_relationship_fk_sql_col_dict,

    'device_list': sql_import_map.device_list_sql_col_fk_dict,
    'material_list_device_list_relationship': sql_import_map.material_list_device_list_relationship_fk_sql_col_dict,

    'cable_relationship': sql_import_map.cable_relationship_fk_sql_col_dict,

    'bossard_price_staps': sql_import_map.bossard_price_fk_sql_col_dict
}
