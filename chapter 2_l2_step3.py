from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects2.html'
browser = webdriver.Chrome()
browser.get(link)

ln(abs(12*sin(x)))
select = Select(browser.find_element_by_css_selector('#dropdown'))
number1 = int(browser.find_element_by_css_selector('#num1').text)
number2 = int(browser.find_element_by_css_selector('#num2').text)
select.select_by_value(str(number1+number2))
browser.find_element_by_css_selector('button.btn.btn-default').click()
time.sleep(30)
