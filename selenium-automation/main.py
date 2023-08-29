import undetected_chromedriver as chromedriver
import time
import random
from fp.fp import FreeProxy
from undetected_chromedriver import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

# timeout is high due to usage of free proxies
TIMEOUT = 15
# this is risky for production but for this example it is fine
IGNORED_EXCEPTIONS=(NoSuchElementException, TimeoutException,)

# for buttons
def search_for_element_and_click(browser ,by, selector, _=None):
    element = WebDriverWait(browser, TIMEOUT, ignored_exceptions=IGNORED_EXCEPTIONS).until(EC.presence_of_element_located((by, selector)))
    time.sleep(2+(random.randint(0,200)/100))
    element.click()

# for text fields
def search_for_element_and_send_keys(browser ,by, selector, input_):
    element = WebDriverWait(browser, TIMEOUT, ignored_exceptions=IGNORED_EXCEPTIONS).until(EC.presence_of_element_located((by, selector)))
    time.sleep(2+(random.randint(0,200)/100))
    element.click()
    element.send_keys(input_)

# fetching a free proxy
proxy = FreeProxy(timeout=3).get()

# setting up browser
opt = Options()
opt.add_argument("--proxy-server="+proxy)

# get driver object
# as an example i will be using a news website
driver = chromedriver.Chrome(headless=False,use_subprocess=False, options=opt)
driver.get('https://fludter.blogspot.com/')

# click on the first article
search_for_element_and_click(driver, By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/main/div/div/div[1]/article/div/div/div[1]/h3/a')

# wait until the page loads
search_for_element_and_click(driver, By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/main/div/div/div/article/div/div/div[3]/div[2]/div/h3')

# take a screenshot
driver.save_screenshot("fludter-blog.png")

# close driver
driver.close()