# Chrome sẽ là trình duyệt chạy test case
from selenium import webdriver  # import webdriver từ selenium package
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Đường dẫn đến chromedriver , mở trình duyệt Chrome lên
driver = webdriver.Chrome(executable_path='chromedriver.exe')


driver.get('https://vnexpress.net/')  # điều hướng đến trang chủ vnexpress

print(driver.title)  # in ra tiêu đề của trang web

# find_element : trả về thành phần đầu tiên tìm thấy, nếu ko tìm thấy ném vào ngoại lệ NoSuchElementException
# find_elements : trả về thành phần đầu tiên tìm thấy, nếu ko tìm thấy trả về danh sách rỗng


# Phân tích : Mỗi một bài báo được sử dụng bởi 1 thẻ 'article' có class là item-news, tiêu đề là thẻ 'h3'

articles = driver.find_elements(
    By.CSS_SELECTOR, 'article.item-news')  # trả về nhiều danh sách
for article in articles:  # vòng lặp duyệt từng danh sách
    try:
        # mỗi article chỉ lấy thẻ 'h3' chứa title
        title = article.find_element(By.TAG_NAME, 'h3').text
        # in ra thông tin mô tả
        description = article.find_element(By.TAG_NAME, 'p').text
        print(title)  # in ra các tiêu đề của mỗi bài báo
        print(description)
        print('=====')  # nếu kết quả in ra dấu thì các bài báo không có title
    except NoSuchElementException:
        pass

driver.quit()  # tắt Chrome
