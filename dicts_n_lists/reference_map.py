from dicts_n_lists import sql_import_map

# TODO: Rozbić ścieżki na poszczególne projekty lub zlikwidować całkowicie
default_data_path = r'C:\Users\rytpio\Desktop\Projekty bieżące\DATA'
file_path_dicts = {
    'currency': f'{default_data_path}\\Currency.xlsx',
    'bossard_price_staps': f'{default_data_path}\\BOSSARD\\bossard_stadlerID_list.xlsx',
    'bossard_kanban_staps': f'{default_data_path}\\BOSSARD\\Bossard 04.12.2023.xlsx',
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
             },
    '4292': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4292_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4292_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'',#no wz OLD PROJECT
             # 'wz_processed': f'',#no wz OLD PROJECT
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4292_CABLE_QUANTITY.xlsx',
             },
    '4336': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4336_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4336_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4336_CABLE_QUANTITY.xlsx',
             },
    '4337': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4337_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4437_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4337_CABLE_QUANTITY.xlsx',
             },
    '4341': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4341_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4341_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4341_CABLE_QUANTITY.xlsx',
             },
    '4353': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4353_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4353_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4353_CABLE_QUANTITY.xlsx',
             },
    '4354': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4354_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4354_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4354_CABLE_QUANTITY.xlsx',
             },
    '4355': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4355_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4355_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'',#no wz OLD PROJECT
             # 'wz_processed': f'',#no wz OLD PROJECT
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4355_CABLE_QUANTITY.xlsx',
             },
    '4362': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4362_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4362_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4362_CABLE_QUANTITY.xlsx',
             },
    '4382': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4382_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4382_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'',#no wz OLD PROJECT
             # 'wz_processed': f'',#no wz OLD PROJECT
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4382_CABLE_QUANTITY.xlsx',
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
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4421_CABLE_QUANTITY.xlsx',
             'fz_max': 20
             },
    '4423': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4423_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4423_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4473_01erNEIN.xlsx',
             # 'wz_processed': f'{default_data_path}\\WZ\\4473_WZ.xlsx',
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             'fz_max': 61
             },
    '4431': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4431_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4431_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
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
             },
    '4433': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4433_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4433_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4473_01erNEIN.xlsx',
             # 'wz_processed': f'{default_data_path}\\WZ\\4473_WZ.xlsx',
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             },
    '4444': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4444_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4444_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
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
             },
    '4453': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4453_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4453_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             },
    '4454': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4454_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4454_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             },
    '4465': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4465_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4465_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             },
    '4468': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4468_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4468_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             },
    '4471': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4471_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4471_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'',
             # 'avz_processed': f'',
             # 'wz_raw': f'',#no wz STAMI
             # 'wz_processed': f'',#no wz STAMI
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
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
             },
    '4499': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4499_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4499_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4473_01erNEIN.xlsx',
             # 'wz_processed': f'{default_data_path}\\WZ\\4473_WZ.xlsx',
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             },
    '4503': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4503_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4503_MATERIAL_LIST_EXPLODED.csv',
             'avz_raw': f'{default_data_path}\\AVZ\\4503_AVZ_raw+bogies.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4503_AVZ_processed.xlsx',
             'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4503_01erNEIN.xlsx',
             'wz_processed': f'{default_data_path}\\WZ\\4503_WZ.xlsx',
             'device_list': f'{default_data_path}\\DEVICE_LIST\\4503_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4503_CABLE_QUANTITY.xlsx',
             'fz_max': 60 #60 pojazdów, 2 pojazdy 61,62 dodane do zakresu jako KRK3 i TINA; 1 bląd w zam. 10-593226 zamiast 10-12
             },
    '4533': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4533_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4533_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4473_01erNEIN.xlsx',
             # 'wz_processed': f'{default_data_path}\\WZ\\4473_WZ.xlsx',
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             },
    '4541': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4541_MATERIAL_LIST.xlsx',  # new - not full
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4541_MATERIAL_LIST_EXPLODED.csv',
             # 'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             # 'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             # 'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4473_01erNEIN.xlsx',
             # 'wz_processed': f'{default_data_path}\\WZ\\4473_WZ.xlsx',
             # 'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             # 'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
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
             'avz_raw': f'{default_data_path}\\AVZ\\4547_AVZ_raw.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4547_AVZ_processed.xlsx',
             'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4547_01erNEIN.xlsx',
             'wz_processed': f'{default_data_path}\\WZ\\4547_WZ.xlsx',
             'device_list': f'{default_data_path}\\DEVICE_LIST\\4547_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4547_CABLE_QUANTITY.xlsx',
             'fz_max': 18
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
    'material_list': sql_import_map.material_list_sql_col_dict,
    'material_list_wz_relationship': sql_import_map.material_list_wz_relationship_sql_col_dict,
    'avz': sql_import_map.avz_sql_col_dict,
    'avz_knot': sql_import_map.avz_knot_sql_col_dict,
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
