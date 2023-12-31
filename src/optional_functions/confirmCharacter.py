from ..utils import decorator


# SHORT VARS EXPLAINATION

# wd = working_dict
# cc = confirm_character
# a_ccf = ask_confirm_character_function


def remove_confirm_character(wd, cc):
    """Delete confirm character"""
    for i in range(1, len(wd)):
        if wd[i][0].endswith(cc):
            wd[i][0] = wd[i][0][:-len(cc)]

    return wd


def add_confirm_character(wd, cc):
    """Thêm confirm character"""
    for i in range(1, len(wd)):
        wd[i] = [wd[i][0] + cc, wd[i][1]]
    return wd


@decorator
def confirm_character_function(wd, a_ccf, cc):
    """Confirm character"""
    if a_ccf in ('R', 'U'):
        wd = remove_confirm_character(wd, cc)
    if a_ccf in ('A', 'U'):
        wd = add_confirm_character(wd, cc)
    return wd
