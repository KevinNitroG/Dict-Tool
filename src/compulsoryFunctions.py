import fnmatch
import zipfile
import os
import re

from .utils import exit_program, switch_pwd, delete_dir
from .pr import *


# SHORT VARS EXPLANATION

# yd = your_dict
# adzf = all_dict_zip_files
# lold = list_of_line_dict
# cf = current_format
# wd = working_dict
# rc_p = current_dict['re_compile_pattern']
# dl = dict_list


def read_current_dict(yd, adzf):
    '''Đọc dictionary'''
    yd = yd.strip().strip("\n")
    list_dir = []
    if yd != '':
        lold = yd.splitlines()
    else:
        delete_dir('./Extracted Dict')
        list_dir = [f for f in os.listdir() if (f.endswith(
            '.txt') or True for zip_file_name in adzf if fnmatch.fnmatch(f, zip_file_name))]
        if list_dir == []:
            exit_program(
                "Không tìm thấy bất kì file macro có sẵn trong thư mục hiện tại", 1)
        # List out the list of file with number
        print(prLightPurple("Chọn file macro:\n"))
        for i, file in enumerate(list_dir, start=1):
            print("{}.   {}".format(str(i).rjust(5), file))
        _ = int(input("\nNhập số thứ tự file bạn muốn chọn: "))
        print()
        selected_file_name = list_dir[_-1]
        # If selection is a dictionary zip file
        if selected_file_name.endswith('.zip'):
            with zipfile.ZipFile(selected_file_name, 'r') as zip_ref:
                switch_pwd('./Extracted Dict')
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
    '''Tạo re.compile pattern'''
    cf = re.escape(cf).replace(
        '\\{sort\\}', '(?P<sort>.*)').replace('\\{long\\}', '(?P<long>.*)')
    return cf


# Detech which type is the dict, {sort} before {long} or vice versa
# def specify_format_type(cf):
#     # cf = current_format
#     if cf.index('{sort}') < cf.index('{long}'):
#         return 1
#     return 2


def split_dict(wd, rc_p):
    '''Tách dictionary thành list'''
    pattern = re.compile(rc_p)
    for i in range(1, len(wd)):
        match = re.search(pattern, wd[i])
        wd[i] = [match.group('sort'), match.group('long')]
    return wd


def select_dict_type(dl):
    '''Chọn loại dictionary'''
    for i, dict_type in enumerate(dl, start=1):
        print("{}.   {}".format(str(i).rjust(5), dict_type["name"]))
    print()
    _ = input("Chọn thứ tự: ")
    return dl[int(_)-1]


def detect_current_dict_type(wd, dl):
    '''Tự động nhận diện loại dictionary'''
    first_line = wd[0][:-1]
    for dict_type in dl:
        if first_line in dict_type["first_line"]:
            _ = input(
                "Dictionary hiện tại là {}? [Y/n]: ".format(dict_type["name"])).upper()
            if _ in ('Y', ''):
                return dict_type
            print(prLightPurple("\nChọn loại dictionary bộ gõ hiện tại\n"))
            return select_dict_type(dl)
    # NO AVAILABLE DICTIONARY TYPE MATCH
    _ = input(
        "\nKhông thể nhận diện được dictionary hiện tại. Chọn thủ công? [Y/n]: ").upper()
    if _ in ('Y', ''):
        print(prLightPurple("\nChọn loại dictionary bộ gõ hiện tại\n"))
        return select_dict_type(dl)
    exit_program("Kết thúc chương trình")


def join_working_dict(wd):
    '''Gộp list dictionary hoàn chỉnh'''
    return '\n'.join(wd)
