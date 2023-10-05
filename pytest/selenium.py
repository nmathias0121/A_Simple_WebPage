from pathlib import Path
import os

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.by import By

@contextmanager
def wait_for_page_load(driver, timeout=30):
    old_page = driver.find_element_by_tag_name('html')
    yield
    WebDriverWait(driver, timeout).until( staleness_of(old_page) )

def test_nonsecret_scenario():
    # get landing page url
    test_dir = os.getcwd()
    index_path = os.path.join(test_dir, "page", "index.html")
    landing_page = Path(index_path).as_uri()

    # construct headless chrome driver
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(landing_page)

    wait_for_page_load(driver)

    # fill the form and submit
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