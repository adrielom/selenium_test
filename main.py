from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
import os


def wait_for_element_by (elementId, by, time = 10):
    field = WebDriverWait(driver, time).until(
        EC.presence_of_element_located((by, elementId))
    )
    return field

def set_storage():
    for key in list_of_local_storage_keys:
        set_individual_local_storage(key)

async def set_individual_local_storage(key):
    value = os.getenv(key)
    print(value)
    await driver.execute_async_script(f'window.localStorage.setItem({key},{value});')


# async def set_cookie(key, value):
#     await driver.execute_script(f"document.cookie='{key}={value}'")

load_dotenv(os.path.dirname(os.path.realpath(__file__)) + '.env')

user = os.getenv("USR")
password = os.getenv("PSWD")
target = os.getenv("TARGET")

driver = webdriver.Firefox()
targetURL = target
action = ActionChains(driver)

driver.get(targetURL)

# set_storage();    
driver.maximize_window()

try:
    login_input_field = wait_for_element_by("codigoEmpresa", By.ID)
    login_input_field.send_keys(user)
    access_number_input_field = wait_for_element_by("numeroAcesso", By.ID)
    access_number_input_field.send_keys(password, 20)

    action.move_to_element_with_offset(access_number_input_field, -120, 50).click().perform()

    action.move_to_element_with_offset(access_number_input_field, -0, 145, 20).click().perform()
finally:
    while (input() != "q"):
        pass
    driver.quit()



