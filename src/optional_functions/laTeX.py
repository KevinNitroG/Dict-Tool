import os
import requests

from json import loads

from ..constants import latex_format as lf
from ..constants import latex_api, latex_cdn_link, latex_raw_github_link
from ..pr import prGreen, prYellow, prRed, prPurple

from urllib.request import urlopen
from ..utils import switch_pwd, decorator
from ..compulsoryFunctions import split_dict


# SHORT VARS EXPLANATION

# wd = working_dict
# md = modified_dict
# a_lf = ask_latex_function

def should_download_latex():
    print(prYellow("Check status đến LaTeX repo..."))
    reponse = requests.get(latex_api)
    if not reponse.ok:
        print(prRed("Không thể kết nối đến LaTeX repo"))
        return False
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
    print(prGreen("Không update LaTeX dictionary hiện có"))
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
    print(prGreen("Đã tạo file LaTeX dict trong folder LaTeX với tên:" +
          prPurple('LaTeX.txt')))


@decorator
def remove_latex(wd):
    '''Xoá LaTeX'''
    md = [wd[0]]
    for i in range(1, len(wd)):
        if wd[i][0][0] not in lf:
            md += [wd[i]]
    return md


@decorator
def add_latex(wd):
    '''Thêm LaTeX'''
    switch_pwd('./LaTeX')
    if should_download_latex():
        download_latex()
    # If no LaTeX.txt file, skip add LaTeX
    if not os.path.exists('LaTeX.txt'):
        print(prRed("Skip add LaTeX ._."))
        return wd
    with open('LaTeX.txt', 'r', encoding='utf-8') as f:
        ld = f.readlines()
    ld = split_dict(ld[1:], '(?P<sort>.*)\\t(?P<long>.*)\\t')
    wd += ld
    switch_pwd('../')
    return wd


def latex_function(wd, a_lf):
    if a_lf == 'R' or a_lf == 'U':
        wd = remove_latex(wd)
    if a_lf == 'A' or a_lf == 'U':
        wd = add_latex(wd)
    return wd
