import fnmatch
import zipfile
import os
import re

from .utils import clear_screen, exit_program, switch_pwd, delete_dir
from .pr import *


def read_current_dict(yd, adzf):
    # yd = your_dict
    # adzf = all_dict_zip_files
    # lold = list_of_line_dict
    yd = yd.strip().strip("\n")
    list_dir = []
    if yd != '':
        lold = yd.splitlines()
    else:
        delete_dir('./Extracted Folder')
        list_dir = [f for f in os.listdir() if (f.endswith('.txt') or True for zip_file_name in adzf if fnmatch.fnmatch(f, zip_file_name))]
        if list_dir == []:
            exit_program("Không tìm thấy bất kì file macro có sẵn trong thư mục hiện tại", 1)
        # List out the list of file with number
        print(prLightPurple("Chọn file macro:\n"))
        for i, file in enumerate(list_dir, start=1):
            print(f"{prYellow(i)}\t{file}")
        _ = int(input("\nNhập số thứ tự file bạn muốn chọn: "))
        selected_file_name = list_dir[_-1]
        # If selection is a dictionary zip file
        if (True for zip_file_name in adzf if fnmatch.fnmatch(selected_file_name, zip_file_name)):
            with zipfile.ZipFile(selected_file_name, 'r') as zip_ref:
                switch_pwd('./Extracted Folder')
                zip_ref.extractall("./")
                os.rename(zip_ref.namelist()[0], 'extracted_dictionary.txt')
            with open('extracted_dictionary.txt', 'r', encoding='utf-8') as file:
                lold = file.readlines()
            switch_pwd('../')
        else:
            with open(selected_file_name, 'r', encoding='utf-8') as file:
                lold = file.readlines()
    return lold


def create_re_compile_pattern(cf):
    # cf = current_format
    return cf.replace('{sort}', '(.*)').replace('{long}', '(.*)')


def specify_format_type(cf):
    # cf = current_format
    if cf.index('{sort}') < cf.index('{long}'):
        return 1
    return 2


def split_working_dict(wd, rc_p, ft):
    # wd = working_dict
    # rc_p = current_dict['re_compile_pattern']
    # ft = current_dict['format_type']
    pattern = re.compile(rc_p)
    if ft == 1:
        for i in range(1, len(wd)):
            match = re.search(pattern, wd[i])
            wd[i] = [match.group(1), match.group(2)]
    else:
        for i in range(1, len(wd)):
            match = re.search(pattern, wd[i])
            wd[i] = [match.group(2), match.group(1)]
    return wd


def select_dict_type(dl):
    # dl = dict_list
    for i, dict_type in enumerate(dl, start=1):
        print("{}\t {}".format(prYellow(i).ljust(5, '.'), dict_type["name"]))
    print()
    _ = input(prYellow("Chọn thứ tự: "))
    return dl[int(_)-1]


def detect_current_dict_type(wd, dl):
    # wd = working_dict
    # dl = dict_list
    first_line = wd[0][:-1]
    for dict_type in dl:
        if first_line == dict_type["first_line"]:
            _ = input("\nPhát hiện dictionary hiện tại là {}? [Y/n]: ".format(dict_type["name"])).upper()
            if _ == 'Y' or _ == '':
                return dict_type
            else:
                print(prLightPurple("\nChọn loại dictionary bộ gõ hiện tại\n"))
                return select_dict_type(dl)
    # NO AVAILABLE DICTIONARY TYPE MATCH
    _ = input("\nKhông thể nhận diện được dictionary hiện tại. Chọn thủ công? [Y/n]: ").upper()
    if _ == 'Y' or _ == '':
        print(prLightPurple("\nChọn loại dictionary bộ gõ hiện tại\n"))
        return select_dict_type(dl)
    else:
        exit_program("Kết thúc chương trình")


def join_working_dict(wd):
    # wd = working_dict
    return '\n'.join(wd)