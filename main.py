from src import clear_screen, wait_for_pressed_key, switch_pwd, exit_program
from src import prBanner, prTitle, prGreen, prBlue, prLightPurple
from src import read_current_dict, detect_current_dict_type, create_re_compile_pattern, split_dict, select_dict_type, join_working_dict
from src import latex_function, confirm_character_function, sort_dict, convert, create_converted_dictionary_as_file

from dictionaryList import *
from userConstants import *


def main():

    clear_screen()
    prBanner()
    wait_for_pressed_key()

    try:
        from userOptions import ask_convert_dict, ask_latex_function, ask_confirm_character_function, ask_sort_dict, ask_print_final_dictionary, ask_create_macro
    except ModuleNotFoundError:
        ask_convert_dict, ask_latex_function, ask_confirm_character_function, ask_sort_dict, ask_print_final_dictionary, ask_create_macro = '', '', '', '', '', ''

    # PREPARE...

    prTitle("PREPARE")
    print(prLightPurple("Reading your dictionary...\n"))
    switch_pwd(input_dict_folder)
    # read your dict file
    working_dict = read_current_dict(your_dictionary)
    # detect your dict file
    current_dict = detect_current_dict_type(working_dict, dictionary_list)
    # create re_compile_pattern for current dict
    current_dict['re_compile_pattern'] = create_re_compile_pattern(
        current_dict['format'])
    # split each line into parts using re.match
    working_dict = split_dict(working_dict, current_dict["re_compile_pattern"])
    switch_pwd('../')
    print()
    print(prGreen("Done reading!"))
    print()
    clear_screen()

    # ASK USER FOR FUNCTIONS

    clear_screen()
    prTitle("CHỌN OPTIONS")
    print(prLightPurple("Chọn theo trong dấu [], lựa chọn nào in hoa sẽ là mặc định"))
    print()
    ask_convert_dict = ask_convert_dict.upper() or input(
        "Convert dictionary sang dictionary bộ gõ khác [y/N]: ").upper()
    ask_latex_function = ask_latex_function.upper() or input(
        "Latex [a]dd / [r]emove / [u]pdate / [ABORT]: ").upper()
    ask_confirm_character_function = ask_confirm_character_function.upper() or input(
        "Confirm character [a]dd / [r]emove / [u]pdate / [ABORT]: ").upper()
    ask_sort_dict = ask_sort_dict.upper() or input(
        "Sort lại theo từ tắt từ a-z [Y/n]: ").upper()
    ask_print_final_dictionary = ask_print_final_dictionary.upper() or input(
        "In ra converted dictionary [Y/n]: ").upper()
    ask_create_macro = ask_create_macro.upper() or input(
        "Tạo file macro trong directory hiện tại [y/N]: ").upper()
    print()
    clear_screen()

    # EXECUTE OPTIONAL FUNCTIONS
    prTitle("EXECUTE FUNCTIONS")

    # LaTeX function - compare user input inside function
    working_dict = latex_function(working_dict, ask_latex_function)

    # Confirm character - compare user input inside function
    working_dict = confirm_character_function(
        working_dict, ask_confirm_character_function, confirm_character)

    # Sort dict
    if ask_sort_dict in ('Y', ''):
        working_dict = sort_dict(working_dict, sort_dict_type)

    # Convert dict
    if ask_convert_dict == 'Y':
        print(prBlue("Chọn loại dictionary convert sang:"))
        print()
        # select your dict to convert
        selected_dict = select_dict_type(dictionary_list)
        # create re_compile_pattern for selected dict
        selected_dict['re_compile_pattern'] = create_re_compile_pattern(
            selected_dict['format'])
    else:
        selected_dict = current_dict

    working_dict = convert(working_dict, selected_dict)

    # Join dictionary
    working_dict = join_working_dict(working_dict)

    print(prGreen("Done executing functions!"))
    print()

    # FINISH JOBS

    # Print dictionary
    if ask_print_final_dictionary in ('Y', ''):
        prTitle("PRINT DICTIONARY")
        print(working_dict)
        print()
        wait_for_pressed_key()
        print()

    # Create macro file
    if ask_create_macro == 'Y':
        prTitle("TẠO FILE MACRO")
        switch_pwd(output_dict_folder)
        create_converted_dictionary_as_file(working_dict, selected_dict)
        print()
        wait_for_pressed_key()

    exit_program("Kết thúc chương trình ^^")


# SCRIPT START FROM HERE

main()
