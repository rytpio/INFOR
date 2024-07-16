from dicts_n_lists import ref_lists
from SQL import general_sql
from psycopg2 import DatabaseError



#Set everything to M as default
def set_all_to_x(table_name:str, set_col:str, set_value:str):
    conn = general_sql.connect()
    cursor = conn.cursor()
    query = f"UPDATE {table_name} SET {set_col} = '{set_value}'" + " WHERE not nrc = 'CHEMIE'"

    try:
        cursor.execute(query)
        conn.commit()
    except(Exception, DatabaseError) as error:
        print('Error: %s' % error)

def refresh_chemie():
    for x in ref_lists.chemie_ktxt:
        general_sql.update_based_on_partial_string('material_list','nrc','CHEMIE',
                                                   'description_1', x, ref_lists.chemie_ktxt_excluded)

def refresh_outsourcing():
    # for x in ref_lists.outsourcing_ktxt:
    #     general_sql.update_based_on_partial_string('material_list','nrc','OUTSOURCING',
    #                                                'description_1', x, ref_lists.outsourcing_ktxt_excluded)
    for x in ref_lists.outsourcing_companies_dict.keys():
        general_sql.update_based_on_partial_string('material_list','nrc', 'OUTSOURCING',
                                                   'supplier_name_id', str.lower(x), ref_lists.outsourcing_companies_excluded)

def refresh_nrc():
    for x in ref_lists.material_list_nrc_ktxt:
        general_sql.update_based_on_partial_string('material_list','nrc','NRC',
                                                   'description_1', x, "")

def refresh_rest():
    for x in ['koszty transport', 'fracht', 'verzoll']:
        general_sql.update_based_on_partial_string('material_list','nrc','TRANSPORT',
                                                   'description_1', x, "")
    for x in ['opakow', 'verpackung', 'skrzynie']:
        general_sql.update_based_on_partial_string('material_list','nrc','PACK',
                                                   'description_1', x, "")

    for x in ['narzędziownia']:
        general_sql.update_based_on_partial_string('material_list','nrc','TOOLS',
                                                   'description_1', x, "")

    for x in ['c-materiał']:
        general_sql.update_based_on_partial_string('material_list','nrc','KANBAN_KTL',
                                                   'description_1', x, "")
    for x in ['smartbin']:
        general_sql.update_based_on_partial_string('material_list','nrc','BOSSARD',
                                                   'description_1', x, "")

#set_all_to_x('material_list','nrc','M')
refresh_chemie()
refresh_outsourcing()
refresh_nrc()
refresh_rest()
