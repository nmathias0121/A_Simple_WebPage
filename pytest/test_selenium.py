from pathlib import Path
import os
import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.by import By

def construct_headless_chrome_driver():
    service = Service(executable_path='./chromedriver.exe')
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    return webdriver.Chrome(service=service, options=options)


def get_landing_page_url():
    test_dir = os.getcwd()
    index_path = os.path.join(test_dir, "web-page", "parent_page.html")
    index_uri = Path(index_path).as_uri()
    return index_uri


# As demonstrated in the linked web page from the course assignment
@contextmanager
def wait_for_page_load(driver, timeout=30):
    old_page = driver.find_element_by_tag_name('html')
    yield
    WebDriverWait(driver, timeout).until( staleness_of(old_page) )


def test_nonsecret_scenario():
    landing_page =  get_landing_page_url()
    driver = construct_headless_chrome_driver()

    driver.get(landing_page)
    wait_for_page_load(driver)

    # You can place additional test code here to drive this one test
    preferred_name = driver.find_element(By.ID, "preferredname")
    preferred_name.send_keys('Neil')

    food = driver.find_element(By.ID,'food')
    food.send_keys('pizza')

    secret = driver.find_element(By.ID,'secret')
    secret.send_keys('imagine')

    submit_button = driver.find_element(By.ID,'submit')
    submit_button.click()

    wait_for_page_load(driver)

    k = driver.current_url
    assert 'web-page/response_page.html?preferredname=Neil&food=pizza&secret=imagine' in k

    thank_name = driver.find_element(By.ID, 'thankname')
    assert thank_name.text == 'Neil'

    food_ploy = driver.find_element(By.ID, 'foodploy')
    assert food_ploy.text == 'pizza'

    driver.quit()


def test_secret_scenario():
    landing_page = get_landing_page_url()
    driver = construct_headless_chrome_driver()

    driver.get(landing_page)

    preferred_name = driver.find_element(By.ID, 'preferredname')
    preferred_name.send_keys('Neil')

    food = driver.find_element(By.ID,'food')
    food.send_keys('pizza')

    secret = driver.find_element(By.ID,'secret')
    secret.send_keys('magic')

    submit_button = driver.find_element(By.ID,'submit')
    submit_button.click()

    wait_for_page_load(driver)

    k = driver.current_url
    assert 'web-page/response_page.html?preferredname=Neil&food=pizza&secret=magic' in k

    thank_name = driver.find_element(By.ID, 'thankname')
    assert thank_name.text == 'Neil'

    food_ploy = driver.find_element(By.ID, 'foodploy')
    assert food_ploy.text == 'pizza'

    secret_button = driver.find_element(By.ID, 'secretButton')
    secret_button.click()

    time.sleep(1) 

    j = driver.current_url
    assert 'web-page/secret_page.html?preferredname=Neil&secret=magic' in j

    thank_name = driver.find_element(By.ID, 'thankname')
    assert thank_name.text == 'Neil'

    secret = driver.find_element(By.ID,'secret')
    assert secret.text == 'magic'

    driver.quit()

