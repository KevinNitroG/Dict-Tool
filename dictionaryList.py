dictionary_list = [
    {
        'name': 'RAW',                          # name of app
        'specific_name': 'r',                   # specific name to easier to call in script, anything you like
        # 'delimiter': '#delimiter#',             # the delimiter between sort_word and long_word
        # 're_compile_pattern': r'(.+)(##)(.+)',  # for match the re.compile
        # 'format': 1,                            # 1 is sort_word then long_word, 2 is long_word then sort_word
        'format': r'{sort}#raw#{long}',
        'first_line': r'#raw#',                 # the first line in the macro file
        'macro': 'raw_macro.txt',               # macro file name
        'dictionary_zip_file': ''               # if the app require zip dictionary like Gboard
    },
    {
        'name': 'Gboard - All languages',
        'specific_name': 'g',
        # 'delimiter': '\t',
        # 're_compile_pattern': r'(.+)(\t)(.+)',
        # 'format': 1,
        'format': r'{sort}{long}',
        'first_line': r'# Gboard Dictionary version:1',
        'macro': 'dictionary.txt',
        'dictionary_zip_file': 'PersonalDictionary-*.zip'
    },
    {
        'name': 'OpenKey',
        'specific_name': 'o',
        # 'delimiter': ':',
        # 're_compile_pattern': r'(.+)(:)(.+)',
        # 'format': 1,
        'format': r'{sort}{long}',
        'first_line': r';Compatible OpenKey Macro Data file for UniKey*** version=1 ***',
        'macro': 'OpenKeyMacro.txt',
        'dictionary_zip_file': ''
    },
    {
        'name': 'EVKey',
        'specific_name': 'e',
        # 'delimiter': '||',
        # 're_compile_pattern': r'(.+)(\|\|)(.+)',
        # 'format': 1,
        'format': r'{sort}{long}',
        'first_line': r'<<Đây là dòng làm dấu Unicode, không được sửa hoặc xoá dòng này>>',
        'macro': 'evkmacro.txt',
        'dictionary_zip_file': ''
    },
    {
        'name': 'UniKey',
        'specific_name': 'u',
        # 'delimiter': ':',
        # 're_compile_pattern': r'(.+)(:)(.+)',
        # 'format': 1,
        'format': r'{sort}{long}',
        'first_line': r';DO NOT DELETE THIS LINE*** version=1 ***',
        'macro': 'ukmacro.txt',
        'dictionary_zip_file': ''
    }
]