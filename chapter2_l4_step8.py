from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)
btn = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
browser.find_element_by_css_selector('#book').click()

x = int(browser.find_element_by_css_selector('#input_value').text)
rightanswer = str(math.log(math.fabs(12 * math.sin(x))))

button = browser.find_element_by_css_selector('#solve')
browser.execute_script("window.scrollBy(0, 150);")
browser.find_element_by_css_selector('#answer').send_keys(rightanswer)
button.click()

time.sleep(30)
