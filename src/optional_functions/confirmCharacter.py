from ..utils import prYellow, prGreen


def remove_confirm_character(wd, cc):
    # wd = list of dictionary
    # cc = confirm_character
    for i in range(1, len(wd)):
        if wd[i][0].endswith(cc):
            wd[i][0] = wd[i][0][:-len(cc)]
    
    return wd


def add_confirm_character(wd, cc):
    # wd = list of dictionary
    # cc = confirm_character
    for i in range(1, len(wd)):
        wd[i] = [wd[i][0] + cc, wd[i][1]]
    return wd


def confirm_character_function(wd, a_ccf, cc):
    # wd = working_dict
    # a_ccf = ask_confirm_character_function
    # cc = confirm_character
    if a_ccf == 'R' or a_ccf == 'U':
        print(prYellow("Đang xoá Confirm Character trong Dictionary hiện tại..."))
        wd = remove_confirm_character(wd, cc)
        print(prGreen("Done"))
    if a_ccf == 'A' or a_ccf == 'U':
        print(prYellow("Đang thêm Confirm Character vào Dictionary hiện tại..."))
        wd = add_confirm_character(wd, cc)
        print(prGreen("Done"))
    return wd