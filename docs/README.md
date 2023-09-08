<p align="center">
    <img src="https://img.shields.io/github/repo-size/KevinNitroG/Dict-Tool?style=for-the-badge" alt="Repo Size"/>
    <img src="https://img.shields.io/github/stars/KevinNitroG/Dict-Tool?style=for-the-badge" alt="Repo Star"/>
    <a href="https://github.com/KevinNitroG/Dict-Tool/archive/refs/heads/main.zip">
        <img src="https://img.shields.io/badge/dict_convert-download-yellow?style=for-the-badge" alt="cosmetic"/>
    </a>
</p>

<pre align="center">
██████╗ ██╗ ██████╗████████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔══██╗██║██╔════╝╚══██╔══╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██║  ██║██║██║        ██║          ██║   ██║   ██║██║   ██║██║     ███████╗
██║  ██║██║██║        ██║          ██║   ██║   ██║██║   ██║██║     ╚════██║
██████╔╝██║╚██████╗   ██║          ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═════╝ ╚═╝ ╚═════╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
</pre>

<h3 align="center">Python script giúp quản lý, chuyển đổi từ điển <i>(bảng gõ tắt)</i> giữa các bộ gõ</h3>

---

## 🪶 TÍNH NĂNG

-   Chuyển đổi giữa các dictionary trong danh sách [**bộ gõ hỗ trợ**](#bộ-gõ-hỗ-trợ-📃)
-   Thêm / xoá gõ tắt cho [**LaTeX**][LaTeX_Gboard_repo_link]
-   Thêm / xoá confirm character sau cùng của **key**
    > ví dụ thay vì gõ `xl` -> `xin lỗi` thì sẽ thành `xlf` -> `xin lỗi`. Dễ kiểm soát gõ tắt hơn
-   Sắp xếp lại danh sách gõ tắt theo thứ tự [**ASCII**][ASCII_information]

## 📃 BỘ GÕ HỖ TRỢ

-   [UniKey](https://www.unikey.org/)
-   [EVKey](https://evkeyvn.com/)
-   [OpenKey](https://open-key.org/)
-   [Gboard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin)

---

## 📄 HƯỚNG DẪN

### 🐣 CƠ BẢN

1.  Cài đặt [Python](https://www.python.org/downloads/)
2.  [Tải soure code về](https://github.com/KevinNitroG/Dict-Tool/releases/latest), giải nén, vào folder repo
3.  Mở terminal chạy `pip install -r requirements.txt`
4.  Chuẩn bị dictionary:
    -   **Cách 1:** Paste file dictionary vào folder [Dictionary In](../Dictionary%20In/)
    -   **Cách 2:** Copy paste nội dung vào biến `your_dictionary` file [userConstant.py](../userConstants.py)
        > Script sẽ ưu tiên trong file [userConstant.py](../userConstants.py)
5.  Chạy file [main.py](../main.py)
6.  Dictionary sẽ được tạo ra ở folder [Dictionary Out](../Dictionary%20Out/)

> **Note**
>
> Các yêu cầu `[Y/n]`, `[y/N]` nhập hoa thường đều được, mặc định sẽ theo lựa chọn **in hoa**<br>Bất kì kí tự nào khác sẽ chọn in thường `[y]` hoặc `[n]`
>
> Yêu cầu `[a]dd / [r]emove / [u]pdate / [S]kip` nhập hoa thường đều được<br>bất kì kí tự nào khác `a`, `r`, `u` _(hoặc in hoa)_ sẽ chọn `[S]kip`

### 🦾 NÂNG CAO

-   Có thể tải [latest source code](https://github.com/KevinNitroG/Dict-Tool/archive/refs/heads/main.zip) về _(Bản beta kiểu vậy)_
-   Có thể thay đổi một vài biến trong file [`userConstants.py`](../userConstants.py) và thêm các dictionary khác ở file [`dictionaryList.py`](../dictionaryList.py)
-   Có thể tuỳ chọn option sẵn để skip qua bước script hỏi chọn options [userOptions.py](../userOptions.py)
    > Hãy **rename** file [userOptions.py.sample](../userOptions.py.sample) thành `userOptions.py`<br>Lưu ý tuỳ chọn trong file này đều là in hoa

---

## 🥰 MORE...

-   Có thể yêu cầu thêm bộ gõ tại [Issues](https://github.com/KevinNitroG/Dict-Tool/issues)
-   Có thể tạo **Pull Request** thêm về bộ gõ, format nằm trong file [dictionaryList.py](../dictionaryList.py)

---

## 🧓 VERSION HISTORY

Go to here 👉: [version_history.md](version_history.md)

---

## 😫 TO DO

-   [ ] Sort by Unicode
-   [ ] Better way to handle user input?

<!-- Foot hyperlinks -->

[LaTeX_Gboard_repo_link]: https://github.com/DenverCoder1/latex-gboard-dictionary
[ASCII_information]: https://www.vlsifacts.com/wp-content/uploads/2023/02/ASCII-Code.png
