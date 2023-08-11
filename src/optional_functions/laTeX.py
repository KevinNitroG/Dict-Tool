def remove_latex(wd, lf):
    # wd = working_dict
    # lf = latex_format
    # md = modified_dict
    md = [wd[0]]
    for i in range(1, len(wd)):
        if wd[i][0][0] not in lf:
            md += [wd[i]]
    return md


def add_latex(wd, lf):
    # wd = working_dict
    # lf = latex_format
    # md = modified_dict
    md = [wd[0]]
    for i in range(1, len(wd)):
        if wd[i][0][0] not in lf:
            md += [wd[i]]
    return md


def download_latex():
    pass