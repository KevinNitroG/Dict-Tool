import fnmatch
import zipfile
import os
import re

from .utils import clear_screen, exit_program
from .pr import *


def extract_delimiter(rcp):
    # rc_p = re_compile_pattern
    start = rcp.find('(', rcp.find('(') + 1)
    end = rcp.find(')', start)
    return rcp[start + 1: end]

def read_current_dictionary(yd, adzf):
    # yd = your_dictionary
    # adzf = all_dictionary_zip_files
    yd = yd.strip().strip("\n")
    list_dir = []
    if yd != '':
        list_of_line_dictionary = yd.splitlines()
    else:
        # list_dir = [f for f in os.listdir() if (f.endswith('.txt') or fnmatch.fnmatch(f, 'PersonalDictionary-*.zip'))]
        list_dir = [f for f in os.listdir() if (f.endswith('.txt') or True for zip_file_name in adzf if fnmatch.fnmatch(f, zip_file_name))]
        if list_dir == []:
            exit_program("Không tìm thấy bất kì file macro có sẵn trong thư mục hiện tại", 1)
        # List out the list of file with number
        print(prLightBlue("Vui lòng chọn file macro:\n"))
        for i, file in enumerate(list_dir, start=1):
            print(f"{prYellow(i)}\t{file}")
        _ = int(input(prYellow("\nNhập số thứ tự file bạn muốn chọn: ")))
        selected_file_name = list_dir[_-1]
        # If selection is a GBoard dictionary zip file
        if fnmatch.fnmatch(selected_file_name, 'PersonalDictionary-*.zip'):
            with zipfile.ZipFile(selected_file_name, 'r') as zip_ref:
                zip_ref.extractall("./")
            with open('dictionary.txt', 'r', encoding='utf-8') as file:
                list_of_line_dictionary = file.readlines()
        else:
            with open(selected_file_name, 'r', encoding='utf-8') as file:
                list_of_line_dictionary = file.readlines()
    return list_of_line_dictionary


def split_splitlines_working_dictionary(wd, rc_p):
    # wd = working_dictionary
    # rc_p = current_dictionary["re_compile_pattern"]
    pattern = re.compile(rc_p)
    for i in range(1, len(wd)):
        match = re.search(pattern, wd[i])
        wd[i] = [match.group(1), match.group(2), match.group(3)]
    return wd


def reverse_dictionary_format(wd):
    # wd = working_dictionary
    for i in range(1, len(wd)):
        wd[i].reverse()
    return wd


def join_splitlines_working_dictionary(wd):
    # wd = working_dictionary
    for i in range(1, len(wd)):
        wd[i] = ''.join(wd[i])
    wd = '\n'.join(wd)
    return wd


def select_dictionary_type(dl):
    # dl = dictionary_list
    for i, dictionary_type in enumerate(dl, start=1):
        print("{}\t {}".format(prYellow(i).ljust(5, '.'), dictionary_type["name"]))
    print()
    _ = input(prYellow("Chọn thứ tự: "))
    return dl[int(_)-1]


def detect_current_dictionary_type(wd, dl):
    # wd = working_dictionary
    # dl = dictionary_list
    first_line = wd[0][:-1]
    for dictionary_type in dl:
        if first_line == dictionary_type["first_line"]:
            _ = input(prYellow("\nPhát hiện dictionary hiện tại là {}? [Y/n]: ".format(dictionary_type["name"]))).upper()
            if _ == 'Y' or _ == '':
                return dictionary_type
            else:
                print(prLightPurple("\nCHỌN LOẠI DICTIONARY BỘ GÕ HIỆN TẠI\n"))
                return select_dictionary_type(dl)
    # NO AVAILABLE DICTIONARY TYPE MATCH
    _ = input(prYellow("\nKhông thể nhận diện được dictionary hiện tại. Chọn thủ công? [Y/n]: ").upper())
    if _ == 'Y' or _ == '':
        print(prLightPurple("\nCHỌN LOẠI DICTIONARY BỘ GÕ HIỆN TẠI\n"))
        return select_dictionary_type(dl)
    else:
        exit_program("Kết thúc chương trình")