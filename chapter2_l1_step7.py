from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)



    chest = browser.find_element_by_css_selector("#treasure")
    x=chest.get_attribute("valuex")
    y = calc(x)

    answ = browser.find_element_by_css_selector("#answer")
    answ.send_keys(y)
    chbox = browser.find_element_by_css_selector("#robotCheckbox")
    chbox.click()
    radbut = browser.find_element_by_css_selector("#robotsRule")
    radbut.click()
    sbm = browser.find_element_by_css_selector(".btn.btn-default")
    sbm.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
