from pathlib import Path
import os

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

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