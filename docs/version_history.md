# 🧓 VERSION HISTORY

# 1.3

-   **Beauty:**

    -   Pep8 format,... by deepsource bot
    -   Doc for function: Change to Eng, double quotes
    -   README.md change the download source code to latest release site

-   **Code changes:**
    -   Delete unused function _(Dict type for ... sort?)_
    -   Add request get timeout = 5 second for get LaTeX api
    -   Remove 'dictionary_zip_file' in [dictList](../dictionaryList.py)
    -   Input dict: all kind of files :v

# 1.2

-   Bruh rename [DictTools.py](../DictTool.py) to [main.py](../main.py)
-   Add decorate function
-   Add `requests` module to handle network status with LaTeX function, also add skip LaTeX if no LaTeX dict is found

# 1.1

-   **Code changes:**

    -   Fix format with MetaCharacter
    -   Move latex_format constant from [useConstants.py](../userConstants.py) to [constants.py](../src/constants.py)
    -   Add sort_dict_type: sort dict by `{sort}` or `{long}`
    -   Move latex_function & confirm_character_function compare user inputs into sub module, not in main
    -   Fix [userOptions.py](../userOptions.py) doesn't work

-   **Just for beauty:**

    -   Add more logs when executing, clearscreen for sections, change some print colours 🙂
    -   rename [main.py](../main.py) to [DictTools.py](../DictTool.py)
    -   Add more details about features in [README.md](README.md) _(let it be done tmr I'm going to sleep)_

# 1.0

-   Initiate with some unimplemented features...
-   **Feature:** Convert, remove LaTeX, confirm character function, sort _(ASCII only)_
