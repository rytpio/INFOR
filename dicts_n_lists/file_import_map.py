#   ///////////////// WZ / Struct ?
wz_col_dict_STAG = {
    'Unnamed:  0': 'U1',
    'Level': 'level',
    'Struktur.Menge': 'wz_quantity',
    'Menge Total': 'wz_quantity_tree',
    'S2ktxt': 'wz_header',
    'Einheit': 'unit',
    'Satzart': 'material_group',
    'Mnr Path': 'breadcrumb',
    'Output': 'wz_material_category',
    'pos': 'stadler_id',
    'Baugruppe': 'bg_general',  # missing col in STAPS
    'Matlistelink': 'matlistelink',  # removed
    'Revision': 'revision',  # removed
    'Struktur.Ktxt': 'description_1',
    'Kurztext 2': 'description_2',
    'Kurztext 3': 'description_3',
    'Bemerkung': 'comment',
    'Dokucode': 'dokucode',  # removed
    'ZeichnNr': 'drawing_id',
    'Zchlink': 'zchlink',  # removed
    'ZeichIndex': 'drawing_revision',
    'Kistersviewerlink': 'viewer_link',
    'ArtRL': 'art_rl',  # removed
    'Rlnr': 'rlnr',  # removed
    'Status5': 'status5',  # removed
    'Handl': 'handl',  # removed
    'Einkauf': 'purchased',
    'Eigenfertigung': 'specification_ready',
    'Statustechnik': 'released_to_production',
    'Freigabe': 'freigabe',  # removed
    'Cadposnr': 'cad_pos_nr',  # TODO: Implement category if correct stk. list number
    'Sort': 'sort',
    'Zyklus': 'zyklus',  # removed
    'Sort.1': 'sort_1',  # no _1 in STAPS
    'Mnr Path.1': 'breadcrumb_2',  # no _1 in STAPS
    'Output.1': 'output_1',  # no _1 in STAPS # removed
    'bestellt gesamt': 'bestellt_gesamt',  # removed
    'Bestand': 'bestand',  # removed
    'Lieferant nächster': 'lieferant_nachster',  # removed
    'Termin nächster': 'termin_nachster',  # removed
    'Menge nächste': 'menge_nachste',  # removed
    'BestelltAlterIndex': 'bestelltalterindex',  # removed
    'MengGrobEink': 'menggrobeink',  # removed
    'MengBestVor': 'meng_best_vor',  # removed
    'MengeInStrukt': 'wz_quantity_tree_total',
    'Hersteller': 'supplier',
    'Hersteller ArtNr': 'supplier_id',
    'STS Gruppe': 'wz_material_category_2',
    'Attrib01': 'attrib01',  # removed
    'Farbkennung Master': 'farbkennung_master',  # removed
    'Menge bestellt farbneutral': 'menge_bestellt_farbneutral',  # removed
    'Bestand farbneutral': 'bestand_farbneutral',  # removed
    'Buffer': 'buffer',  # removed
    'Bestellmengebuffer': 'bestellmengebuffer',  # removed
    'BestandBuffer': 'bestandbuffer',  # removed
    'In Änderung': 'in_anderung',  # removed
    'ManPos': 'manpos',  # removed
    'Vorgänger': 'vorganger',  # removed
    'Mod Revision': 'mod_revision',  # removed
    'Baugruppe.1': 'baugruppe_1',  # no _1 in STAPS  # removed
    'Schluessel': 'schluessel'  # removed
}
wz_col_dict_STAPS = {
    'Unnamed:  0': 'U1',  # removed
    'Level': 'level',
    'Struktur.Menge': 'wz_quantity',
    'Menge Total': 'wz_quantity_tree',
    'S2ktxt': 'wz_header',
    'Einheit': 'unit',
    'Satzart': 'material_group',
    'Mnr Path': 'breadcrumb',
    'Output': 'wz_material_category_1',
    'pos': 'stadler_id',
    # 'Baugruppe': 'baugruppe',
    'Matlistelink': 'matlistelink',  # removed
    'Revision': 'revision',  # removed
    'Struktur.Ktxt': 'description_1',
    'Kurztext 2': 'description_2',
    'Kurztext 3': 'description_3',
    'Bemerkung': 'comment',
    'Dokucode': 'dokucode',  # removed
    'ZeichnNr': 'drawing_id',
    'Zchlink': 'zchlink',  # removed
    'ZeichIndex': 'drawing_revision',
    'Kistersviewerlink': 'viewer_link',
    'ArtRL': 'art_rl',  # removed
    'Rlnr': 'rlnr',  # removed
    'Status5': 'status5',  # removed
    'Handl': 'handl',  # removed
    'Einkauf': 'purchased',
    'Eigenfertigung': 'specification_ready',
    'Statustechnik': 'released_to_production',
    'Freigabe': 'freigabe',  # removed
    'Cadposnr': 'cad_pos_nr',  # TODO: Implement category if true
    'Sort': 'sort',
    'Zyklus': 'zyklus',  # removed
    'Sort.1': 'sort_1',  # no _1 in STAPS
    'bestellt gesamt': 'bestellt_gesamt',
    'Bestand': 'bestand',  # removed
    'Lieferant nächster': 'lieferant_nachster',  # removed
    'Termin nächster': 'termin_nachster',  # removed
    'Menge nächste': 'menge_nachste',  # removed
    'BestelltAlterIndex': 'bestelltalterindex',  # removed
    'MengGrobEink': 'menggrobeink',  # removed
    'MengBestVor': 'meng_best_vor',  # removed
    'MengeInStrukt': 'wz_quantity_tree_total',
    'Hersteller': 'supplier',
    'Hersteller ArtNr': 'supplier_id',
    'STS Gruppe': 'wz_material_category_2',
    'Attrib01': 'attrib01',  # removed
    'Farbkennung Master': 'farbkennung_master',
    'Menge bestellt farbneutral': 'menge_bestellt_farbneutral',
    'Bestand farbneutral': 'bestand_farbneutral',
    'Buffer': 'buffer',
    'Bestellmengebuffer': 'bestellmengebuffer',
    'BestandBuffer': 'bestandbuffer',
    'In Änderung': 'in_anderung',
    'ManPos': 'manpos',
    'Vorgänger': 'vorganger',
    'Mod Revision': 'mod_revision',
    'Baugruppe': 'bg_general',  # no _1 in STAPS
    'Schluessel': 'schluessel'
}
wz_col_short_list_STAPS = [
    'level',
    'wz_quantity',
    'wz_quantity_tree',
    'wz_header',
    'unit',
    'material_group',
    'wz_material_category_1',
    'stadler_id',
    'bg_general',
    'revision',
    'description_1',
    'description_2',
    'description_3',
    'comment',
    'drawing_id',
    'drawing_revision',
    'viewer_link',
    'purchased',
    'specification_ready',
    'released_to_production',
    'sort',
    'sort_1',
    'breadcrumb',
    'wz_quantity_tree_total',
    'supplier',
    'supplier_id',
    'wz_material_category_2',
]

#   ///////////////////// INFOR
order_list = [
    'BMEB', 'BEM', 'BM',
    'OOEB', 'OPEB', 'OMEB',
    'AZEB', 'HUB', 'HUEB', 'SUEB', 'AR00', 'TEC'
    # 'EFEB'-?, 'RBEB'-?, #AZEB(rozliczenie firm out, akord?);
    # OOEB, (podmontaże EVM, drobne czynnosci EEM - outsourcing?),
    # OPEB(montaże EVM, podmontaże - produkcyjne) ,
    # OMEB -(montaże EVM, podmontaże - materiałowe)
    # AMEB-zamówienia pod zmianę, mogą uwzględniać też brakujacy material wstecz oraz byc zamówieniami w przód;
    # nie jest rozbite jako AMEB-wstecz i obecnie; zmiany w przód-normalne zamówienie
    # ADIF-przypadek, kiedy braki z nomrlanego zamówienia zostały chyba domówione pod OMEB
    # -prawdopodobnie, żeby przenieść koszty budżetowe; potencjalne ryzyko omijania pozycji
    # RBEB-wyjaśnic z zakupami
]
infor_col_dict_US = {  # single
    'Load Date': 'info_date',  # ?
    'Archivestatus': 'archiv_status',  # ?
    'Herkunft': 'herkunft',  # ?

    'Bestellung': 'order_id',
    'Rahmenvertrag': 'beleg_nr_abruf',  # removed
    'Lieferantnr': 'supplier_name_id',
    'Extktxt': 'supplier',
    'Komm': 'project',
    'Epos': 'bg_detail',
    'Kst': 'kst',  # removed
    'Mnr': 'stadler_id',
    'Ktxt': 'description_1',
    'Segm3 Meng': 'order_quantity',
    'Me': 'unit',
    'Segm3 Term': 'order_delivery_date',
    'Netto2': 'netto2',  # removed
    'We': 'currency',
    'Brutto': 'brutto',  # removed
    'Status4': 'status4',  # removed
    'Lager': 'lager',  # removed
    'Zdesc': 'order_status',
    'Sachbearbeiter': 'buyer',
    'Inlkto': 'bg_general',
    'Rnr': 'rnr',  # removed
    'Status1': 'status1',  # removed
    'Acppart Preis': 'unit_price',
    'F Preisbasis': 'unit_price_basis',
    'Addname1': 'supplier_id',
    'Extartnr': 'supplier_description_1',
    'Createdate': 'order_create_date',
    'Usbemerkung 4': 'supplier_country',
    'Usbemerkung 5': 'usbemerkung_5',  # removed
    'Fzvon': 'fz_start',
    'Fzbis': 'fz_end',
    'Num2': 'num2',  # removed
    'Usrealfield1': 'usrealfield1',  # removed
    'Saint': 'saint',  # removed
    'Lfdnr': 'lfdnr'  # removed
}
infor_col_dict_STAG = {
    'Belegnrbest': 'order_id',
    'Belegnrabruf': 'beleg_nr_abruf',  # removed
    'Utnr': 'supplier_name_id',
    'Extktxt': 'supplier',
    'Komm': 'project',
    'Epos': 'bg_detail',
    'Kst': 'kst',  # removed
    'Mnr': 'stadler_id',
    'Ktxt': 'description_1',
    'Segm3 Meng': 'order_quantity',
    'Me': 'unit',
    'Segm3 Term': 'order_delivery_date',
    'Netto2': 'netto2',  # removed
    'We': 'currency',
    'Brutto': 'brutto',  # removed
    'Status4': 'status4',  # removed
    'Lager': 'lager',  # removed
    'Zdesc': 'order_status',
    'Sachbearbeiter': 'buyer',
    'Inlkto': 'bg_general',
    'Rnr': 'rnr',  # removed
    'Status1': 'status1',  # removed
    'Acppart Preis': 'unit_price',
    'F Preisbasis': 'unit_price_basis',
    'Addname1': 'supplier_id',
    'Extartnr': 'supplier_description_1',
    'Createdate': 'order_create_date',
    'Usbemerkung 4': 'supplier_country',
    'Usbemerkung 5': 'usbemerkung_5',  # removed
    'Fzvon': 'fz_start',
    'Fzbis': 'fz_end',
    'Num2': 'num2',  # removed
    'Usrealfield1': 'usrealfield1',  # removed
    'Saint': 'saint',  # removed
    'Lfdnr': 'lfdnr'  # removed
}
infor_col_dict_STAPS = {
    'Beleg Nr Best': 'order_id',
    'Beleg Nr Abruf': 'beleg_nr_abruf',  # removed
    'Lieferanten Nr': 'supplier_name_id',
    'Lieferant': 'supplier',
    'Komm': 'project',
    'Baugruppe': 'bg_detail',
    'Kst': 'kst',  # removed
    'Lfdnr': 'lfd',  # STAPS column # removed
    'Mnr': 'stadler_id',
    'Ktxt': 'description_1',
    'Best Mng': 'order_quantity',
    'Gelieferte Menge': 'order_quantity_delivered',  # removed
    'Offene Menge': 'order_quantity_delivered_open',  # removed
    'Me': 'unit',
    'Termin': 'order_delivery_date',
    'Netto2': 'netto2',  # removed
    'Offener_Rechnungsbetrag_Fw': 'o_rechnungsbetrag_fw',  # STAPS column   # removed
    'We': 'currency',
    'WE Bestellwert': 'we_bestellwert',  # STAPS column   # removed
    'We Auswahl': 'we_auswahl',  # STAPS column   # removed
    # 'Brutto': 'brutto', STAG column   # removed
    'Status4': 'status4',  # removed
    'Freigabe': 'zdesc',  # STAPS column    # removed
    'Zustand': 'order_status',  # STAPS column    # removed
    # 'Lager': 'lager', STAG column
    # 'Zdesc': 'zdesc', STAG column
    'Sachbearbeiter': 'buyer',
    'Inlkto': 'bg_general',
    'Rnr': 'rnr',  # removed
    'Status1': 'status1',  # removed
    'Preis': 'unit_price',
    'F Preisbasis': 'unit_price_basis',
    'Kurztext 2': 'supplier_2',  # STAPS
    # 'Addname1': 'addname1', STAG
    'Ext Art Nr': 'supplier_id',
    'Createdate': 'order_create_date',
    'Land': 'supplier_country',
    'Kanton': 'supplier_country_region',
    # 'Usbemerkung 4': 'usbemerkung_4', STAG
    # 'Usbemerkung 5': 'usbemerkung_5', STAG
    'Fz Von': 'fz_start',
    'Fz Bis': 'fz_end',
    'Num2': 'num2',  # removed
    # 'Usrealfield1': 'usrealfield1', STAG   # removed
    'Saint': 'saint',  # removed
    'LBC': 'lbc',  # removed
    'Lieferbedingung': 'lieferbedingung',  # removed
    'Zahlungsbedingung': 'zahlungsbedingung',  # removed
    'Bemerkung': 'comment',
    'Herstellerinfo': 'herstellerinfo',  # removed
    'Usbemerkung 1 Pos': 'usbemerkung1pos'  # removed
    # 'Lfdnr': 'lfdnr' STAG; w innej kolejnosci kolumn
}
infor_col_dict_STAPS_single = {
    'Load Date': 'to_remove1',
    'Bestellung': 'order_id',
    'Rahmenvertrag': 'beleg_nr_abruf',  # removed
    'Lieferantnr': 'supplier_name_id',
    'Lieferant': 'supplier',
    'Komm': 'project',
    'Epos Num': 'bg_detail',
    'Kst': 'kst',  # removed
    'Artikelnr': 'stadler_id',
    'Artikel': 'description_1',
    'Bestellmenge': 'order_quantity',
    'Mengeneinheit': 'unit',
    'Gelieferte Menge': 'order_quantity_delivered',  # removed
    'Offene Menge': 'order_quantity_open',  # removed
    'Lieferdatum': 'order_delivery_date',
    'Kopfrabatt': 'to_remove2',  # removed
    'Bestellpos Netto0': 'netto0',  # removed
    'Bestellpos Netto2 ber': 'netto2',  # removed
    'Waehrung': 'currency',
    'Freigabe': 'order_status',
    'Konsi': 'to_remove3',  # removed
    'Status': 'zustand',  # removed
    'Sachbearbeiter': 'buyer',
    'Konto Inl': 'bg_general',
    'Pos': 'rnr',  # removed
    'Auftragsbest Verlangt': 'to_remove4',  # removed
    'Einzelteilpreis': 'unit_price',
    'Einzelteilbasis': 'unit_price_basis',
    'Basis': 'basis',  # removed
    'Ktxt2 Stamm': 'supplier_id',
    'Fremdartnr': 'supplier_description_1',
    'Erstbestelldatum': 'order_create_date',
    'Land': 'supplier_country',
    'Kanton': 'supplier_country_region',
    'Fahrzeug Von': 'fz_start',
    'Fahrzeug Bis': 'fz_end',
    'Satzart Ext Eb': 'material_group',  # STAPS_single #NRC=Z; zwykły=H, M
    # 'Usrealfield1': 'usrealfield1', STAG
    'Anr': 'to_remove5',  # removed
    'Bestaetigung': 'to_remove6',  # removed
    'Diff': 'to_remove7',  # removed
    'Usbemerkung 1 Pos': 'to_remove8',  # removed
    'Bemerkung': 'comment',
}
infor_col_list_short = [
    'project',
    'order_id',
    'order_status',
    'order_create_date',
    'order_delivery_date',

    'stadler_id',
    'description_1',
    'supplier_id',
    'supplier_description_1',

    'order_quantity',
    'unit',

    'unit_price',
    'unit_price_basis',
    'currency',

    'supplier_name_id',
    'supplier',
    'supplier_country',
    'buyer',

    'bg_detail',
    'bg_general',

    'fz_start',
    'fz_end'

]

# //////////////////////// AVZ
avz_col_dict = {
    'Reihe': 'avz_struct_index',
    'Ebene': 'level',
    'Din En': 'din',
    'Mengeneinheit': 'unit',
    'Anzahl': 'quantity',
    'Artikelnummer': 'stadler_id',
    'Artikel Revision': 'article_rev',
    'Pos Nr': 'position_number',
    'Artikel Benennung 1': 'description_1',
    'Artikel Benennung 2': 'description_2',
    'Werkstoff': 'material',
    'Werkstoff Neu': 'material_new',
    'Artikel Status': 'article_status',
    'Artikel Freigeber': 'article_approved_by',
    'Artikel Freigabe': 'article_approved',
    'Dokument': 'document',
    'Dokument Nr': 'document_nr',
    'Pos Etz': 'position_etz',
    'Dok Revision': 'doc_revision',
    'Dok Status': 'doc_status',
    'Dok Freigeber': 'doc_approved_by',
    'Dok Freigabe': 'doc_approved',
    'Schweissfreigeber': 'schweiss_approved_by',
    'Schweissfreigabe': 'schweiss_approved_date',
    'Projekt Nr': 'project',
    'Projektname': 'project_name',
    'Schemapos': 'schematic_position',
    'Einbauort': 'vehicle_area',
    'Klassifizierung': 'classification',
    'Ersatzartikel': 'initial_article',
    'Rootartikel': 'root_article',
    'Rootversion': 'root_version',
    'Hersteller': 'supplier',
    'Hersteller Art Nr': 'supplier_article_id',
    'Hersteller Typ': 'supplier_type',
    'Hersteller Art Idx': 'supplier_article_idx',
    'Gewicht': 'weight',
    'Bemerkung': 'comment',
    'Dok Class Id': 'doc_class_id',
    'Dok Liefr  Nr': 'doc_supplier_nr',
    'Vertraulich': 'confidential'
}  # done
avz_col_short_list = [
    'avz_struct_index',
    'level',
    'din',
    'unit',
    'quantity',
    'stadler_id',
    'article_rev',
    'position_number',
    'description_1',
    'description_2',
    'material',
    'material_new',
    'document',
    'document_nr',
    'position_etz',
    'doc_revision',
    'doc_status',
    'project',
    'project_name',
    'schematic_position',
    'vehicle_area',
    'classification',
    'initial_article',
    'root_article',
    'root_version',
    'supplier',
    'supplier_article_id',
    'supplier_type',
    'supplier_article_idx',
    'weight',
    'comment',
    'doc_class_id',
    'doc_supplier_nr'
]  # done
avz_col_type_dict = {
    'avz_struct_index': int,
    'level': int,
    'quantity': int,
    'weight': float
}  # done
avz_pos_ranges = {
    'main_mechanic_l': 1,
    'main_mechanic_h': 199,
    'screws_l': 200,
    'screws_h': 249,
    'nuts_l': 250,
    'nuts_h': 299,
    'washers_l': 300,
    'washers_h': 349,
    'bolts_misc_l': 350,
    'bolts_misc_h': 399,
    'hoses_pneumatic_l': 400,
    'hoses_pneumatic_h': 449,
    'chemicals_l': 450,
    'chemicals_h': 499,
    'struct_pneumatic_l': 500,
    'struct_pneumatic_h': 599,
    'main_pneumatic_l': 600,
    'main_pneumatic_h': 699,
    'struct_electric_l': 700,
    'struct_electric_h': 799,
    'diverse_l': 800,
    'diverse_h': 899,
    'specification_l': 900,
    'specification_h': 999,
    'main_electric_l': 1000,
    'main_electric_h': 1299,
}  # acc. to BU_1951939

# ////////////////////// KTL/Kanban
ktl_short_col_dict = {
    'KATEGORIA': 'category',
    'NAZWA ARTYKUŁU': 'description_pl',
    'NUMER MAFII': 'stadler_id',
    'NUMER SP': 'sp_id',
    'NUMER DOSTAWCY': 'supplier_id',
    'DOSTAWCA': 'supplier',
    'OPIS': 'description_de',
    'WYMIARY': 'description',
    'JEDNOSTKA': 'unit',
    'RODZAJ MATERIAŁU': 'type',
    'BG': 'bg'
}

# ////////////////////// Bossard
bossard_col_dict = {
    'site': 'site',
    'project': 'project',
    'group': 'group',
    'location': 'location',
    'phys__addr_': 'phys__addr_',
    'cust_item_no_': 'cust_item_no_',
    'description': 'description',
    'dimension': 'dimension',
    'part_type': 'part_type',
    'delivery_date': 'delivery_date',
    'order_state': 'order_state',
    'priority': 'priority',
    'order_qty': 'order_qty',
    'stock': 'stock',
    'stock_in_days': 'stock_in_days',
    'error': 'error',
    'active': 'active',
    'item_rp': 'item_rp',
    'item_expr_rp': 'item_expr_rp',
    'item_rqty': 'item_rqty',
    'yearly_u_': 'yearly_u_',
    'supplier': 'supplier',
    'box_type': 'box_type',
    'bin_no_': 'bin_no_',
    'box_weight': 'box_weight',
    'ø_value_rqty': 'ø_value_rqty',
    'remove_on': 'remove_on',
    'remaining_qty': 'remaining_qty',
    'last_weighted': 'last_weighted'
}
bossard_short_col_dict = {
    'site': 'site',
    'project': 'status',
    'group': 'bossard_group',
    'location': 'location',
    'cust_item_no_': 'stadler_id',
    'description': 'description_1',
    'dimension': 'description_2',
    'part_type': 'part_type',
    'supplier': 'supplier',
    'sup_item_no_': 'supplier_id',
}  # done

# ////////////////////// Apparateliste
device_list_stapr_e3_short_col_dict = {  # i tak dla kazdego projektu do stworzenia
    'E': 'function',
    'Schema Position': 'schematic_position',
    'H / U': 'h_u',
    'NameEN': 'comment_en',
    'Type': 'description_1',
    'Basic data': 'description_2',
    'Drawing Number/ Ordering Number': 'supplier_id',
    'Supplier / Manufacturer': 'supplier',
    'Location': 'car_area',
    'Stadler-ID': 'stadler_id',
    'Baugruppe': 'stadler_set_id',
    'menge': 'quantity',
    'Ordering Number': 'order',
    'State': 'status'
}  # done
device_dict_project = {
    '4473': {
        'col_change_dict': {
            'schema_position': 'schematic_position',
            'h_u': 'h_u',
            'stk_a': 'stk_a',
            'stk_b': 'stk_b',
            'stk_c': 'stk_c',
            'stk_d': 'stk_d',
            'stk_e': 'stk_e',
            'bezeichnung_deutsch': 'description_1',
            'bg': 'bg',
            'din_1': 'din_1',
            'din_2': 'din_2',
            'group_mask': 'group_mask',
            'typ': 'type',
            'nenndaten': 'description_2',
            'massbilder_bestellnummer': 'supplier_id',
            'lieferant_hersteller': 'supplier',
            'einbau_ort': 'car_area',
            'schema': 'schematic',
            'bemerkungen': 'comment',
            'stadlerid': 'stadler_id',
            'be_status': 'status',
            'verantwortlich': 'person_responsible'},
        'col_complete_list': [
            'schematic_position', 'h_u', 'stk_a', 'stk_b', 'stk_c', 'stk_d', 'stk_e', 'stk_f', 'stk_g', 'stk_h',
            'stk_i', 'stk_j', 'stk_k', 'stk_l', 'stk_m', 'stk_n', 'stk_o', 'description_1', 'bg', 'din_1', 'din_2', 'group_mask',
            'type', 'description_2', 'supplier_id', 'supplier', 'car_area',
            'schematic', 'comment', 'stadler_id', 'status', 'person_responsible'
        ],
        'col_cutout_list': [
            'schema_position', 'h_u', 'stk_a', 'stk_b', 'stk_c', 'stk_d', 'stk_e', 'bezeichnung_deutsch',
            'bg', 'din_1', 'din_2', 'group_mask', 'typ', 'nenndaten', 'massbilder_bestellnummer', 'lieferant_hersteller',
            'einbau_ort', 'schema', 'bemerkungen', 'stadlerid', 'be_status', 'verantwortlich']
    },
    '4547': {
        'col_change_dict': {
            'schema_position': 'schematic_position',
            'h_u': 'h_u',
            'stk_a': 'stk_a',
            'stk_b': 'stk_b',
            'stk_c': 'stk_c',
            'stk_d': 'stk_d',
            'bezeichnung_deutsch': 'description_1',
            'bg': 'bg',
            'din_1': 'din_1',
            'din_2': 'din_2',
            'group_mask': 'group_mask',
            'typ': 'type',
            'nenndaten': 'description_2',
            'massbilder_bestellnummer': 'supplier_id',
            'lieferant_hersteller': 'supplier',
            'einbau_ort': 'car_area',
            'schema': 'schematic',
            'bemerkungen': 'comment',
            'stadlerid': 'stadler_id',
            'be_status': 'status',
            'verantwortlich': 'person_responsible'},
        'col_complete_list': [
            'schematic_position', 'h_u', 'stk_a', 'stk_b', 'stk_c', 'stk_d', 'stk_e', 'stk_f', 'stk_g', 'stk_h',
            'stk_i', 'stk_j', 'stk_k', 'stk_l', 'stk_m', 'stk_n', 'stk_o',
            'description_1', 'bg', 'din_1', 'din_2', 'group_mask', 'type', 'description_2', 'supplier_id', 'supplier', 'car_area',
            'schematic', 'comment', 'stadler_id', 'status', 'person_responsible'
        ],
        'col_cutout_list': [
            'schema_position', 'h_u', 'stk_a', 'stk_b', 'stk_c', 'stk_d', 'bezeichnung_deutsch',
             'bg', 'din_1', 'din_2', 'group_mask', 'typ', 'nenndaten', 'massbilder_bestellnummer', 'lieferant_hersteller',
            'einbau_ort', 'schema', 'bemerkungen', 'stadlerid', 'be_status', 'verantwortlich']
    },
    '4431': {
        'col_change_dict': {
            'schema_position': 'schematic_position',
            'h_u': 'h_u',
            'stk_a': 'stk_a',
            'stk_b': 'stk_b',
            'stk_c': 'stk_c',
            'stk_d': 'stk_d',
            'bezeichnung_deutsch': 'description_1',
            'bg': 'bg',
            'din_1': 'din_1',
            'din_2': 'din_2',
            'group_mask': 'group_mask',
            'typ': 'type',
            'nenndaten': 'description_2',
            'massbilder_bestellnummer': 'supplier_id',
            'lieferant_hersteller': 'supplier',
            'einbau_ort': 'car_area',
            'schema': 'schematic',
            'bemerkungen': 'comment',
            'stadlerid': 'stadler_id',
            'be_status': 'status',
            'verantwortlich': 'person_responsible'},
        'col_complete_list': [
            'schematic_position', 'h_u', 'stk_a', 'stk_b', 'stk_c', 'stk_d', 'stk_e', 'stk_f', 'stk_g', 'stk_h',
            'stk_i', 'stk_j', 'stk_k', 'stk_l', 'stk_m', 'stk_n', 'stk_o',
            'description_1', 'bg', 'din_1', 'din_2', 'group_mask', 'type', 'description_2', 'supplier_id', 'supplier', 'car_area',
            'schematic', 'comment', 'stadler_id', 'status', 'person_responsible'
        ],
        'col_cutout_list': [
            'schema_position', 'h_u', 'stk_a', 'stk_b', 'stk_c', 'stk_d', 'bezeichnung_deutsch',
             'bg', 'din_1', 'din_2', 'group_mask', 'typ', 'nenndaten', 'massbilder_bestellnummer', 'lieferant_hersteller',
            'einbau_ort', 'schema', 'bemerkungen', 'stadlerid', 'be_status', 'verantwortlich']
    },
'4423': {
        'col_change_dict': {
            'schema_position': 'schematic_position',
            'h_u': 'h_u',
            'stk_a': 'stk_a',
            'stk_b': 'stk_b',
            'stk_c': 'stk_c',
            'stk_d': 'stk_d',
            'stk_e': 'stk_e',
            'bezeichnung_deutsch': 'description_1',
            'bg': 'bg',
            'din_1': 'din_1',
            'din_2': 'din_2',
            'group_mask': 'group_mask',
            'typ': 'type',
            'nenndaten': 'description_2',
            'massbilder_bestellnummer': 'supplier_id',
            'lieferant_hersteller': 'supplier',
            'einbau_ort': 'car_area',
            'schema': 'schematic',
            'bemerkungen': 'comment',
            'stadlerid': 'stadler_id',
            'be_status': 'status',
            'verantwortlich': 'person_responsible'},
        'col_complete_list': [
            'schematic_position', 'h_u', 'stk_a', 'stk_b', 'stk_c', 'stk_d', 'stk_e', 'stk_f', 'stk_g', 'stk_h',
            'stk_i', 'stk_j', 'stk_k', 'stk_l', 'stk_m', 'stk_n', 'stk_o',
            'description_1', 'bg', 'din_1', 'din_2', 'group_mask', 'type', 'description_2', 'supplier_id', 'supplier', 'car_area',
            'schematic', 'comment', 'stadler_id', 'status', 'person_responsible'
        ],
        'col_cutout_list': [
            'schema_position', 'h_u', 'stk_a', 'stk_b', 'stk_c', 'stk_d', 'stk_e',  'bezeichnung_deutsch',
            'bg', 'din_1', 'din_2', 'group_mask', 'typ', 'nenndaten', 'massbilder_bestellnummer', 'lieferant_hersteller',
            'einbau_ort', 'schema', 'bemerkungen', 'stadlerid', 'be_status', 'verantwortlich']
    },
'4503': {
        'col_change_dict': {
            'schema_position': 'schematic_position',
            'h_u': 'h_u',
            'stk_a': 'stk_a',
            'stk_b': 'stk_b',
            'stk_c': 'stk_c',
            'bezeichnung_deutsch': 'description_1',
            'bg': 'bg',
            'din_1': 'din_1',
            'din_2': 'din_2',
            'group_mask': 'group_mask',
            'typ': 'type',
            'nenndaten': 'description_2',
            'massbilder_bestellnummer': 'supplier_id',
            'lieferant_hersteller': 'supplier',
            'einbau_ort': 'car_area',
            'schema': 'schematic',
            'bemerkungen': 'comment',
            'stadlerid': 'stadler_id',
            'be_status': 'status',
            'verantwortlich': 'person_responsible'},
        'col_complete_list': [
            'schematic_position', 'h_u', 'stk_a', 'stk_b', 'stk_c', 'stk_d', 'stk_e', 'stk_f', 'stk_g', 'stk_h',
            'stk_i', 'stk_j', 'stk_k', 'stk_l', 'stk_m', 'stk_n', 'stk_o',
            'description_1', 'bg', 'din_1', 'din_2', 'group_mask', 'type', 'description_2', 'supplier_id', 'supplier', 'car_area',
            'schematic', 'comment', 'stadler_id', 'status', 'person_responsible'
        ],
        'col_cutout_list': [
            'schema_position', 'h_u', 'stk_a', 'stk_b', 'stk_c',  'bezeichnung_deutsch',
            'bg', 'din_1', 'din_2', 'group_mask', 'typ', 'nenndaten', 'massbilder_bestellnummer', 'lieferant_hersteller',
            'einbau_ort', 'schema', 'bemerkungen', 'stadlerid', 'be_status', 'verantwortlich']
    },
'4541': {
        'col_change_dict': {
            'schema_position': 'schematic_position',
            'h_u': 'h_u',
            'stk_a': 'stk_a',
            'stk_b': 'stk_b',
            'stk_c': 'stk_c',
            'bezeichnung_deutsch': 'description_1',
            'bg': 'bg',
            'din_1': 'din_1',
            'din_2': 'din_2',
            'group_mask': 'group_mask',
            'typ': 'type',
            'nenndaten': 'description_2',
            'massbilder_bestellnummer': 'supplier_id',
            'lieferant_hersteller': 'supplier',
            'einbau_ort': 'car_area',
            'schema': 'schematic',
            'bemerkungen': 'comment',
            'stadlerid': 'stadler_id',
            'be_status': 'status',
            'verantwortlich': 'person_responsible'},
        'col_complete_list': [
            'schematic_position', 'h_u', 'stk_a', 'stk_b', 'stk_c', 'stk_d', 'stk_e', 'stk_f', 'stk_g', 'stk_h',
            'stk_i', 'stk_j', 'stk_k', 'stk_l', 'stk_m', 'stk_n', 'stk_o',
            'description_1', 'bg', 'din_1', 'din_2', 'group_mask', 'type', 'description_2', 'supplier_id', 'supplier', 'car_area',
            'schematic', 'comment', 'stadler_id', 'status', 'person_responsible'
        ],
        'col_cutout_list': [
            'schema_position', 'h_u', 'stk_a', 'stk_b', 'stk_c',  'bezeichnung_deutsch',
            'bg', 'din_1', 'din_2', 'group_mask', 'typ', 'nenndaten', 'massbilder_bestellnummer', 'lieferant_hersteller',
            'einbau_ort', 'schema', 'bemerkungen', 'stadlerid', 'be_status', 'verantwortlich']
    },
'4556': {
        'col_change_dict': {
            'schema_position': 'schematic_position',
            'h_u': 'h_u',
            'stk_a': 'stk_a',
            'stk_b': 'stk_b',
            'stk_c': 'stk_c',
            'bezeichnung_deutsch': 'description_1',
            'bg': 'bg',
            'din_1': 'din_1',
            'din_2': 'din_2',
            'group_mask': 'group_mask',
            'typ': 'type',
            'nenndaten': 'description_2',
            'massbilder_bestellnummer': 'supplier_id',
            'lieferant_hersteller': 'supplier',
            'einbau_ort': 'car_area',
            'schema': 'schematic',
            'bemerkungen': 'comment',
            'stadlerid': 'stadler_id',
            'be_status': 'status',
            'verantwortlich': 'person_responsible'},
        'col_complete_list': [
            'schematic_position', 'h_u', 'stk_a', 'stk_b', 'stk_c', 'stk_d', 'stk_e', 'stk_f', 'stk_g', 'stk_h',
            'stk_i', 'stk_j', 'stk_k', 'stk_l', 'stk_m', 'stk_n', 'stk_o',
            'description_1', 'bg', 'din_1', 'din_2', 'group_mask', 'type', 'description_2', 'supplier_id', 'supplier', 'car_area',
            'schematic', 'comment', 'stadler_id', 'status', 'person_responsible'
        ],
        'col_cutout_list': [
            'schema_position', 'h_u', 'stk_a', 'stk_b', 'stk_c',  'bezeichnung_deutsch',
            'bg', 'din_1', 'din_2', 'group_mask', 'typ', 'nenndaten', 'massbilder_bestellnummer', 'lieferant_hersteller',
            'einbau_ort', 'schema', 'bemerkungen', 'stadlerid', 'be_status', 'verantwortlich']
    }
}

# ////////////////////// ZVZ
zvz_col_list = [
    'sent_to_the_buyer',
    'CHANGE_sent_to_the_buyer',
    'leer1',
    'ablage_gebiet',
    'BG',
    'DIN',
    'DIN_unterbaugruppe',
    'leer2',
    'stufe_1',
    'stufe_2',
    'stufe_3',
    'stufe_4',
    'stufe_5',
    'stufe_6',
    'stufe_7',
    'stufe_8',
    'stufe_9',
    'stufe_10',
    'dachl',
    'haupt_benennung',
    'zusatz_benennung',
    'stand',
    'bemerkungen',
    'mehrfachverwendung',
    # 'draw_link',
    'draw_id',
    'pos_oder_RUB',
    'draw_index',
    # 'stk_link',
    'stk_id',
    'aenderungsantrag',
    'datum',
    'aenderungsbereich',
    'B_menge',
    'C_menge',
    'A_menge',
    'total_1fz',
    '15_fz',
    'serie_freigabe15_fz',
    'projektbereich',
    'status']  # not_used
zvz_col_short_list = [
    'BG',
    'DIN',
    'DIN_unterbaugruppe',
    'haupt_benennung',
    'zusatz_benennung',
    'stand',
    'bemerkungen',
    'mehrfachverwendung',
    # 'draw_link',
    'draw_id',
    'pos_oder_RUB',
    'draw_index',
    # 'stk_link',
    'stk_id',
    'datum',
    'B_menge',
    'C_menge',
    'A_menge',
    'total_1fz',
    'serie_freigabe15_fz',
    'status',
    'car',
    'level',
    'detail',
    'breadcrumb'
]  # not_used
zvz_col_bogie_short_list = [
    'BG',
    'DIN',
    'DIN_unterbaugruppe',
    'haupt_benennung',
    #'zusatz_benennung',
    #'stand',
    'bemerkungen',
    #'mehrfachverwendung',
    # 'draw_link',
    'draw_id',
    'pos_oder_RUB',
    'draw_index',
    # 'stk_link',
    'stk_id',
    #'datum',
    'B_menge',
    'C_menge',
    'A_menge',
    'total_1fz',
    #'serie_freigabe15_fz',
    'status',
    'car',
    'level',
    'detail',
    'breadcrumb'
]  # not_used
zvz_bogie_col_list = [
    'leer1',
    'ablage_gebiet',
    'BG',
    'DIN',
    'DIN_unterbaugruppe',
    'leer2',#KRK2
    #'stufe_0',
    'stufe_1', 'stufe_2', 'stufe_3', 'stufe_4', 'stufe_5',
    'stufe_6', 'stufe_7', 'stufe_8', 'stufe_9', 'stufe_10',
    'stufe_11', 'stufe_12',
    'draw_id',
    'pos_oder_RUB',
    'stk_id',
    'haupt_benennung',
    'leer3',#KRK2
    'status',
    'bemerkungen',
    'LDG', #KRK2
    'ZG', #KRK2
    'SERIE', #KRK2
    'A_menge',
    'C_menge',
    'B_menge',
    'total_1fz',
    '58_fz',
    'A_mengev2', #KRK2
    'C_mengev2', #KRK2
    'B_mengev2', #KRK2
    'total_1fzv2', #KRK2
    '2_fzv2', #KRK2
    '60_fz',#KRK2
    'fertigungs freigegeben',
    # 'zum_bayer_geschickt',
    # 'ändern_zum_bayer_geschickt',
    'brandschutzanforderung',
    'ib',
    'aenderungsbereich',
    'draw_index',
    'draw_ändgs_nr',
    'stk_vers',
    'stk_ändgs_nr',
    'aktuelle_änderung_freigegeben'
]  # not_used
