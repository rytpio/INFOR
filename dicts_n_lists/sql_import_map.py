# /////////////// UNNASSIGNED.
fz_sql_col_dict = {
    'CONSTRAINT fk_material_list_id':
        'FOREIGN KEY(fz) REFERENCES material_list(fz) ON DELETE SET NULL ON UPDATE CASCADE'
}

# /////////////// CURRENCY.
currency_sql_col_dict = {
    'CURRENCY': 'VARCHAR(25)',
    'EUR': 'FLOAT',
    'DATE': 'DATE'
}

# ////////////// AVZ
avz_sql_col_dict = {
    'avz_struct_index': 'INTEGER',
    'level': 'INTEGER',
    'din': 'VARCHAR(3)',
    'din_txt': 'VARCHAR(100)',
    'unit': 'VARCHAR(10)',
    'quantity': 'FLOAT',
    'stadler_id': 'VARCHAR(16)',
    'article_rev': 'VARCHAR(5)',
    'position_number': 'INTEGER',
    'description_1': 'VARCHAR(100)',
    'description_2': 'VARCHAR(100)',
    'material': 'VARCHAR(50)',
    'material_new': 'VARCHAR(50)',
    'document': 'VARCHAR(50)',
    'document_nr': 'VARCHAR(50)',
    'position_etz': 'VARCHAR(50)',
    'doc_revision': 'VARCHAR(5)',
    'doc_status': 'VARCHAR(50)',
    'project': 'VARCHAR(20)',
    'project_name': 'VARCHAR(50)',
    'schematic_position': 'VARCHAR(50)',
    'vehicle_area': 'VARCHAR(50)',
    'classification': 'VARCHAR(50)',
    'initial_article': 'VARCHAR(50)',
    'root_article': 'VARCHAR(16)',
    'root_version': 'VARCHAR(5)',
    'supplier': 'VARCHAR(50)',
    'supplier_article_id': 'VARCHAR(50)',
    'supplier_type': 'VARCHAR(50)',
    'supplier_article_idx': 'VARCHAR(50)',
    'weight': 'FLOAT',
    'comment': 'VARCHAR(255)',
    'doc_class_id': 'VARCHAR(50)',
    'doc_supplier_nr': 'VARCHAR(50)',
    #   'DIN_ktxt': 'VARCHAR(255)',
    'pos_nr_category_bu_1951939': 'VARCHAR(255)',
    'breadcrumb': 'VARCHAR(255)',
    'lvl1': 'VARCHAR(255)',
    'lvl2': 'VARCHAR(255)',
    'lvl3': 'VARCHAR(255)',
    'lvl4': 'VARCHAR(255)',
    'lvl5': 'VARCHAR(255)',
    'lvl6': 'VARCHAR(255)',
    'avz_quantity_in_tree': 'FLOAT',
    'fk_bossard_kanban_staps': 'INTEGER NULL',
    'fk_ktl_kanban_staps': 'INTEGER NULL',
    'fk_ktl_kanban_stag': 'INTEGER NULL',
    'fk_wz': 'INTEGER NULL'
    # 'fk_avz_knot': 'INTEGER NULL'
}
avz_knot_sql_col_dict = { #przypisane nagłówki do reszty
    'project': 'VARCHAR(25)',
    'car': 'VARCHAR(50)', #domyślnie ALL, pozostałe wydzielić wagony ręcznie przed importem
    'knot_1': 'VARCHAR(255)',
    'knot_2': 'VARCHAR(255)',
    'knot_3': 'VARCHAR(255)',
    'bg': 'INTEGER',
    'din': 'VARCHAR(2)',
    'group_mask': 'VARCHAR(255)',
    'avz_breadcrumb': 'VARCHAR(500)', #knot_id
    'fk_avz': 'INTEGER NULL', #1:n, domyślnie powinien być NOT NULL - zawsze kompletne
}

avz_mat_knot_sql_col_dict = { # pozycje cenowy dla każdego pojazdu pod AVZ
    'project': 'VARCHAR(25)',
    'fz': 'INTEGER NULL', #na podstawie materialisty dla danego pojazdu
    'avz_id': 'INTEGER NULL', #bezpośredni id dla avz - musi pokrywać się z breadcrumb inaczej rozjazdy i należy wygenerować na nowo dla pewności
    'avz_breadcrumb': 'VARCHAR(500)', #knot_id 1:1 w połączeniu z avz_id
    'purchase_level': 'VARCHAR(50)',
    'purchased_status_exact': 'VARCHAR(50)',
    'purchased_status_general': 'VARCHAR(50)',
    'order_id': 'VARCHAR(255)',
    'supplier_mat': 'VARCHAR(255)',
    'price': 'FLOAT',
    'currency': 'VARCHAR(50)',
    'price_eur': 'FLOAT',
    'price_eur_sum': 'FLOAT',
    'fk_avz': 'INTEGER NULL' #1:n, domyślnie powinien być NOT NULL - zawsze kompletne
}

#Potrzebna jeszcze pozycje kalkulacji - maska - pozycja avz/matlist - maska

avz_sql_col_fk_dict = {
    'CONSTRAINT fk_bossard_kanban_staps': 'FOREIGN KEY(fk_bossard_kanban_staps) REFERENCES '
                                          'bossard_kanban_staps(bossard_kanban_staps) '
                                          'ON DELETE SET NULL ON UPDATE CASCADE',
    'CONSTRAINT fk_ktl_kanban_staps': 'FOREIGN KEY(fk_ktl_kanban_staps) REFERENCES ktl_kanban_staps(ktl_kanban_staps) '
                                      'ON DELETE SET NULL ON UPDATE CASCADE',
    'CONSTRAINT fk_ktl_kanban_stag': 'FOREIGN KEY(fk_ktl_kanban_stag) REFERENCES ktl_kanban_stag(ktl_kanban_stag) '
                                     'ON DELETE SET NULL ON UPDATE CASCADE'
    # 'CONSTRAINT fk_avz_knot': 'FOREIGN KEY(fk_avz_knot) REFERENCES avz_knot(avz_knot) ON DELETE SET NULL ON UPDATE
    # CASCADE'
}
avz_knot_relationship_sql_col_dict = {
    'fk_avz': 'BIGINT NULL',
    'fk_avz_knot': 'BIGINT NULL'
}

avz_knot_relationship_fk_sql_col_dict = {
    'CONSTRAINT fk_avz': 'FOREIGN KEY(fk_avz) REFERENCES avz(avz) ON DELETE CASCADE ON UPDATE CASCADE',
    'CONSTRAINT fk_avz_knot': 'FOREIGN KEY(fk_avz_knot) REFERENCES avz_knot(avz_knot) ON DELETE CASCADE ON UPDATE '
                              'CASCADE'
}

# ////////////// Materialliste/INFOR
material_list_sql_col_dict = {
    'project': 'VARCHAR(25)',
    'order_id': 'VARCHAR(255)',
    'order_status': 'VARCHAR(25)',
    'order_create_date': 'VARCHAR(255)',
    'order_delivery_date': 'VARCHAR(255)',
    'stadler_id': 'VARCHAR(255)',
    'description_1': 'VARCHAR(255)',
    'supplier_id': 'VARCHAR(255)',
    'supplier_description_1': 'VARCHAR(255)',
    'order_quantity': 'VARCHAR(255)',
    'unit': 'VARCHAR(25)',
    'unit_price': 'VARCHAR(255)',
    'unit_price_basis': 'VARCHAR(25)',
    'currency': 'VARCHAR(25)',
    'supplier_name_id': 'VARCHAR(255)',
    'supplier': 'VARCHAR(255)',
    'supplier_country': 'VARCHAR(255)',
    'buyer': 'VARCHAR(255)',
    'bg_detail': 'VARCHAR(255)',
    'bg_general': 'VARCHAR(255)',
    'fz_start': 'VARCHAR(255)',
    'fz_end': 'VARCHAR(255)',
    'NRC': 'VARCHAR(255)',
    'fz_list': 'VARCHAR(255)',
    'fz_count': 'VARCHAR(255)',
    'quantity_per_fz': 'VARCHAR(255)',
    'price_per_fz': 'VARCHAR(255)',
    'order_category': 'VARCHAR(255)',
    'fz': 'VARCHAR(255)',
    'fk_bossard_kanban_staps': 'INTEGER NULL',
    'fk_ktl_kanban_staps': 'INTEGER NULL',
    'fk_ktl_kanban_stag': 'INTEGER NULL',
    'fk_cable_quantity': 'INTEGER NULL',
    'fk_wz': 'INTEGER NULL',  # no relation only for check
    'fk_avz': 'INTEGER NULL',  # no relation only for check
    'fk_device_list': 'INTEGER NULL',  # no relation only for check
    'dev_mask': 'VARCHAR(255)', # for leftover later fulfillment
    'avz_mask': 'VARCHAR(255)', # for leftover later fulfillment
    'leftover_mask': 'VARCHAR(255)', # for leftover later fulfillment
    'group_mask': 'VARCHAR(255)' # for leftover later fulfillment
}
material_list_sql_col_fk_dict = {
    'CONSTRAINT fk_bossard_kanban_staps': 'FOREIGN KEY(fk_bossard_kanban_staps) REFERENCES '
                                          'bossard_kanban_staps(bossard_kanban_staps) ON '
                                          'DELETE SET NULL ON UPDATE CASCADE',
    'CONSTRAINT fk_ktl_kanban_staps': 'FOREIGN KEY(fk_ktl_kanban_staps) REFERENCES ktl_kanban_staps(ktl_kanban_staps) '
                                      'ON DELETE SET NULL ON UPDATE CASCADE',
    'CONSTRAINT fk_ktl_kanban_stag': 'FOREIGN KEY(fk_ktl_kanban_stag) REFERENCES ktl_kanban_stag(ktl_kanban_stag) ON '
                                     'DELETE SET NULL ON UPDATE CASCADE',
    'CONSTRAINT fk_cable_quantity': 'FOREIGN KEY(fk_cable_quantity) REFERENCES cable_quantity(cable_quantity) ON '
                                    'DELETE SET NULL ON UPDATE CASCADE'
}
material_list_wz_relationship_sql_col_dict = {
    'fk_material_list': 'BIGINT NULL',
    'fk_wz': 'BIGINT NULL'
}
material_list_wz_relationship_fk_sql_col_dict = {
    'CONSTRAINT fk_material_list': 'FOREIGN KEY(fk_material_list) REFERENCES material_list(material_list) ON DELETE '
                                   'CASCADE ON UPDATE CASCADE',
    'CONSTRAINT fk_wz': 'FOREIGN KEY(fk_wz) REFERENCES wz(wz) ON DELETE CASCADE ON UPDATE CASCADE'
}
material_list_device_list_relationship_sql_col_dict = {
    'fk_material_list': 'BIGINT NULL',
    'fk_device_list': 'BIGINT NULL'
}
material_list_device_list_relationship_fk_sql_col_dict = {
    'CONSTRAINT fk_material_list': 'FOREIGN KEY(fk_material_list) REFERENCES material_list(material_list) ON DELETE '
                                   'CASCADE ON UPDATE CASCADE',
    'CONSTRAINT fk_device_list': 'FOREIGN KEY(fk_device_list) REFERENCES device_list(device_list) ON DELETE '
                                 'CASCADE ON UPDATE CASCADE'
}

material_list_leftover_sql_col_dict = {
    'project': 'VARCHAR(25)',
    'order_id': 'VARCHAR(100)',
    'bg_set': 'VARCHAR(8)',
    'group_mask': 'VARCHAR(255)',
    'should_be_included': 'VARCHAR(10)',
    'leftover_Acomp': 'VARCHAR(100)',
    'stadler_id': 'VARCHAR(50)'
}

# ////////////// Struct/WZ
wz_staps_sql_col_dict = {
    'level': 'INTEGER',
    'wz_quantity': 'FLOAT',
    'wz_quantity_tree': 'FLOAT',
    'wz_header': 'VARCHAR(255)',
    'unit': 'VARCHAR(50)',
    'material_group': 'VARCHAR(50)',
    'stadler_id': 'VARCHAR(50)',
    'revision': 'VARCHAR(20)',
    'description_1': 'VARCHAR(255)',
    'description_2': 'VARCHAR(500)',
    'description_3': 'VARCHAR(500)',
    'comment': 'VARCHAR(500)',
    'drawing_id': 'VARCHAR(50)',
    'drawing_revision': 'VARCHAR(50)',
    'viewer_link': 'VARCHAR(255)',
    'purchased': 'VARCHAR(50)',
    'specification_ready': 'VARCHAR(50)',
    'released_to_production': 'VARCHAR(50)',
    'sort': 'INTEGER',
    'sort_1': 'INTEGER',
    'breadcrumb': 'VARCHAR(255)',
    'wz_material_category_1': 'VARCHAR(255)',
    'wz_quantity_tree_total': 'FLOAT',
    'supplier': 'VARCHAR(100)',
    'supplier_id': 'VARCHAR(100)',
    'wz_material_category_2': 'VARCHAR(50)',
    'bg_general': 'VARCHAR(50)',
    'lvl1': 'VARCHAR(255)',
    'lvl2': 'VARCHAR(255)',
    'lvl3': 'VARCHAR(255)',
    'project': 'VARCHAR(50)',
    'car': 'VARCHAR(50)',
    'car_stadler_id': 'VARCHAR(255)',
    'fk_bossard_kanban_staps': 'INTEGER NULL',
    'fk_ktl_kanban_staps': 'INTEGER NULL',
    'fk_ktl_kanban_stag': 'INTEGER NULL',
    'fk_device_list': 'INTEGER NULL', #no relation only for check
    'fk_avz': 'INTEGER NULL', #no relation only for check
    'fk_material_list': 'INTEGER NULL' #no relation only for check
}

# /////////////////// KTL/KANBAN
ktl_staps_sql_col_dict = {
    'category': 'VARCHAR(100)',
    'description_pl': 'VARCHAR(255)',
    'stadler_id': 'VARCHAR(255)',
    'sp_id': 'VARCHAR(100)',
    'supplier_id': 'VARCHAR(100)',
    'supplier': 'VARCHAR(100)',
    'description_de': 'VARCHAR(255)',
    'description': 'VARCHAR(255)',
    'unit': 'VARCHAR(16)',
    'type': 'VARCHAR(100)',
    'bg': 'VARCHAR(26)'
}
ktl_stag_sql_col_dict = {
    'stadler_id': 'VARCHAR(100)',
    'src': 'VARCHAR(100)'
}

# /////////////////// BOSSARD
bossard_price_sql_short_col_dict = {
    'stadler_id': 'VARCHAR(50)',
    'prc_1_pln': 'FLOAT',
    'fk_bossard_kanban_staps': 'INTEGER NULL'
}
bossard_price_fk_sql_col_dict = {
    'CONSTRAINT fk_bossard_kanban_staps': 'FOREIGN KEY(fk_bossard_kanban_staps) REFERENCES bossard_kanban_staps('
                                          'bossard_kanban_staps) ON DELETE SET NULL ON UPDATE CASCADE',
}
bossard_sql_short_col_dict = {
    'site': 'VARCHAR(100)',
    'status': 'VARCHAR(100)',
    'bossard_group': 'VARCHAR(100)',
    'location': 'VARCHAR(100)',
    'stadler_id': 'VARCHAR(50)',
    'description_1': 'VARCHAR(255)',
    'description_2': 'VARCHAR(255)',
    'part_type': 'VARCHAR(255)',
    'supplier': 'VARCHAR(100)',
    'supplier_id': 'VARCHAR(50)'
}

# ////////////////// KABEL
cable_data_sql_col_dict = {
    'stadler_id': 'VARCHAR(100)',
    'stadler_id_supplier': 'VARCHAR(100)',
    'x_section_mm2': 'VARCHAR(100)',
    'type': 'VARCHAR(100)',
    'supplier': 'VARCHAR(100)',
    'description': 'VARCHAR(255)',
    'description_2': 'VARCHAR(255)',
}
cable_quantity_sql_col_dict = {
    'stadler_id': 'VARCHAR(100)',
    'project': 'VARCHAR(100)',
    'sum_m': 'BIGINT'
}
cable_relationship_sql_col_dict = {
    'fk_cable_quantity': 'INTEGER NULL',
    'fk_cable_data': 'INTEGER NULL'
}
cable_relationship_fk_sql_col_dict = {
    'CONSTRAINT fk_cable_quantity': 'FOREIGN KEY(fk_cable_quantity) REFERENCES cable_quantity(cable_quantity) ON '
                                    'DELETE SET NULL ON UPDATE CASCADE',
    'CONSTRAINT fk_cable_data': 'FOREIGN KEY(fk_cable_data) REFERENCES cable_data(cable_data) ON DELETE SET NULL ON '
                                'UPDATE CASCADE'
}

# ///////////////// APPARATELISTE
device_list_sql_col_dict = {
    'project': 'VARCHAR(50)',
    'schematic_position': 'VARCHAR(50)',
    'h_u': 'VARCHAR(100)',
    'stk_a': 'FLOAT',
    'stk_b': 'FLOAT',
    'stk_c': 'FLOAT',
    'stk_d': 'FLOAT',
    'stk_e': 'FLOAT',
    'stk_f': 'FLOAT',
    'stk_g': 'FLOAT',
    'stk_h': 'FLOAT',
    'stk_i': 'FLOAT',
    'stk_j': 'FLOAT',
    'stk_k': 'FLOAT',
    'stk_l': 'FLOAT',
    'stk_m': 'FLOAT',
    'stk_n': 'FLOAT',
    'stk_o': 'FLOAT',
    'stk_pp': 'FLOAT',
    'stk_sum': 'FLOAT',
    'bg': 'VARCHAR(100)',
    'din_1': 'VARCHAR(1)',
    'din_2': 'VARCHAR(1)',
    'group_mask': 'VARCHAR(100)',
    'description_1': 'VARCHAR(500)',
    'description_2': 'VARCHAR(500)',
    'type': 'VARCHAR(255)',
    'supplier_id': 'VARCHAR(255)',
    'supplier': 'VARCHAR(100)',
    'car_area': 'VARCHAR(500)',  # or divide into separate table with car's
    'schematic': 'VARCHAR(255)',
    'comment': 'VARCHAR(255)',
    'stadler_id': 'VARCHAR(100)',
    'status': 'VARCHAR(100)',
    'person_responsible': 'VARCHAR(100)',
    'fk_bossard_prc': 'INTEGER NULL',
    'fk_bossard_kanban_staps': 'INTEGER NULL',
    'fk_ktl_kanban_staps': 'INTEGER NULL',
    'fk_ktl_kanban_stag': 'INTEGER NULL',
    'fk_wz': 'INTEGER NULL', #no relation only for check
    'fk_material_list': 'INTEGER NULL' #no relation only for check
}
device_list_sql_col_fk_dict = {
    'CONSTRAINT fk_bossard_prc': 'FOREIGN KEY(fk_bossard_prc) REFERENCES bossard_price_staps(bossard_price_staps) ON '
                                 'DELETE SET NULL ON UPDATE CASCADE',
    'CONSTRAINT fk_bossard_kanban_staps': 'FOREIGN KEY(fk_bossard_kanban_staps) REFERENCES bossard_kanban_staps('
                                          'bossard_kanban_staps) ON DELETE SET NULL ON UPDATE CASCADE',
    'CONSTRAINT fk_ktl_kanban_staps': 'FOREIGN KEY(fk_ktl_kanban_staps) REFERENCES ktl_kanban_staps(ktl_kanban_staps) '
                                      'ON DELETE SET NULL ON UPDATE CASCADE',
    'CONSTRAINT fk_ktl_kanban_stag': 'FOREIGN KEY(fk_ktl_kanban_stag) REFERENCES ktl_kanban_stag(ktl_kanban_stag) ON '
                                     'DELETE SET NULL ON UPDATE CASCADE'
}
device_list_stapr_e3_sql_col_dict = {
    'function': 'VARCHAR(100)',
    'schematic_position': 'VARCHAR(100)',
    'h_u': 'VARCHAR(100)',
    'comment_en': 'VARCHAR(255)',
    'description_1': 'VARCHAR(255)',
    'description_2': 'VARCHAR(255)',
    'supplier_id': 'VARCHAR(100)',
    'supplier': 'VARCHAR(100)',
    'car_area': 'VARCHAR(100)',
    'stadler_id': 'VARCHAR(100)',
    'stadler_set_id': 'VARCHAR(100)',
    'quantity': 'FLOAT',
    'order': 'VARCHAR(255)',
    'status': 'VARCHAR(100)'
}

offer_base_sql_col_dict = {
    # address info
    'tender': 'VARCHAR(100)',
    'tender_name': 'VARCHAR(100)',
    'supplier': 'VARCHAR(100)',  # potential db extension
    'offer_id': 'VARCHAR(100)',
    'price': 'FLOAT',
    'currency': 'VARCHAR(10)',  # potential data for currency risk analysis
    'component_id': 'VARCHAR(100)',
    'component_description': 'VARCHAR(255)',
    # main price info
    'total_quantity': 'FLOAT',
    'lead_time_weeks': 'FLOAT',
    'transport': 'VARCHAR(15)',
    'payment_details': 'VARCHAR(255)',
    'warranty': 'VARCHAR(255)',
    'offer_valid': 'DATE',
    'price_valid': 'DATE',
    'price_formula_desc': 'VARCHAR(255)',  # empty; potential for additional offer evaluation
    # extra price info
    # 'rams_lcc_duration_weeks': 'FLOAT',
    # 'rams_lcc_price': 'FLOAT',
    # 'fai_price': 'FLOAT',
    # 'documentation_price': 'FLOAT',
    # 'certification_price': 'FLOAT',
    # 'development_price': 'FLOAT',
    # 'test_price': 'FLOAT',
    # 'homologation_price': 'FLOAT',
    # 'training_price': 'FLOAT',
    # 'other_price': 'FLOAT',
    # 'other_description': 'VARCHAR(255)',
    # dates info
    'request_date': 'DATE',
    'received_date': 'DATE',
    'requested_by': 'VARCHAR(100)',  # potential db extension
    'supplied_by': 'VARCHAR(100)',  # potential db extension
}
