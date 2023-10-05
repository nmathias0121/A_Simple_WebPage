from pathlib import Path
import os

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of

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