import os
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector("input[name='firstname']").send_keys('Ivan')
browser.find_element_by_css_selector("input[name='lastname']").send_keys('Dmitriev')
browser.find_element_by_css_selector("input[name='email']").send_keys('azaza@azaza.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'example.txt')
loadfile = browser.find_element_by_css_selector('#file')
loadfile.send_keys(file_path)
browser.find_element_by_css_selector('.btn.btn-primary').click()
