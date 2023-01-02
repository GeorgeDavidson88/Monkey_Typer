import time
import threading

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# The location of your driver.
PATH = "C:\Program Files (x86)\chromedriver.exe"

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://monkeytype.com")  # Gets the website.
driver.implicitly_wait(30)  # Waiting for the website to fully load.

delay = 0.01  # The time between each letter typed.


def letter_by_letter(delay):
    while (len(driver.find_element(By.ID, "words").find_element(By.CLASS_NAME, "word").text) != 0):
        word = [letter for letter in driver.find_element(
            By.CSS_SELECTOR, ".word.active").text] + [" "]

        for letter in word:
            # Sends the letter to the browser.
            ActionChains(driver).send_keys(letter).perform()
            time.sleep(delay)

    print("Program Stopped.")


while True:
    command = input("> ").lower()

    if command == "start":
        if len(driver.find_element(By.ID, "words").text) != 0:
            print("Started Program...")
            letter_by_letter(delay)
        else:
            print("Failed to start.")

    elif command == "quit":
        print("Quitting Program...")
        driver.quit()
        print("Almost Done...")
        break

    else:
        print(
            f"'{command}' is not recognized. Type 'start' to start typing or 'quit' to quit the program."
        )

print("Done")
