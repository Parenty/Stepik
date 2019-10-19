from selenium import webdriver
import math
import time



link = 'http://SunInJuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

x = int(browser.find_element_by_css_selector('#input_value').text)
rightanswer = str(math.log(math.fabs(12*math.sin(x))))

button = browser.find_element_by_tag_name("button")
browser.execute_script("window.scrollBy(0, 150);")
browser.find_element_by_css_selector('#answer').send_keys(rightanswer)
browser.find_element_by_css_selector('#robotCheckbox').click()
browser.find_element_by_css_selector('#robotsRule').click()
button.click()

time.sleep(30)