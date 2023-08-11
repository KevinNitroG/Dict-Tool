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
        wd[i][0] = wd[i][0] + cc
    return wd