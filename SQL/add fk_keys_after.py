import general_sql


def create_fk_keys_after_upload(project: str, wz: bool, avz: bool, material_list: bool, device_list: bool):
    """
    #add data fk indicators after wz add -- parents must be added first
    :param project:
    :param wz:
    :param avz:
    :param material_list:
    :param device_list:
    :return:
    """

    #if new added; although need to update it's own fk_'s
    # # WZ
    # if wz:
    #     general_sql.update_fk(['device_list'], 'wz', 'fk_wz', project)
    #     general_sql.update_fk(['material_list'], 'wz', 'fk_wz', project)
    #     general_sql.update_fk(['avz'], 'wz', 'fk_wz', project)

    # # AVZ
    # if avz:
    #     general_sql.update_fk(['wz'], 'avz', 'fk_avz', project)
    #     general_sql.update_fk(['material_list'], 'avz', 'fk_avz', project)

    # MATERIAL_LIST
    if material_list:
        general_sql.update_fk(['wz'], 'material_list', 'fk_material_list', project)
        general_sql.update_fk(['device_list'], 'material_list', 'fk_material_list', project)

    # # DEVICE_LIST
    # if device_list:
    #     general_sql.update_fk(['wz'], 'device_list', 'fk_device_list', project)
    #     general_sql.update_fk(['material_list'], 'device_list', 'fk_device_list', project)
    #
    #     general_sql.update_fk(['device_list'], 'wz', 'fk_wz', project)
    #     general_sql.update_fk(['device_list'], 'material_list', 'fk_material_list', project)


# for x in ["4503",
# "4541",
# "4547",
# "4556"]:
create_fk_keys_after_upload('4541', True, True, True, True)
#create_fk_keys_after_upload('4541', True, True, True, True)