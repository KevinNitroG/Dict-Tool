# DICT CONVERTER ✨ ![GitHub repo size](https://img.shields.io/github/repo-size/KevinNitroG/Dict-Converter?style=for-the-badge) ![GitHub Repo stars](https://img.shields.io/github/stars/KevinNitroG/Dicter-Converter?style=for-the-badge)

Python script để chuyển đổi giữa các dictionary của bộ gõ _(Danh sách gõ tắt)_

## TÍNH NĂNG

-   Chuyển đổi giữa các dictionary trong danh sách [bộ gõ hỗ trợ](#bộ-gõ-hỗ-trợ)
-   Thêm gõ tắt cho [**LaTeX**](https://github.com/DenverCoder1/latex-gboard-dictionary)
-   Thêm / xoá confirm character sau cùng của **key**
    > ví dụ thay vì gõ `xl` -> `xin lỗi` thì sẽ thành `xlf` -> `xin lỗi`. Dễ kiểm soát gõ tắt hơn

## BỘ GÕ HỖ TRỢ

-   [UniKey](https://www.unikey.org/)
-   [EVKey](https://evkeyvn.com/)
-   [OpenKey](https://open-key.org/)
-   [Gboard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin)

## HƯỚNG DẪN

-   Cài đặt [Python](https://www.python.org/downloads/)
-   [Tải repo](https://github.com/KevinNitroG/Dict-Converter/archive/refs/heads/main.zip), giải nén
-   Chuẩn bị dictionary:
    -   **Cách 1:** Paste file dictionary vào folder repo _(Đuôi `.txt`)_
    -   **Cách 2:** Copy paste nội dung vào biến `your_dictionary` file [userConstant.py](../userConstants.py)
-   Chạy file [main.py](../main.py)

## LƯU Ý

-   Đối với **EVKey** do có ký tự đặc biệt ở dòng đầu tiên nên khi tạo file macro sẽ không dùng được. Hãy copy paste nội dung sau khi convert vào file macro của **EVKey** sẵn có
-   Đối với **Gboard**, nếu chọn tạo file macro sẽ có yêu cầu tạo file zip nén lại

## MORE...

-   Bạn có thể yêu cầu thêm bộ gõ tại [Issues](../../issues)
-   Có thể tạo pull request thêm về bộ gõ, format nằm trong file [dictionaryList.py](../dictionaryList.py)
