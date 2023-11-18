import time
from typing import List

from seleniumwire import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument('--window-size=1920,1080')
    # chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("disable-gpu")
    service = Service()
    driver = webdriver.Chrome(options=chrome_options, service=service)

    driver.get('https://cloud.google.com/text-to-speech')
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "eRUHpf"))
    ts_app = driver.find_element(by=By.TAG_NAME, value="ts-app")
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', ts_app)
    speak_btn: WebElement = shadow_root.find_element(by=By.ID, value="button")
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(speak_btn, 0, 0).perform()
    speak_btn.click()
    WebDriverWait(driver, 10).until(ec.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")))
    checkbox = driver.find_element(by=By.CLASS_NAME, value="recaptcha-checkbox-border")
    checkbox.click()
    driver.wait_for_request("token", 30)
    with open("log.txt", "w") as f:
        for request in driver.requests:
            if request.response:
                f.writelines(f"{request.url}\n")
    driver.quit()


if __name__ == "__main__":
    main()

