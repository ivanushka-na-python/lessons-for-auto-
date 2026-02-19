from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
# sleep - плохая практика

# вроде как экономит время
# options.add_experimental_option('datach', True)# сессия не будет умирать 


@pytest.fixture()
def chrome_driver():
    options = Options()
    options.add_argument('--window-size=1440,900')
    driver = webdriver.Chrome(options=options)
    yield driver
    sleep(5)
    driver.quit()
    
 
def test_xpath(chrome_driver: webdriver.Chrome):
    chrome_driver.get('https://www.qa-practice.com/elements/input/simple')
    input_field = chrome_driver.find_element(By.XPATH, '//*[@placeholder="Submit me"]')
    input_field.send_keys('123123')
    input_field.send_keys(Keys.ENTER)
    result_text = chrome_driver.find_element(By.ID, 'result-text')
    assert result_text.text == '123123'


# driver.maximize_window()
# driver.set_window_size(450, 900)

# text_string = driver.find_element(By.ID, 'id_text_string')
# text_string.send_keys('test')
# text_string.submit()


# sleep(5)
# text_string = driver.find_element(By.ID, 'id_text_string')
# text_string.send_keys('test')
# text_string.send_keys(Keys.ENTER)
# sleep(5)
# result_text = driver.find_element(By.ID, 'result-text')
# assert result_text.text == 'test'


# print(driver.title)
# print(driver.current_url)
# # driver.page_source

# # sleep(5)
# driver.close()# закрывается текущая вкладка браузера 
# # driver.quit()# закрывается сам браузер 


