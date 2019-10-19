from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_css_selector('.trollface.btn.btn-primary').click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x = int(browser.find_element_by_css_selector('#input_value').text)
rightanswer = str(math.log(math.fabs(12 * math.sin(x))))

button = browser.find_element_by_tag_name("button")
browser.execute_script("window.scrollBy(0, 150);")
browser.find_element_by_css_selector('#answer').send_keys(rightanswer)
button.click()

time.sleep(30)
