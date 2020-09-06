from URL.url import driver
import time
import str


def login_from_header():
    # set_url()  # start calling the url path and chromedriver
    driver.find_element_by_xpath(
        '//a[text()="Log in"]').click()  # ID in Login button can be more helpful in this option we can use href and text but using xpath is not recommended
    driver.switch_to_window(driver.window_handles[1])  # switch between tabs

    if driver.current_url == str.auth_path:  # check if the url changed to auth page

        driver.find_element_by_id("user-email").send_keys(str.user_name)
        driver.find_element_by_xpath(
            '//button[text()=" Next "]').click()  # ID in next button can be more helpful- the Next text contain 2 spaces
        time.sleep(3)

        if driver.current_url == str.login_path:  # check if the url changed to login page

            driver.find_element_by_id("user-passowrd").send_keys(str.password)
            driver.find_element_by_xpath('//button[text()=" Log In "]').click()  # ID in Login button can be more helpful- the Login text contain 2 spaces

            print("the login test status: " + str.success_message)

        else:
            print("authorization test " + str.failure_message)
    else:

        print(" login test " + str.failure_message)
