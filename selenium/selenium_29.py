from selenium import webdriver
from selenium.webdriver.common.print_page_options import PrintOptions

driver = webdriver.Edge()

print_options = PrintOptions()
print_options.page_ranges=['1-2']
driver.set_window_size(400,400)
driver.get("https://music.163.com")

base64code = driver.print_page(print_options)
print(base64code)