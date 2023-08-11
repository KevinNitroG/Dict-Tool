# TODO NOTE
# ADD LATEXT UPDATE FROM GITHUB: https://github.com/DenverCoder1/latex-gboard-dictionary
# add ... in selections
# compress file name follow dictionaryList
# switch create dbjasdbakdb from main into sub function!

import subprocess

from src import *

from userConstants import your_dictionary, input_dictionary_folder, output_dictionary_folder
from dictionaryList import *
from userConstants import confirm_character


def main():

    prBanner()
    wait_for_pressed_key()

    try:
        from userOptions import ask_remove_latex, ask_confirm_character, ask_sort_dict, ask_print_final_dictionary, ask_create_macro
    except ModuleNotFoundError:
        pass


    # PREPARE...


    print(prGreen("Reading your dictionary...\n"))
    switch_pwd(input_dictionary_folder)
    all_dictionary_zip_file = [dictionary['dictionary_zip_file'] for dictionary in dictionary_list if dictionary['dictionary_zip_file'] != '']
    splitlines_working_dictionary = read_current_dictionary(your_dictionary, all_dictionary_zip_file)
    current_dictionary = detect_current_dictionary_type(splitlines_working_dictionary, dictionary_list)
    splitlines_working_dictionary = split_splitlines_working_dictionary(splitlines_working_dictionary, current_dictionary["re_compile_pattern"])
    if current_dictionary['format'] == 2:
        splitlines_working_dictionary = reverse_dictionary_format(splitlines_working_dictionary)
    switch_pwd('../')
    clear_screen()

    print(prBold(prLightBlue("CHỌN LOẠI DICTIONARY CONVERT SANG".center(40, '-'))), end = '\n\n')
    selected_dictionary = select_dictionary_type(dictionary_list)


    # ASK USER FOR FUNCTIONS


    clear_screen()
    print(prBold(prLightBlue("LỰA CHỌN OPTIONS".center(40, '-'))), end = '\n\n')
    print(prLightPurple("Chọn theo trong dấu [], lựa chọn nào in hoa sẽ là mặc định"))
    print("\033[1;33m") # YELLOW
    ask_remove_latex = input("Remove Latext [Y/n]: ").upper() if ask_remove_latex == '' else ask_remove_latex
    ask_confirm_character = input("Confirm character [a]dd / [r]emove / [u]pdate / [ABORT]: ") if ask_confirm_character == '' else ask_confirm_character
    ask_sort_dict = input("Sort lại theo từ tắt từ a-z [Y/n]: ").upper() if ask_sort_dict == '' else ask_sort_dict
    ask_print_final_dictionary = input("In ra converted dictionary [Y/n]: ").upper() if ask_print_final_dictionary == '' else ask_print_final_dictionary
    ask_create_macro = input("Tạo file macro trong directory hiện tại [y/N]: ").upper() if ask_create_macro == '' else ask_create_macro
    print("\033[0m") # RESET COLOUR
    clear_screen()


    # EXECUTE OPTIONAL FUNCTIONS


    # Remove LaTeX
    if ask_remove_latex == 'Y' or ask_remove_latex == '':
        from userConstants import latex_format
        splitlines_working_dictionary = remove_latex(splitlines_working_dictionary, latex_format)

    # Convert dict
    splitlines_working_dictionary = convert(splitlines_working_dictionary, current_dictionary, selected_dictionary)

    # Confirm character
    if ask_confirm_character == 'r' or ask_confirm_character == 'u':
        splitlines_working_dictionary = remove_confirm_character(splitlines_working_dictionary, selected_dictionary['re_compile_pattern'], confirm_character)
    elif ask_confirm_character == 'a' or ask_confirm_character == 'u':
        splitlines_working_dictionary = add_confirm_character(splitlines_working_dictionary, selected_dictionary['re_compile_pattern'], confirm_character)

    # Sort dict
    if ask_sort_dict == 'Y' or ask_sort_dict == '':
        splitlines_working_dictionary = sort_dict(splitlines_working_dictionary)


    # FINISH JOBS


    if selected_dictionary['format'] == 2:
        splitlines_working_dictionary = reverse_dictionary_format(splitlines_working_dictionary)

    # Join dictionary
    splitlines_working_dictionary = join_splitlines_working_dictionary(splitlines_working_dictionary)

    # Print dictionary
    if ask_print_final_dictionary == 'Y' or ask_print_final_dictionary == '':
        print(splitlines_working_dictionary, end = '\n\n')
        wait_for_pressed_key()

    # Create macro file
    switch_pwd(output_dictionary_folder)
    if ask_create_macro == 'Y':
        print(prBold(prLightBlue("TẠO FILE MACRO".center(40, '-'))), end = '\n\n')
        # If selected dictionary is EVKey
        if selected_dictionary['specific_name'] == 'e':
            _ = input(prYellow("\nPhát hiện đã chọn convert sang EVKey, script sẽ tự động tạo file theo phương pháp đặc biệt? [Y/n]: ")).upper()
            if _ == 'Y' or _ == '':
                evkey_special_create_file(splitlines_working_dictionary, output_dictionary_folder, selected_dictionary['macro'])
        # If selected dictionary is Gboard
        elif selected_dictionary['specific_name'] == 'g':
            _ = input(prYellow("\nPhát hiện đã chọn convert sang GBoard, bạn có muốn zip file lại? [Y/n]: ")).upper()
            if _ == 'Y' or _ == '':
                from userConstants import gboard_dictionary_compress_file_name
                gboard_dictionary_compress("dictionary.txt", gboard_dictionary_compress_file_name)
        else:
            # Create step
            create_converted_dictionary_as_file(splitlines_working_dictionary, selected_dictionary['macro'])

        wait_for_pressed_key()

    exit_program("Kết thúc chương trình ^^")


# SCRIPT START FROM HERE

try:
    main()
except ModuleNotFoundError:
    install_requirements()