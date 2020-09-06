
from URL.url import set_url
from Login.login import login_from_header
from Tasks.task import get_task_list, create_new_task, change_task_status


def change_created_task():
    set_url()
    login_from_header()
    get_task_list()
    create_new_task()
    change_task_status()


if __name__ == "__main__":
    change_created_task()
