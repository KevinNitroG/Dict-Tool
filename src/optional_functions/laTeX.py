import os

from json import loads

from ..constants import latex_format as lf
from ..constants import latex_api, latex_cdn_link, latex_raw_github_link
from ..pr import prGreen, prYellow, prRed, prPurple

from urllib.request import urlopen
from ..utils import switch_pwd
from ..compulsoryFunctions import split_dict


def should_download_latex():
    print(prYellow("Fetch sha của LaTeX dict hiện có trên Github..."))
    with urlopen(latex_api) as f:
        fetched_sha = loads(f.read())['sha']
    try:
        with open('LaTeX-sha.txt') as f:
            current_sha = f.read()
    except:
        current_sha = ''
    if fetched_sha != current_sha:
        print(prYellow("Có bản LaTeX khác hiện có, đang tải bản LaTeX mới..."))
        with open('LaTeX-sha.txt', 'w') as f:
            f.write(fetched_sha)
        return True
    elif not os.path.exists('LaTeX.txt'):
        return True
    return False


def download_latex():
    try:
        print(prYellow("Đang tải qua link Raw Github..."))
        with urlopen(latex_raw_github_link) as f:
            latex_dict = f.read().decode('utf-8')
    except:
        print(prRed("Oops Raw Github link không phản hồi :v"))
        print(prYellow("Đang tải qua link CDN..."))
        with urlopen(latex_cdn_link) as f:
            latex_dict = f.read().decode('utf-8')
    print(prGreen("Done"))
    with open('LaTeX.txt', 'w', encoding='utf-8') as f:
        f.write(latex_dict)
    print(prGreen("Đã tạo file LaTeX dict trong folder LaTeX với tên:" + prPurple('LaTeX.txt')))


def remove_latex(wd):
    # wd = working_dict
    # md = modified_dict
    md = [wd[0]]
    for i in range(1, len(wd)):
        if wd[i][0][0] not in lf:
            md += [wd[i]]
    return md


def add_latex(wd):
    # wd = working_dict
    # ld = latex_dict
    switch_pwd('./LaTeX')
    if should_download_latex():
        download_latex()
    with open('LaTeX.txt', 'r', encoding='utf-8') as f:
        ld = f.readlines()
    ld = split_dict(ld, '(.*)\\t(.*)\\t', 1)
    wd += ld
    switch_pwd('../')
    return wd


def latex_function(wd, a_lf):
    # wd = working_dict
    # a_lf = ask_latex_function
    if a_lf == 'R' or a_lf == 'U':
        print(prYellow("Đang xoá LaTeX trong Dictionary hiện tại..."))
        wd = remove_latex(wd)
        print(prGreen("Done"))
    if a_lf == 'A' or a_lf == 'U':
        print(prYellow("Đang thêm LaTeX vào Dictionary hiện tại..."))
        wd = add_latex(wd)
        print(prGreen("Done"))
    return wd