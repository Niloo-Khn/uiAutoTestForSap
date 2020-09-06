from configparser import ConfigParser

file = './config.ini'
parser = ConfigParser()
parser.read(file)


user_name = parser['account']['user_name']
password = parser['account']['password']

auth_path = parser['setting']['auth_path']
login_path = parser['setting']['login_path']
projects_path = parser['setting']['projects_path']
url = parser['setting']['url_path']
path = parser['setting']['chromedriver_path']


success_message = parser['messages']['success_message']
failure_message = parser['messages']['fail_message']

task_name = parser['project']['task_name']
task_cat = parser['project']['task_cat']
task_status = parser['project']['task_status']