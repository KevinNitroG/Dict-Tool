def sorten_dict(wd):
    # wd = working_dict
    # md = modified_dict
    md = [wd[0]]
    md += sorted(wd[1:])
    return md