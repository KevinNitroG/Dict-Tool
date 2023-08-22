import os

from ..pr import *
from ..utils import decorator


# SHORT VARS EXPLANATIONS

# fd = final_dictionary
# sd = selected_dict


def dictionary_compress(sd):
    import zipfile
    compress, ext = os.path.splitext(sd['dictionary_zip_file'].rstrip('-*'))
    compress = compress + '-Generated' + ext
    with zipfile.ZipFile(compress, 'w') as zip_ref:
        zip_ref.write(sd['macro'])
    print(prGreen("File zip macro đã được tạo ^^. Tên file: ") + prPurple(compress))


def evkey_special_create_file(content, evkey_macro):
    content = content[69:]
    from ..constants import EVKey_macro_first_line_binary as first_line
    with open(evkey_macro, 'wb') as f:
        f.write(first_line)
    with open(evkey_macro, 'a', encoding='utf-8') as f:
        f.write(content)
    print(prGreen("File macro đã được tạo ^^. Tên file: ") + prPurple(evkey_macro))


@decorator
def create_converted_dictionary_as_file(fd, sd):
    '''Tạo file dictionary'''
    _ = 'Y'
    if os.path.exists(sd['macro']):
        _ = input(
            "File macro đã hiện có tại đường dẫn hiện tại, có muốn ghi đè [Y/n]: ").upper()
    if _ in ('Y', ''):
        if sd['specific_name'] == 'e':
            evkey_special_create_file(fd, sd['macro'])
        else:
            with open(sd['macro'], 'w', encoding="utf-8") as file:
                file.write(fd)
            print(prGreen("File macro đã được tạo ^^. Tên file: ") +
                  prPurple(sd['macro']))
            if sd['dictionary_zip_file']:
                _ = input("Tạo file zip dictionary [Y/n]: ")
                if _ in ('Y', ''):
                    dictionary_compress(sd)
    else:
        print(prCyan("Đã huỷ tạo file macro"))
