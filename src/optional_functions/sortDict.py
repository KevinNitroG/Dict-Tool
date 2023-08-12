from ..utils import prYellow, prGreen, prPurple


def sort_dict(wd, sdt):
    # wd = working_dict
    # sdt = sort_dict_type
    # md = modified_dict
    print(prYellow("Đang sort Dictionary theo kiểu " + prPurple(sdt)))
    md = [wd[0]]
    md += sorted(wd[1:], key=lambda x: x[sdt - 1])
    print(prGreen("Done"))
    return md