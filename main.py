import os
import threading
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# The location of your driver.
PATH = os.path.join("driver", "chromedriver.exe")

service = Service(executable_path=PATH)
driver = webdriver.Chrome()

driver.get("https://monkeytype.com")  # Gets the website.
driver.implicitly_wait(30)  # Waiting for the website to fully load.


class Main:
    def __init__(self):
        self.typing = False
        self.delay = 0.01  # The time between each letter typed.

    def typer(self):
        while True:
            if self.typing and (len(driver.find_element(By.ID, "words").find_element(By.CLASS_NAME, "word").text) != 0):
                word = [letter for letter in driver.find_element(
                    By.CSS_SELECTOR, ".word.active").text] + [" "]

                for letter in word:
                    # Sends the letter to the browser.
                    ActionChains(driver).send_keys(letter).perform()
            else:
                self.typing = False

            time.sleep(self.delay)

    def main_loop(self):
        while True:
            command = input("> ").lower()

            if command == "start":
                if len(driver.find_element(By.ID, "words").text) != 0:
                    self.typing = True
                    print("Started Program...")
                else:
                    print("Failed to start.")

            elif command == "stop":
                self.typing = False
                print("Program Stoped.")

            elif command == "quit":
                print("Quitting Program...")
                driver.quit()
                print("Almost Done...")
                break

            elif command == "help":
                print("""'start' - Start Typing.
'stop' - Stop Typing.
'quit' - Quit Program.""")
            else:
                print(
                    f"'{command}' is not recognized. Type 'help' to see commands.")

        print("Done")


def main():
    main = Main()

    typer_thred = threading.Thread(target=main.typer)
    typer_thred.daemon = True
    typer_thred.start()

    main.main_loop()


if __name__ == "__main__":
    main()
