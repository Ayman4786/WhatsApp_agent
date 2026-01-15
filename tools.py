# tools.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

delay=random.randint(10,12)
class ToolError(Exception):
    pass

  
def _get_driver():
    options = Options()
    options.add_argument("--user-data-dir=C:/wp_chrome_profile")
    options.add_argument("--profile-directory=Default")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def send_whatsapp_message(contact_name: str, message: str) -> dict:
    if not contact_name or not message:
        raise ToolError("Invalid input")

    driver = _get_driver()
    wait = WebDriverWait(driver, 60)

    try:
        driver.get("https://web.whatsapp.com/")
        time.sleep(delay)

        # 1. Search box
        search_box = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div/div/div[1]/p')
            )
        )
        search_box.clear()
        time.sleep(delay)
        search_box.send_keys(contact_name)
        time.sleep(delay)
        search_box.send_keys(Keys.ENTER)

        # 2. Message box
        message_box = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div/div/div[3]/div/p')
            )
        )
        time.sleep(delay)
        message_box.send_keys(message)
        time.sleep(delay)
        message_box.send_keys(Keys.ENTER)
        time.sleep(delay)

        return {
            "status": "success",
            "detail": f"Message sent to {contact_name}"
        }

    except Exception as e:
        raise ToolError(str(e))

    finally:
        driver.quit()
