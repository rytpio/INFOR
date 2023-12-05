import pandas as pd
from dicts_n_lists import reference_map
from SQL import general_sql


def material_list(project: str, standard: str):
    table_name = 'materialliste'
    path = reference_map.file_path_dicts.get(table_name)
    columns = reference_map.sql_col.get(table_name)
    fk_columns = reference_map.sql_fk_col.get(table_name)

    #general_sql.drop_table(table_name)
    #general_sql.create_table(table_name, table_name, columns | fk_columns)

    # df = import_Infor.import_infor_data(standard, path)
    # df.to_excel(r'C:\Users\rytpio\Desktop\Projekty bieżące\4423_TEST\other_data\4423_material_all.xlsx', index=None)
    df = pd.read_excel(r'C:\Users\rytpio\Desktop\Projekty bieżące\MATLIST\4423_material_exploded_all.xlsx')
    # for col in col_complete_list:
    #     if col not in df.columns.tolist():
    #         sql_col_type = source_dicts.sql_col[table_name].get(col)
    #         if sql_col_type.upper() == 'FLOAT':
    #             df[col] = 0.0
    #         elif sql_col_type.upper() == 'INTEGER' or 'BIGINT':
    #             df[col] = 0
    #         else:
    #             df[col] = ''

    df_bossard_prc = general_sql.get_table_col('bossard_price_staps',
                                               ['id'] + list(reference_map.sql_col.get('bossard_price_staps').keys()))
    df_bossard_kanban_staps = general_sql.get_table_col('bossard_kanban_staps', ['id'] + list(
        reference_map.sql_col.get('bossard_kanban_staps').keys()))
    df_ktl_kanban_staps = general_sql.get_table_col('ktl_kanban_staps',
                                                    ['id'] + list(reference_map.sql_col.get('ktl_kanban_staps').keys()))
    # DOTO: WHERE projects=projects
    df_ktl_kanban_stag = general_sql.get_table_col('ktl_kanban_stag',
                                                   ['id'] + list(reference_map.sql_col.get('ktl_kanban_stag').keys()))

    df_kabel_quantity = general_sql.get_table_col_condition('kabel_quantity',
                                                            ['id'] + list(
                                                                reference_map.sql_col.get('kabel_quantity').keys()),
                                                            'project', project)
    # DOTO:WHERE projects=projects

    # DOTO: SQL Zrzut na pojazdy z pełnymi danymi
    # DOTO: SQL Wygrzebanie chemii i zrzut
    # DOTO: SQL Wygrzebanie norm i zrzut
    # DOTO: SQL Szacowane NRC i zrzut
    # DOTO: SQL Wyrzucenie nieprzypisanych grouppositions do przypisania
    # DOTO: SQL Wygrzebanie i zrzut całego fit-mat bossard
    # DOTO: SQL Wygrzebanie i zrzut KTL
    # DOTO: SQL Wygrzebanie i zrzut KTL/Kanban i Bossard - grupowych księgowań na c-mat
    # DOTO: SQL Wygrzebanie BMEB, AMEB i innych niestandardowych - do analizy %
    # DOTO: SQL Zrzut nieprzypisanych pozycji do listy aparatów
    # DOTO: SQL Zrzut nieprzypisanych pozyjci do listy AVZ
    # DOTO: SQL Zrzut komponentów na projekty
    # DOTO: SQL Zrzut dostawców i ich zamówień
    # DOTO: SQL Zrzut komponentów i ich zamówień
    # DOTO: SQL Scalenie i zrzut całego BOM na "projekt"

    # DOTO: Wrzucenie pozostałych projektów robionych w STAPS
    # DOTO: Wrzucenie projektu STAG - BLS; próba dostosowania systemu do projektów STAG
    # DOTO: Zaludnienie projektami STAG - potrzebna informacja o koncepcji każdego projektu i jego rozbicia w INFOR
    # DOTO: Wrzucenie projektu STAR; próba dostosowania systemu do projektów STAR
    # DOTO: Zaludnienie projektami STAR

    # Cel - narzędzie do lepszego wyszukiwania i klasyfikacji historycznych zamówień pomiędzy konceptami - największy minus to brak 3D
    # Drugi cel - narzędzie do lepszego klasyfikowania zebranych ofert i rozsyłania zapytań (baza dostawców, baza komponentów, baza specyfikacji)
    # Drugi cel wiekszy - wymaga zbudowania NDA, baza dostawców juz jest, baza specyfikacji wymaga załączników i opisów(najwięcej pracy - klasyfikacja dla wyznaczenia podobieństw)


    df['fk_bossard_kanban_staps'] = df['mnr'].apply(lambda x: general_sql.one_step_fk(df_bossard_kanban_staps, 'stadler_id', x))
    df['fk_ktl_kanban_staps'] = df['mnr'].apply(lambda x: general_sql.one_step_fk(df_ktl_kanban_staps, 'stadler_id', x))
    df['fk_ktl_kanban_stag'] = df['mnr'].apply(lambda x: general_sql.one_step_fk(df_ktl_kanban_stag, 'stadler_id', x))
    df['fk_kabel_quantity'] = df['mnr'].apply(lambda x: general_sql.one_step_fk(df_kabel_quantity, 'stadler_id', x))

    # jak połączyc inaczej niz po stadler_id -> stadler_id -> dla WZ potrzebna WZ.. - jak określić ?
    # to samo z AVZ; potrzeba stadler_id_pojazd - > stadler_id_pojazd_breadcrumb? --jest wiele breadcrumb

    # !!!!!!!!!!!!masterlista
    # +materiallista z odjętymi sztukami z AVZ, zamówieniami bossard i kanban/ktl(do weryfikacji czy sumy się pokrywają ilość*pojazd a infor)
    # z odjętymi kablami(do weryfikacji czy sumy się pokrywają ilość*pojazd a infor)z odjętą listą aparatów(do weryfikacji które pozycje się rozjeźdżają)
    # +pozycje AVZ, bez apparatelisty, kabli (mechanika komponenty i ich bossard)
    # +kanban_ktl-ilości * ceny
    # +kable_quantity * ceny
    # +lista aparatów z odjetymi kablami, z odjętym KTL\Kanban * ceny
    # +elementy wysocepowtarzalne(fit mat poza bossard i kanban)-ilość * ceny
    # +chemia-ilości * ceny

    ## kontrola długosci poszczególnych VARCHAR // NIE - używać TEXT zamiast VARCHAR
    # df_len = df.applymap(lambda x: 'NOTOK' if len(str(x)) > 255 else 'OK')
    # df_len.to_excel(r'C:\Users\rytpio\Desktop\Projekty bieżące\4423_TEST\other_data\apcheck.xlsx',index=False)

    # general_sql.drop_table_content(table_name)  # usun stare wpisy
    general_sql.insert_into_table(table_name, df, columns)

    general_sql.get_table(table_name)

material_list("4423", "STAPS")