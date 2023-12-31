import os
import shutil
import sys

from .pr import *


def clear_screen():
    """Clear running screen"""
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Linux and Mac
        os.system('clear')


def wait_for_pressed_key():
    """Wait for user keyboard input"""
    print()
    os.system('pause')
    clear_screen()


def exit_program(msg="Unkown", exit_code=0):
    """Exit program"""
    print(prBold(prLightBlue("KẾT THÚC".center(40, '-'))), end='\n\n')
    if exit_code == 0:
        print(prCyan(msg))
    else:
        print(prRed(msg))
    print()
    os.system('pause')
    sys.exit(exit_code)


# def install_requirements():
#     import subprocess
#     import sys
#     try:
#         subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
#     except subprocess.CalledProcessError:
#         exit_program("Lỗi khi cài đặt requirements. Hãy dùng cmd và nhập lệnh" + prBold("pip install -r requirements.txt"), 1)


def switch_pwd(pwd):
    """Switch present working directory"""
    try:
        os.chdir(pwd)
    except FileNotFoundError:
        print(prRed("Oops folder không tồn tại: \t" + prPurple(pwd)))
        print(prYellow("Tạo folder: \t\t\t" + prPurple(pwd)))
        os.makedirs(pwd)
        os.chdir(pwd)


def delete_dir(d):
    """Delete directory"""
    try:
        shutil.rmtree(d)
        print(prYellow("Đã xoá folder: " + prPurple(d)))
    except FileNotFoundError:
        pass


def decorator(f):
    """Log?"""
    def wrapper(*args, **kwargs):
        print(prLightBlue("WORKING:\t"), prLightPurple(f.__doc__))
        result = f(*args, **kwargs)
        print(prGreen("DONE:\t\t"), prLightPurple(f.__doc__))
        return result
    return wrapper
