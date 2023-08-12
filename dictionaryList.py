# Note that if you use other Gboard language format, just add and change the 'name', 'format', don't change others if you don't know how the code works, especially don't change 'specific_name'
# If any key doesn't have value, then keep it as ''

dictionary_list = [
    {
        'name': 'RAW',                          # name of app
        'specific_name': 'r',                   # specific name to easier to call in script, anything you like, you can leave it to ''
        'format': '{sort}#raw#{long}',          # the format of the key and value to replace
        'first_line': r'#raw#',                 # the first line in the macro file
        'macro': 'raw_macro.txt',               # macro file name
        'dictionary_zip_file': ''               # if the app require zip dictionary like Gboard
    },
    {
        'name': 'Gboard - All languages',       # please don't change this position of Gboard - All languages
        'specific_name': 'g',
        'format': '{sort}\t{long}\t',
        'first_line': r'# Gboard Dictionary version:1',
        'macro': 'dictionary.txt',
        'dictionary_zip_file': 'PersonalDictionary-*.zip'
    },
    {
        'name': 'Gboard - Vietnamese',
        'specific_name': 'g',
        'format': '{sort}\t{long}\tvi',
        'first_line': r'# Gboard Dictionary version:1',
        'macro': 'dictionary.txt',
        'dictionary_zip_file': 'PersonalDictionary-*.zip'
    },
    {
        'name': 'OpenKey',
        'specific_name': 'o',
        'format': '{sort}:{long}',
        'first_line': r';Compatible OpenKey Macro Data file for UniKey*** version=1 ***',
        'macro': 'OpenKeyMacro.txt',
        'dictionary_zip_file': ''
    },
    {
        'name': 'EVKey',
        'specific_name': 'e',
        'format': '{sort}||{long}',
        'first_line': r'<<Đây là dòng làm dấu Unicode, không được sửa hoặc xoá dòng này>>',
        'macro': 'evkmacro.txt',
        'dictionary_zip_file': ''
    },
    {
        'name': 'UniKey',
        'specific_name': 'u',
        'format': '{sort}:{long}',
        'first_line': r';DO NOT DELETE THIS LINE*** version=1 ***',
        'macro': 'ukmacro.txt',
        'dictionary_zip_file': ''
    }
]