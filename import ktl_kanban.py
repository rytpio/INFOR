import pandas as pd
import os.path
from dicts_n_lists import file_import_map
import numpy as np

#tested
def import_ktlkanban(path_ktl_kanban_list: str, path_save: str):

    df_ktl_kanban = pd.read_excel(path_ktl_kanban_list, skiprows=2)

    #[ktl_kanban_col_list.append(col) for col in df_ktl_kanban.columns if "L-" in col]  # dodaj kolumny projektów
    #project_series = [df_ktl_kanban[col] for col in df_ktl_kanban.columns if "L-" in col]
    #series_names = [col for col in df_ktl_kanban.columns if "L-" in col]
    df_ktl_kanban.columns = [str(x).replace("\n", "").strip() for x in df_ktl_kanban.columns]
    df_ktl_kanban = df_ktl_kanban[file_import_map.ktl_short_col_dict.keys()]
    df_ktl_kanban.rename(mapper=file_import_map.ktl_short_col_dict, inplace=True, axis=1)
    df_ktl_kanban = df_ktl_kanban[df_ktl_kanban['stadler_id'].apply(lambda x: isinstance(x, (int, np.int64)))]
    # df_flattened = pd.DataFrame()
    # for name in series_names:
    #     df_ktl_kanban['menge'] = project_series[series_names.index(name)]
    #     df_ktl_kanban['auftrag'] = name
    #     df_flattened = pd.concat(objs=[df_flattened, df_ktl_kanban.dropna(subset='menge', inplace=False)],
    #                              ignore_index=True)
    # df_sp = df_ktl_kanban.copy()
    # df_sp['stadler_id'] = df_sp['sp_id']
    # df_ktl_kanban = pd.concat(objs=[df_ktl_kanban, df_sp], axis=1, ignore_index=True)
    # df_ktl_kanban.dropna(subset=['stadler_id'], inplace=True) # zdublowane ilości --- do zestawienia merge ze strukturą ok; do dołożenia jako oddzielan pozycja nieok

    #df_ktl_kanban['src'] = 'ktl_kanban_staps'
    df_ktl_kanban.to_excel(os.path.join(path_save, r'test_ktl_kanban.xlsx'), index=False)


    return df_ktl_kanban

import_ktlkanban(r'F:\Production\STAPS\22_C-materiał niesystemowy-KTL\KTL_KANBAN_V02.xlsb',
                     r'C:\Users\rytpio\Desktop\Projekty bieżące\WZ')
