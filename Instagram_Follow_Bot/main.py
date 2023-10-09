import json
import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

with open("../../../Data.json") as file:
    data = json.load(file)
email = "YOUR EMAIL"
password = "YOUR PASSWORD"

chromedriver_path = "CHROMEDRIVER PATH"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

chrome_service = Service(chromedriver_path)
interested_in = "WHAT YOUR SEARCHING FOR"


class InstaFollower:
    def __init__(self):
        self.num_of_follower = None
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(4)
        user_name = self.driver.find_element(By.NAME, "username")
        user_name.send_keys(email)

        pass_input = self.driver.find_element(By.NAME, "password")
        pass_input.send_keys(password)
        pass_input.send_keys(Keys.ENTER)
       
        sleep(10)
        not_now_button = self.driver.find_element(By.CLASS_NAME, "_ac8f")
        not_now_button.click()
        sleep(3)
        another_not_now = self.driver.find_element(By.CLASS_NAME, "_a9_1")
        another_not_now.click()
        sleep(2)

    def find_follower(self):
        self.driver.get(f"https://www.instagram.com/{interested_in}/")
        sleep(7)
        self.num_of_follower = self.driver.find_element(By.XPATH,
                                                        '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span').get_attribute(
            "title").replace(',', '')

        followers = self.driver.find_element(By.XPATH,
                                             '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(3)

    def scroll_down(self):
        follower_accounts = self.driver.find_element(by="css selector", value='div._aano')
        sleep(3)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_accounts)
        sleep(4)

    def follow(self):
        for num in range(1, int(self.num_of_follower)):
            follow_button = self.driver.find_element(By.XPATH,
                                                     f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{num}]/div/div/div/div[3]/div/button/div/div')
            delay = random.randint(2, 4)
            sleep(delay)
            if follow_button.text == "Follow":
                if num % 5 == 0:
                    self.scroll_down()
                follow_button.click()
                sleep(3)

            else:
                print("already following")
                if num % 5 == 0:
                    self.scroll_down()
                # self.scroll_down()
                pass


bot = InstaFollower()
bot.login()
bot.find_follower()
bot.follow()
