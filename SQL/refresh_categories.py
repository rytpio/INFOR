from dicts_n_lists import ref_lists
from SQL import general_sql
from psycopg2 import DatabaseError



#Set everything to M as default
def set_all_to_x(table_name:str, set_col:str, set_value:str, project:str):
    conn = general_sql.connect()
    cursor = conn.cursor()
    if project != '':
        query = f"UPDATE {table_name} SET {set_col} = '{set_value}'" + f" WHERE project='{project}' and not nrc='CHEMIE'"
    else:
        query = f"UPDATE {table_name} SET {set_col} = '{set_value}'" + f" WHERE not nrc='CHEMIE'"

    try:
        cursor.execute(query)
        conn.commit()
    except(Exception, DatabaseError) as error:
        print('Error: %s' % error)

def refresh_chemie(project):
    for x in ref_lists.chemie_ktxt:
        general_sql.update_based_on_partial_string('material_list','nrc','CHEMIE',
                                                   'description_1', x, ref_lists.chemie_ktxt_excluded,project)

def refresh_outsourcing(project):
    # for x in ref_lists.outsourcing_ktxt:
    #     general_sql.update_based_on_partial_string('material_list','nrc','OUTSOURCING',
    #                                                'description_1', x, ref_lists.outsourcing_ktxt_excluded)
    for x in ref_lists.outsourcing_companies_dict.keys():
        general_sql.update_based_on_partial_string('material_list','nrc', 'OUTSOURCING',
                                                   'supplier_name_id', str.lower(x), ref_lists.outsourcing_companies_excluded,project)

def refresh_nrc(project):
    for x in ref_lists.material_list_nrc_ktxt:
        general_sql.update_based_on_partial_string('material_list','nrc','NRC',
                                                   'description_1', x, "",project)

def refresh_rest(project):
    for x in ['koszty transport', 'fracht', 'verzoll']:
        general_sql.update_based_on_partial_string('material_list','nrc','TRANSPORT',
                                                   'description_1', x, "",project)
    for x in ['opakow', 'verpackung', 'skrzynie']:
        general_sql.update_based_on_partial_string('material_list','nrc','PACK',
                                                   'description_1', x, "",project)

    for x in ['narzędziownia']:
        general_sql.update_based_on_partial_string('material_list','nrc','TOOLS',
                                                   'description_1', x, "",project)

    for x in ['c-materiał']:
        general_sql.update_based_on_partial_string('material_list','nrc','KANBAN_KTL',
                                                   'description_1', x, "",project)
    for x in ['smartbin']:
        general_sql.update_based_on_partial_string('material_list','nrc','BOSSARD',
                                                   'description_1', x, "",project)

project='4541'
set_all_to_x('material_list','nrc','M',project)
refresh_chemie(project)
refresh_outsourcing(project)
refresh_nrc(project)
refresh_rest(project)
