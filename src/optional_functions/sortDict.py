from ..utils import prYellow, prGreen, prBlue, decorator


# SHORT VARS EXPLANATION

# wd = working_dict
# sdt = sort_dict_type
# md = modified_dict


@decorator
def sort_dict(wd, sdt):
    '''Sort dictionary'''
    print(prYellow("Sort Dictionary theo kiểu " + prBlue(sdt)))
    md = [wd[0]]
    md += sorted(wd[1:], key=lambda x: x[sdt - 1])
    return md