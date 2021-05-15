# beautifME: Website gợi ý chu trình dưỡng da cho người mới bắt đầu bằng Django.

Đây là một dự án bài tập trên trường của nhóm, xây dựng một website gợi ý chu trình dưỡng da cơ bản gồm 5 bước: tẩy trang, sữa rửa mặt, lotion, kem dưỡng và kem chống nắng. Vì website chỉ mang tính chất tham khảo nên mọi người khi sử dụng hãy cân nhắc thật kĩ nhé ^^. Ngoài ra website còn tổng hợp các sản phẩm chăm sóc da và được phân loại theo các tình trạng da, cũng như loại da cùng với những thông tin tổng hợp từ nhiều nguồn tài liệu khác nhau cho mọi người tham khảo.

Bạn có thể truy cập đến đường dẫn https://www.beautifme.com

Để chạy web này trong localhost, các bạn cần có:
* Bạn đã cài đặt một IDE phù hợp: gợi ý của mình là VSCode.
* Cài đặt **Python** và **pip** trong máy (phiên bản nhóm sử dụng là **Python 3.6**)
* Lưu ý khi chạy localhost các bạn sẽ không thể sử dụng Database và SECRET_KEY của chúng mình.

Các bước thực hiện để chạy localhost: (tham khảo)
* Bước 1: Clone project về thông qua câu lệnh `https://github.com/ndklien/beautifME.git`
* Bước 2: (khuyến khích) Khởi tạo môi trường ảo virtualenv
  * Tạo một virtualenv `pip install virtualenv`
  * Tạo virtualenv **virtualenv venv** với **venv** là tên của virtualenv
* Bước 3: Cài đặt các package đi kèm với project: `pip install -r requirements.txt`
* Bước 4: Điều chỉnh cài đặt project.
   * Tạo vô file tên local.py và thả vào trong folder IE104_SC/settings/ *local.py sẽ chứa thiết lập database chạy localhost và SECRET_KEY để chạy ứng dụng*
   * Chỉnh sửa trong file \_init.py__\ trong folder IE104_SC/settings bằng cách thêm dòng lệnh `from .local import *`
   * Điều chỉnh trong file **manage.py** `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IE104_SC.settings.production')` thành `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IE104_SC.settings.local')`
   * *Tuy nhiên vì lí do bảo mật nên mình đã xóa SECRET_KEY đi, nếu không có SECRET_KEY thì project cũng không thể khởi chạy được.*
 * Bước 5: Thu thập các file tĩnh (css, html, js, img, v.v.) bằng `python manage.py collectstatic`.
 * Bước 6: Khởi chạy project bằng `python manage.py runserver`.

***Lưu ý**:*
* Để thoát virtualenv các bạn gõ lệnh deactivate.
* Để thoát runserver thì ta dùng lệnh Ctrl-C

Enjoy~ 😄
