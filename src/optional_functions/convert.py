def convert(wd, sd):
    # wd = working_dict
    # sd = selected_dict
    wd[0] = sd['first_line']
    for i in range(1, len(wd)):
        wd[i] = sd['format'].format(sort=wd[i][0], long=wd[i][1])
    return wd