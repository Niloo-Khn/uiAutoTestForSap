from selenium import webdriver
import str

url = str.url
path = str.path

driver = webdriver.Chrome()


def set_url():
    driver.maximize_window()
    driver.get(url)
    if driver.current_url == url:
        print("the '"+url+"' was opened , test status: " + str.success_message)
    else:
        print("the '"+url+"' didnt find , test status: " + str.failure_message)
