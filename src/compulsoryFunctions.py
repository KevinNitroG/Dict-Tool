import zipfile
import os
import re

from pathlib import Path

from .utils import exit_program, switch_pwd, delete_dir
from .pr import *


# SHORT VARS EXPLANATION

# yd = your_dict
# lold = list_of_line_dict
# cf = current_format
# wd = working_dict
# rc_p = current_dict['re_compile_pattern']
# dl = dict_list


def read_current_dict(yd):
    """Read current dictionary"""
    yd = yd.strip().strip("\n")
    if yd != '':
        lold = yd.splitlines()
    else:
        all_items = Path('./')
        list_dir = [item.name for item in all_items.iterdir() if (item.name not in ['Paste your dictionary into this folder'])
            and item.is_file()]
        if list_dir == []:
            exit_program(
                "Không tìm thấy bất kì file macro có sẵn trong thư mục hiện tại", 1)
        # List out the list of file with number
        print(prLightPurple("Chọn file macro:\n"))
        for i, file in enumerate(list_dir, start=1):
            print(f"{str(i).rjust(5)}.   {file}")
        _ = int(input("\nNhập số thứ tự file bạn muốn chọn: "))
        print()
        selected_file_name = list_dir[_-1]
        # If selection is a dictionary zip file
        if selected_file_name.endswith('.zip'):
            with zipfile.ZipFile(selected_file_name, 'r') as zip_ref:
                delete_dir('./Extracted Dict')
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
    """Create re.compile pattern"""
    cf = re.escape(cf).replace(
        '\\{sort\\}', '(?P<sort>.*)').replace('\\{long\\}', '(?P<long>.*)')
    return cf


def split_dict(wd, rc_p):
    """Split dictionary into list"""
    pattern = re.compile(rc_p)
    for i in range(1, len(wd)):
        match = re.search(pattern, wd[i])
        wd[i] = [match.group('sort'), match.group('long')]
    return wd


def select_dict_type(dl):
    """Select dictionary type"""
    for i, dict_type in enumerate(dl, start=1):
        print(f"{str(i).rjust(5)}.   {dict_type['name']}")
    print()
    _ = input("Chọn thứ tự: ")
    return dl[int(_)-1]


def detect_current_dict_type(wd, dl):
    """Detect current dictionary"""
    first_line = wd[0][:-1]
    for dict_type in dl:
        if first_line in dict_type['first_line']:
            _ = input(
                f"Dictionary hiện tại là {dict_type['name'].upper()}? [Y/n]: ")
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
    return ''


def join_working_dict(wd):
    """Join final dictionary"""
    return '\n'.join(wd)
