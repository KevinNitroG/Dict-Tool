def prBanner():
    from .constants import banner, maintainer, version
    print(prRed(banner))
    print(prLightBlue(f"                           By {maintainer}                       version {version}"))
    print()


def prTitle(v):
    v = ' ' + v + ' '
    print(prBold(prLightBlue(v.center(40, '-'))))
    print()



def prRed(v):
    return f"\033[0;31m{v}\033[0m"


def prYellow(v):
    return f"\033[1;33m{v}\033[0m"


def prGreen(v):
    return f"\033[0;32m{v}\033[0m"


def prCyan(v):
    return f"\033[0;36m{v}\033[0m"


def prLightBlue(v):
    return f"\033[1;34m{v}\033[0m"


def prBlue(v):
    return f"\033[0;34m{v}\033[0m"


def prLightPurple(v):
    return f"\033[1;35m{v}\033[0m"


def prPurple(v):
    return f"\033[0;35m{v}\033[0m"


def prBold(v):
    return f"\033[1m{v}\033[0m"


def prItalic(v):
    return f"\033[3m{v}\033[0m"


def prUnderline(v):
    return f"\033[4m{v}\033[0m"


def prUp(v):
    return f"\033[1A{v}033[0m"