import unittest

import unit_tests
from dicts_n_lists import file_import_map
from dicts_n_lists import sql_import_map
from dicts_n_lists import reference_map
from dicts_n_lists import ref_lists

from import_materialliste import nrc_sieve
from import_materialliste import group_position_sieve
from import_avz import assign_category_bu_1951939
from import_avz import clear_din
from import_materialliste import fz_list
from import_materialliste import fz_correction
from import_materialliste import order_category


class TestReferences(unittest.TestCase):
    """Test columns reference lists and dicts for import from files to SQL with steps"""

    def test_material_list_import(self):
        sql_columns = list(reference_map.sql_col.get('material_list').keys())
        sql_fk_columns = list(reference_map.sql_fk_col.get('material_list').keys())
        col_stag = list(file_import_map.infor_col_dict_STAG.values())
        col_staps = list(file_import_map.infor_col_dict_STAPS.values())
        col_staps_single = list(file_import_map.infor_col_dict_STAPS_single.values())
        col_short_universal = file_import_map.infor_col_list_short

        i = 0
        y = ['sql_columns', 'sql_fk_columns', 'col_stag', 'col_staps', 'col_staps_single', 'col_short_universal']
        for x in [sql_columns, sql_fk_columns, col_stag, col_staps, col_staps_single, col_short_universal]:
            self.assertCountEqual(x, list(set(x)), f"Material list doubles {y[i]}, {i}, {x}")
            i = +1

        for x in sql_fk_columns:
            self.assertIn(str(x).replace("CONSTRAINT ", ""), sql_columns, "MATERIAL LIST")

        for x in col_short_universal:
            self.assertIn(x, sql_columns, "MATERIAL LIST")
            self.assertIn(x, col_stag, "MATERIAL LIST")
            self.assertIn(x, col_staps, "MATERIAL LIST")
            self.assertIn(x, col_staps_single, "MATERIAL LIST")

        for x in ['fk_bossard_kanban_staps', 'fk_ktl_kanban_staps', 'fk_ktl_kanban_stag', 'fk_kabel_quantity']:
            self.assertIn(x, sql_columns, "MATERIAL LIST")

        for x in ['NRC', 'fz_list', 'fz_count', 'quantity_per_fz', 'price_per_fz', 'order_category', 'group', 'fz']:
            self.assertIn(x, sql_columns, "MATERIAL LIST")

    def test_avz_import(self):
        import_col_list = list(file_import_map.avz_col_dict.values())
        import_short_col_list = file_import_map.avz_col_short_list
        col_type_list = list(file_import_map.avz_col_type_dict.keys())
        sql_column_list = list(reference_map.sql_col.get('avz').keys())
        sql_fk_column_list = list(reference_map.sql_fk_col.get('avz').keys())

        i = 0
        y = ['import_col_list', 'import_short_col_list', 'col_type_list', 'sql_columns', 'sql_fk_columns']
        for x in [import_col_list, import_short_col_list, col_type_list, sql_column_list, sql_fk_column_list]:
            self.assertCountEqual(x, list(set(x)), f"AVZ doubles {y[i]}")
            i = +1

        for x in import_short_col_list:
            self.assertIn(x, import_col_list, "AVZ")

        for x in import_short_col_list:
            self.assertIn(x, sql_column_list, "AVZ")

        for x in col_type_list:
            self.assertIn(x, import_short_col_list, "AVZ")

        # Check if fk_columns definitions are in sql_columns
        for x in sql_fk_column_list:
            self.assertIn(str(x).replace('CONSTRAINT ', ''), sql_column_list)

        for x in ['fk_bossard_kanban_staps', 'fk_ktl_kanban_staps', 'fk_ktl_kanban_stag']:
            self.assertIn(x, sql_column_list, "AVZ")

        for x in ['din', 'din_txt', 'pos_nr_category_bu_1951939', 'breadcrumb', 'lvl1', 'lvl2', 'lvl3', 'lvl4',
                  'avz_quantity_in_tree', 'project']:
            self.assertIn(x, sql_column_list, "AVZ")

    def test_wz_import(self):
        sql_columns = list(sql_import_map.wz_staps_sql_col_dict.keys())
        # sql_fk_columns = list(reference_map.sql_fk_col.get('wz').keys())
        # 'fk_bossard_kanban_staps']'fk_ktl_kanban_staps']['fk_ktl_kanban_stag'] #Somehow not made into FK

        staps_list = list(file_import_map.wz_col_dict_STAPS.values())
        stag_list = list(file_import_map.wz_col_dict_STAG.values())  # Not used yet
        staps_short_list = file_import_map.wz_col_short_list_STAPS

        i = 0
        y = ['sql_columns', 'stag_list', 'staps_list', 'staps_short_list']
        for x in [sql_columns, stag_list, staps_list, staps_short_list]:
            self.assertCountEqual(x, list(set(x)), f"WZ doubles {y[i]}")
            i = +1

        for x in staps_short_list:
            self.assertIn(x, staps_list, "WZ")

        for x in staps_short_list:
            self.assertIn(x, sql_columns, "WZ")

        for x in ['viewer_link', 'lvl1', 'lvl2', 'lvl3', 'project', 'car',
                  'car_stadler_id']:  # check if new columns are in sql
            self.assertIn(x, sql_columns, "WZ")

    def test_bossard_import(self):
        sql_price_columns = list(sql_import_map.bossard_price_sql_short_col_dict.keys())
        sql_price_fk_columns = list(reference_map.sql_fk_col.get('bossard_price_staps').keys())

        sql_columns = list(reference_map.sql_col.get('bossard_kanban_staps').keys())
        short_columns = list(file_import_map.bossard_short_col_dict.values())
        # check for doubles
        self.assertCountEqual(short_columns, list(set(short_columns)), "BOSSARD")
        self.assertCountEqual(sql_columns, list(set(sql_columns)), "BOSSARD")
        # check if short is compliant with full
        for x in short_columns:
            self.assertIn(x, sql_columns, "BOSSARD")

        # Check if fk_columns definitions are in sql_columns
        for x in sql_price_fk_columns:
            self.assertIn(str(x).replace('CONSTRAINT ', ''), sql_price_columns)

    def test_device_import(self):
        """short in main, short in sql; sql without fk and new cols = short"""
        sql_columns = list(reference_map.sql_col.get('device_list').keys())
        sql_fk_columns = list(reference_map.sql_fk_col.get('device_list').keys())

        self.assertCountEqual(sql_columns, list(set(sql_columns)), "DEVICE")
        self.assertCountEqual(sql_fk_columns, list(set(sql_fk_columns)), "DEVICE")

        for project in list(set(file_import_map.device_dict_project.keys())):
            col_change_dict = file_import_map.device_dict_project.get(project).get('col_change_dict')
            col_complete_list = file_import_map.device_dict_project.get(project).get('col_complete_list')
            col_cutout_list = file_import_map.device_dict_project.get(project).get('col_cutout_list')

            self.assertCountEqual(list(col_change_dict.keys()), list(set(col_change_dict.keys())), "DEVICE")
            self.assertCountEqual(col_cutout_list, list(set(col_cutout_list)), "DEVICE")
            self.assertCountEqual(col_complete_list, list(set(col_complete_list)), "DEVICE")

            #  cutout_list->change_dict.keys
            self.assertCountEqual(col_cutout_list, list(col_change_dict.keys()),
                                  "DEVICE: cutout col list - change_dict keys Equal in lenght")
            for x in col_cutout_list:
                self.assertIn(x, list(col_change_dict.keys()),
                              f"DEVICE: Missing {x} cutout col list - change_dict keys")

            # final columns -> sql
            for x in col_complete_list:
                self.assertIn(x, sql_columns, f"DEVICE: Missing {x} final_import_col - sql_columns")

            # sql -> final columns
            col_complete_list.append("project")  # column added after file_import
            col_complete_list.append("stk_sum")  # column added after file_import
            sql_columns_no_fk = [x for x in sql_columns if 'fk_' not in x]  # remove foreign keys

            self.assertCountEqual(sql_columns_no_fk, col_complete_list,
                                  "DEVICE: sql_column - col_complete Equal in lenght")
            for x in sql_columns_no_fk:
                self.assertIn(x, col_complete_list, f"DEVICE: Missing {x}  sql_col - col_complete_list")

            # Check if columns added after import, before SQL are in SQL
            for x in ['stk_sum', 'project']:
                self.assertIn(x, sql_columns_no_fk, f"DEVICE: Missing {x} added columns -  sql_col")

            # Check if fk columns added after import, before SQL are in SQL
            for x in ['fk_bossard_prc', 'fk_bossard_kanban_staps', 'fk_ktl_kanban_staps', 'fk_ktl_kanban_stag']:
                self.assertIn(x, sql_columns, f"DEVICE: Missing {x} added columns -  sql_col")

            # Check if fk_columns definitions are in sql_columns
            for x in sql_fk_columns:
                self.assertIn(str(x).replace('CONSTRAINT ', ''), sql_columns)


class TestFunctions(unittest.TestCase):
    """Test functions"""

    def test_order_category_staps(self):
        self.assertEqual('standard', order_category('12345678'))
        self.assertEqual('standard', order_category(12345678))
        self.assertEqual('EB', order_category('EB12345678'))
        self.assertEqual('', order_category(''))

    def test_sieves(self):
        """  sieve NRC, sieve groupposition MATERIAL LIST"""
        nrc_list = ref_lists.material_list_nrc_ktxt
        for x in nrc_list:
            self.assertEqual("NRC", nrc_sieve(x, 1), "NRC_SIEVE")
        if "MATERIAL" not in nrc_list:
            self.assertEqual("NRC", nrc_sieve("MATERIAL", 0), "NRC_SIEVE")
            self.assertEqual("M", nrc_sieve("MATERIAL", 1), "NRC_SIEVE")
        else:
            print("'MATERIAL' is a NRC - test to be modified ! ")

        self.assertTrue(group_position_sieve("", 12004576, 1, ['']))  # stadler id GROUP, number
        self.assertTrue(group_position_sieve("", "12004576", 1, ['']))  # stadler id GROUP, string
        self.assertTrue(
            group_position_sieve("EB1204500", 12004501, 0, ['EB1204500']))  # order in group list and price 0, string
        self.assertFalse(
            group_position_sieve(1204500, 12004501, 0, [1204500]))  # order in group list and price 0, number
        self.assertFalse(
            group_position_sieve("EB1204500", 12004501, 1, ['EB1204500']))  # order in group list and price not 0
        self.assertFalse(group_position_sieve("x", 12004501, 0, ['']))  # order not in group list and price 0
        self.assertFalse(group_position_sieve("x", 12004501, 1, ['']))  # order not in group list and price not 0

    def test_pos_number_category(self):
        """ assign category AVZ """
        self.assertEqual("unassigned", assign_category_bu_1951939(0))
        self.assertEqual("unassigned", assign_category_bu_1951939(1300))
        self.assertEqual("unassigned", assign_category_bu_1951939(59000))
        self.assertEqual("unassigned", assign_category_bu_1951939(-10000))
        self.assertEqual("main_mechanic", assign_category_bu_1951939(2))
        self.assertEqual("screws", assign_category_bu_1951939(201))
        self.assertEqual("nuts", assign_category_bu_1951939(251))
        self.assertEqual("washers", assign_category_bu_1951939(301))
        self.assertEqual("bolts_misc", assign_category_bu_1951939(351))
        self.assertEqual("hoses_pneumatic", assign_category_bu_1951939(401))
        self.assertEqual("chemicals", assign_category_bu_1951939(451))
        self.assertEqual("struct_pneumatic", assign_category_bu_1951939(501))
        self.assertEqual("main_pneumatic", assign_category_bu_1951939(601))
        self.assertEqual("struct_electric", assign_category_bu_1951939(701))
        self.assertEqual("diverse", assign_category_bu_1951939(801))
        self.assertEqual("specification", assign_category_bu_1951939(901))
        self.assertEqual("main_electric", assign_category_bu_1951939(1001))
        self.assertNotEqual("main_electric", assign_category_bu_1951939(1301))

    def test_din(self):
        """ din avz clear function MATERIAL LIST"""
        din_input_list = ref_lists.din_avz_test_list_raw
        din_output_list = ref_lists.din_avz_test_list_processed
        i = 0
        for x in din_input_list:
            self.assertEqual(list(clear_din(x)), din_output_list[i])
            i += 1

    def test_fz_list(self):
        """ fz_list MATERIAL LIST"""
        self.assertEqual(fz_list(0, 0), '0', 'MATERIAL_LIST FZ_LIST')
        self.assertEqual(fz_list(1, 1), '1', 'MATERIAL_LIST FZ_LIST')
        self.assertEqual(fz_list(0, 2), '0, 1, 2', 'MATERIAL_LIST FZ_LIST')
        self.assertNotEqual(fz_list(2, 1), '1, 2', 'MATERIAL_LIST FZ_LIST')  # lucky guess correction

        # fz_correction

    def test_fz_correction(self):
        """ fz_correction MATERIAL LIST"""
        self.assertEqual(list(fz_correction(1, 2, 2)), [1, 2], 'fz_correction MATERIAL LIST')
        self.assertEqual(list(fz_correction(2, 1, 2)), [1, 2], 'fz_correction MATERIAL LIST')
        self.assertEqual(list(fz_correction(0.5, 1, 1)), [0, 1], 'fz_correction MATERIAL LIST')
        self.assertEqual(list(fz_correction(0.5, 0.5, 3)), [0, 0], 'fz_correction MATERIAL LIST')
        self.assertEqual(list(fz_correction(-1, 1, 2)), [1, 1], 'fz_correction MATERIAL LIST')
        self.assertEqual(list(fz_correction(-1, -2, 2)), [1, 2], 'fz_correction MATERIAL LIST')
        self.assertEqual(list(fz_correction(-2, -1, 4)), [1, 2], 'fz_correction MATERIAL LIST')
        self.assertEqual(list(fz_correction(-2, -1, 1)), [1, 1], 'fz_correction MATERIAL LIST')


# # def suite():
# suite = unittest.TestSuite()
# suite.addTest(TestReferences('test_device_import'))
# #     return suite

# unittest.main(TestReferences())

unittest.main(TestFunctions())
