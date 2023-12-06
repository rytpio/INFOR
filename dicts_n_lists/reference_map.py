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

    '4473': {'material_list_raw': f'{default_data_path}\\MATERIAL_LIST\\4473_MATERIAL_LIST.xlsx',
             'material_list_processed': f'{default_data_path}\\MATERIAL_LIST\\4473_MATERIAL_LIST_EXPLODED.xlsx',
             'avz_raw': f'{default_data_path}\\AVZ\\4473_AVZ_raw.csv',
             'avz_processed': f'{default_data_path}\\AVZ\\4473_AVZ_processed.xlsx',
             'wz_raw': f'{default_data_path}\\WZ\\InforStruktur4473_01erNEIN.xlsx',
             'wz_processed': f'{default_data_path}\\WZ\\4473_WZ.xlsx',
             'device_list': f'{default_data_path}\\DEVICE_LIST\\4473_DEVICE_LIST.xlsx',
             'cable_quantity': f'{default_data_path}\\CABLE\\4473_CABLE_QUANTITY.xlsx',
             },

    # '4423': {'materialliste': r'C:\Users\rytpio\Downloads\4423_MateriallisteSTAPS_weekly_DWH_9.05.2023.xlsx',
    #          'avz': r'C:\Users\rytpio\Desktop\Projekty bieżące\NAKA\AVZ_test.xlsx',
    #          'infor_struct': r'C:\Users\rytpio\Desktop\Projekty '
    #                          r'bieżące\4423_TEST\other_data\InforStruktur4423KM_01erNEIN.xlsx',
    #          'apparateliste': r'C:\Users\rytpio\Desktop\Projekty bieżące\APPARATELISTE\4473_apparateliste_work.xlsx',
    #          'kabel_quantity': r'C:\Users\rytpio\Desktop\Projekty bieżące\Kabel_estimations\kabel_4473.xlsx'
    #          }
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
