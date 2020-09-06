import time
from URL.url import driver
import str


def get_task_list():
    time.sleep(2)
    if driver.current_url == str.projects_path:
        driver.find_element_by_xpath(
            '//button[@title="Task List"]').click()  # also finding the task list from lobby but there is no ID and have to use xpath
        print("the task list was opened , test status: " + str.success_message)
    else:
        print("the project page didnt find , test status: " + str.failure_message)


def create_new_task():
    time.sleep(5)
    if driver.find_element_by_xpath(
            '//button[@class="btn btn-primary pl-2 ml-2"]'):  # check if the new task button in visible
        driver.find_element_by_xpath(
            '//button[@class="btn btn-primary pl-2 ml-2"]').click()  # looking for new task button
        time.sleep(5)  # it seems that loading new forms are taking time maybe some optimisation can be helpful
        driver.find_element_by_css_selector(
            'body > ngb-modal-window > div > div > add-task-dialog > ruum-modal-dialog > div > div > autoresize-textarea > textarea').send_keys(
            str.task_name)  # the dialog didnt have any id or name and had to use css, finding this input was really challenging
        time.sleep(5)
        driver.find_element_by_css_selector(
            'body > ngb-modal-window > div > div > add-task-dialog > ruum-modal-dialog > div > div > div.mt-4.position-relative.ng-star-inserted > input').click()  # and also this input
        time.sleep(5)
        driver.find_element_by_xpath(
            '//button[@class="dropdown-item active ng-star-inserted"]').click()  # select the input to have dropdown items
        time.sleep(5)
        driver.find_element_by_css_selector(
            'body > ngb-modal-window > div > div > add-task-dialog > ruum-modal-dialog > div > div > div:nth-child(5) > select-section > div > input').click()  # trying to open the dropdown input
        time.sleep(5)
        driver.find_element_by_id("ngb-typeahead-1-1").click()  # selecting an item from dropdown
        driver.find_element_by_xpath('//button[@class = "btn btn-lg btn-primary"]').click()  # the id is not generated for create task button
        time.sleep(5)
        if driver.find_element_by_xpath('//span[text()="' + str.task_name + '"]'):          # checking the created task in the list of tasks
            print("the create project , test status: " + str.success_message)
    else:
        print("the project didnt created , test status: " + str.failure_message)


def change_task_status():
    if driver.find_element_by_xpath('//span[text()="' + str.task_name + '"]'):  # check if the task is in the list, it should used id or name
        driver.find_element_by_xpath('//span[text()="' + str.task_name + '"]').click()  # select the task in list
        time.sleep(6)
        driver.find_element_by_xpath('//span[text()="' + str.task_cat + '"]').click()  # trying to open the task status dropdown box, actually its not correct way but we need a unique property for detection.
        time.sleep(3)
        driver.find_element_by_xpath('//span[text()="' + str.task_status + '"]').click()  # selecting the status by its name
        time.sleep(3)

        print("the task status changed , test status: " + str.success_message)
    else:
        print("the task didnt find , test status: " + str.failure_message)

    driver.quit()
