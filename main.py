# TODO NOTE
# ADD LATEXT UPDATE FROM GITHUB: https://github.com/DenverCoder1/latex-gboard-dictionary
# add ... in selections

from src import *

from userConstants import your_dictionary, input_dict_folder, output_dict_folder
from dictionaryList import *
from userConstants import confirm_character


def main():

    clear_screen()
    prBanner()
    wait_for_pressed_key()

    try:
        from userOptions import ask_convert_dict, ask_remove_latex, ask_confirm_character, ask_sorten_dict, ask_print_final_dictionary, ask_create_macro
    except ModuleNotFoundError:
        pass


    # PREPARE...

    prTitle("PREPARE")
    print(prLightPurple("Reading your dictionary...\n"))
    switch_pwd(input_dict_folder)
    all_dict_zip_file = [dict['dictionary_zip_file'] for dict in dictionary_list if dict['dictionary_zip_file'] is not None]
    # read your dict file
    working_dict = read_current_dict(your_dictionary, all_dict_zip_file)
    # detect your dict file
    current_dict = detect_current_dict_type(working_dict, dictionary_list)
    # create re_compile_pattern for current dict
    current_dict['re_compile_pattern'] = create_re_compile_pattern(current_dict['format'])
    # Specify the format type of current dict
    current_dict['format_type'] = specify_format_type(current_dict['format'])
    # split each line into parts using re.match
    working_dict = split_working_dict(working_dict, current_dict["re_compile_pattern"], current_dict['format_type'])
    switch_pwd('../')
    print(prGreen("Done reading!"))
    print()
    # clear_screen()


    # ASK USER FOR FUNCTIONS


    # clear_screen()
    prTitle("CHỌN OPTIONS")
    print(prLightPurple("Chọn theo trong dấu [], lựa chọn nào in hoa sẽ là mặc định"))
    print()
    ask_convert_dict = input("Convert dictionary sang dictionary bộ gõ khác [y/N]: ").upper() if ask_convert_dict is not None else ask_convert_dict
    ask_remove_latex = input("Remove Latext [Y/n]: ").upper() if ask_remove_latex is not None else ask_remove_latex
    ask_confirm_character = input("Confirm character [a]dd / [r]emove / [u]pdate / [ABORT]: ") if ask_confirm_character is not None else ask_confirm_character
    ask_sorten_dict = input("Sort lại theo từ tắt từ a-z [Y/n]: ").upper() if ask_sorten_dict is not None else ask_sorten_dict
    ask_print_final_dictionary = input("In ra converted dictionary [Y/n]: ").upper() if ask_print_final_dictionary is not None else ask_print_final_dictionary
    ask_create_macro = input("Tạo file macro trong directory hiện tại [y/N]: ").upper() if ask_create_macro is not None else ask_create_macro
    print()
    # clear_screen()


    # EXECUTE OPTIONAL FUNCTIONS
    prTitle("EXECUTE FUNCTIONS")
    print(prLightPurple("Working..."))

    # Remove LaTeX
    if ask_remove_latex == 'Y' or ask_remove_latex == '':
        from userConstants import latex_format
        working_dict = remove_latex(working_dict, latex_format)

    # Confirm character
    if ask_confirm_character == 'r' or ask_confirm_character == 'u':
        working_dict = remove_confirm_character(working_dict, confirm_character)
    if ask_confirm_character == 'a' or ask_confirm_character == 'u':
        working_dict = add_confirm_character(working_dict, confirm_character)

    # Sort dict
    if ask_sorten_dict == 'Y' or ask_sorten_dict == '':
        working_dict = sorten_dict(working_dict)

    # Convert dict
    if ask_convert_dict == 'Y':
        prTitle("CHỌN LOẠI DICTIONARY CONVERT SANG")
        # select your dict to convert
        selected_dict = select_dict_type(dictionary_list)
        # create re_compile_pattern for selected dict
        selected_dict['re_compile_pattern'] = create_re_compile_pattern(selected_dict['format'])
        # Specify the format type of selected dict
        selected_dict['format_type'] = specify_format_type(selected_dict['format'])
    else:
        selected_dict = current_dict

    working_dict = convert(working_dict, selected_dict)

    # Join dictionary
    working_dict = join_working_dict(working_dict)

    print(prGreen("Done executing functions!"))
    print()


    # FINISH JOBS


    # Print dictionary
    if ask_print_final_dictionary == 'Y' or ask_print_final_dictionary == '':
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
        wait_for_pressed_key()

    exit_program("Kết thúc chương trình ^^")


# SCRIPT START FROM HERE

main()