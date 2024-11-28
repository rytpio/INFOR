from dicts_n_lists import ref_lists
from SQL import general_sql
import pandas as pd

def update_group_mask(project, link):
    #open matlist_after_update
    #stadler_id
    #get mask, - insert into db

    db = pd.read_excel(link, na_values='')
    db = db[['order_id', 'stadler_id', 'dev_mask', 'avz_mask', 'leftover_mask', 'group_mask']]
    db = db.drop_duplicates(['order_id', 'stadler_id'])
    db = db.applymap(lambda x: '' if str(x) == 'nan' else x)

    i = 0
    for row in db.itertuples():

        query = (f"UPDATE material_list SET "
                 f"dev_mask = '{row.dev_mask}', avz_mask = '{row.avz_mask}',"
                 f"leftover_mask = '{row.leftover_mask}', group_mask = '{row.group_mask}' "
                 f"WHERE material_list.project = '{project}' and "
                 f"order_id = '{row.order_id}' and stadler_id = '{row.stadler_id}'")
        general_sql.run_query_set(query)
        i += 1
        print(f"{i} of {db.shape[0]}")

link = r'C:\Users\rytpio\Desktop\Projekty bieżące\DATA\MATERIAL_LIST_LEFTOVER\df_matlist_5_4541.xlsx'
project = '4541'
update_group_mask(project, link)
