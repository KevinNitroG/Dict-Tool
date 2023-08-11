import os
import re

from .pr import *


def remove_latex(wd, lf):
    # wd = list_of_line_dictionary
    # lf = latex_format
    # md = modified_dictionary
    md = [wd[0]]
    for i in range(1, len(wd)):
        if wd[i][0][0] not in lf:
            md += [wd[i]]
    return md


def convert(wd, cd, sd):
    # wd = list_of_line_dictionary
    # cd = current_dictionary
    # sd = selected_dictionary
    # IF CURRENT DICTIONARY IS GBOARD, THEN \t AT THE END WILL BE REMOVED
    if cd['specific_name'] == 'g':
        for i in range(1, len(wd)):
            wd[i][2] = wd[i][2][:-1]
    # CONVERT
    wd[0] = sd['first_line']
    for i in range(1, len(wd)):
        wd[i] = [wd[i][0], sd['delimiter'], wd[i][2]]
    # IF SELECTED DICTIONARY IS GBOARD, THEN \t AT THE END WILL BE ADDED
    if sd['specific_name'] == 'g':
        for i in range(1, len(wd)):
            wd[i][2] = wd[i][2] + '\t'
    return wd

def add_confirm_character(wd, sd_rcp,cc):
    # wd = list of dictionary
    # sd_d_rcp = selected_dictionary['re_compile_pattern']
    # cc = confirm_character
    for i in range(1, len(wd)):
        wd[i][0] = wd[i][0] + cc
    return wd

def remove_confirm_character(wd, sd_rcp,cc):
    # wd = list of dictionary
    # sd_d_rcp = selected_dictionary['re_compile_pattern']
    # cc = confirm_character
    for i in range(1, len(wd)):
        if wd[i][0].endswith(cc):
            wd[i][0] = wd[i][0][:-len(cc)]
    return wd


def sort_dict(wd):
    # wd = working_dictionary
    return sorted(wd, key=lambda x: x[0])


def create_converted_dictionary_as_file(fd, sd_m):
    # fd = final_dictionary
    # sd_m = selected_dictionary["macro"]
    _ = 'Y'
    if os.path.exists(sd_m):
        _ = input(prYellow("File macro đã hiện có tại đường dẫn hiện tại, có muốn ghi đè [Y/n]: ")).upper()
        print()
    if _ == 'Y' or _ == '':
            with open(sd_m, 'w', encoding="utf-8") as file:
                file.write(fd)
            print(prGreen("File macro đã được tạo ^^. Tên file: ") + prPurple(sd_m))
    else:
        print(prGreen("\nĐã huỷ tạo file macro"))


def gboard_dictionary_compress(name, compress):
    with zipfile.ZipFile(compress, 'w') as zip_ref:
        zip_ref.write(name)
    print(prGreen("File zip macro gboard đã được tạo ^^. Tên file: ") + prPurple(evkey_macro))


# def evkey_special_create_file(content, output_dictionary_folder, evkey_macro):
#     import shutil
#     from .utils import switch_pwd
#     switch_pwd('../')
#     shutil.copy('DoNotTouchThis/evkey_macro_first_line.txt', os.path.join(output_dictionary_folder, evkey_macro))
#     switch_pwd(output_dictionary_folder)
#     content = content[69:]
#     with open(evkey_macro, 'a', encoding='utf-8') as f:
#         f.write(content)


def evkey_special_create_file(content, output_dictionary_folder, evkey_macro):
    content = content[69:]
    from .constants import EVKey_macro_first_line_binary as first_line
    with open(evkey_macro, 'wb') as f:
        f.write(first_line)
    with open(evkey_macro, 'a', encoding='utf-8') as f:
        f.write(content)
    print(prGreen("File macro đã được tạo ^^. Tên file: ") + prPurple(evkey_macro))