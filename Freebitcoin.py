#!/usr/bin/env python3
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

account_username = "user@email.com" #USERNAME OR BTC WALLETADDRESS 
account_password = "password" #PASSWORD FOR FREEBITCOIN

def Deletecookies():
    browser.delete_all_cookies()
    print ("Deleted Cookies")
    sleep(3)
pass

def clickbanners():
    sleep(3)
    browser.find_element_by_css_selector("html.js.no-touch.svg.inlinesvg.svgclippaths.no-ie8compat body div#push_notification_modal.reveal-modal.open div.push_notification_big div div div.pushpad_deny_button").click()
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/div/a[1]").click()
pass

#Readytogo
def readytogo():
    browser.maximize_window()
    sleep(1)
    print ("Maximized Browser")
    sleep(1)
    print ("Found Freebit website")
pass

# Login to the website
def login():
    try:
        elem10 = browser.find_element_by_class_name ("login_menu_button")
        if elem10.is_displayed():
            elem10.click()
            print("Clicked the Login Tab")
    except NoSuchElementException:
        print("...")
    sleep(1)
    username = browser.find_element_by_id("login_form_btc_address")
    sleep(1)
    username.send_keys(account_username)
    sleep(1)
    print ("Entered Username")
    sleep(1)
    password = browser.find_element_by_id("login_form_password")
    sleep(1)
    password.send_keys(account_password)
    sleep(1)
    print ("Entered Password")
    sleep(1)
    browser.find_element_by_css_selector("#login_button").click()
    sleep(1)
    print ("Logged into the website")
    sleep(5)
    try:
        elem = browser.find_element_by_css_selector(".push_notification_big > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)")
        if elem.is_displayed():
           elem.click()
           print("Clicked it the Banner!")
    except NoSuchElementException:
        print("...")
    sleep(1)
pass

#ClickFreeroll
def Freeroll():
    sleep(1)
    try:
        elem11 = browser.find_element_by_css_selector("#free_play_link_li > a:nth-child(1)")
        if elem11.is_displayed():
           elem11.click()
           print("Clicked The Free Btc Tab")
    except NoSuchElementException:
        print("...")
    browser.find_element_by_css_selector("#free_play_link_li > a:nth-child(1)").click()
    sleep(1)
    html = browser.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    sleep(5)
    print("Waiting to Click")
    try:######waits 1Hour until rolling clickable
     WebDriverWait(browser, 3600).until(EC.element_to_be_clickable(
     (By.CSS_SELECTOR, RollButton)))
    except NoSuchElementException:
      print("...")
    browser.find_element_by_css_selector(RollButton).click()
    sleep(5)
    browser.find_element_by_css_selector("#myModal22 > a:nth-child(2)").click()
    sleep(2)
pass

#PrintCollectedValues
def PrintValues():
    sleep(1)
    BTC = browser.find_element_by_id("winnings").text
    sleep(1)
    print(BTC + " Satoshi Gained")
    print(1)
    Balance = browser.find_element_by_css_selector(".balanceli").text
    sleep(1)
    print("Your Balance is " + Balance)
    sleep(1)
    BTCBALFILE = open('/home/user/Desktop/FreebitcoinFILE1.txt', 'w') #change the path to one suitable
    BTCBALFILE.write(Balance)
    BTCBALFILE.close()
pass

browser = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver') # change me to your chromedriver executable location
url = 'https://freebitco.in/?op=signup_page'
RollButton = "#free_play_form_button"
RollID = "free_play_form_button"
os.system('clear')
sleep(5)
browser.get(url)
sleep(10)
clickbanners()
sleep(2)
readytogo()
sleep(2)
login()
sleep(12)
Freeroll()
PrintValues()
sleep(2)
browser.quit()
sleep(2)
exit(0)
