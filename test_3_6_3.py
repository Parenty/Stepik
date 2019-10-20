import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"
                                 ])
def test_func(browser, url):
    browser.get(url)
    answer = str(math.log(int(time.time())))
    WebDriverWait(browser, 12).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".quiz-component.ember-view")))
    browser.find_element(By.CSS_SELECTOR, '.textarea.ember-text-area.ember-view').send_keys(answer)

    # WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".textarea.ember-text-area.ember-view"), answer))
    btn = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
    btn.click()
    WebDriverWait(browser, 12).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    iscorrect = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    assert iscorrect == "Correct!", f"'{iscorrect}' is not same 'Correct!'"
