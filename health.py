
"""
需求:
    模拟六院健康打卡(https://punchin.6thhosp.com:28011/#/)
"""
import os
from time import sleep
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions


# 定位用户名和密码input框
def report(usr, pwd):
    # 规避检测
    print(f'+++++++++++++{usr} 正在打卡中++++++++++++++')
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])

    service = Service(executable_path='./chromedriver', log_path='chrome.log')
    browser = Chrome(service=service, options=option)
    browser.get('https://punchin.6thhosp.com:28011/#/')

    # 定位用户名密码框
    username = browser.find_element(
        By.XPATH, '//*[@id="apply"]/div[2]/form/div[2]/div[2]/div/input')
    password = browser.find_element(
        By.XPATH, '//*[@id="apply"]/div[2]/form/div[3]/div[2]/div/input')
    # 传入用户名和密码
    username.send_keys(usr)
    password.send_keys(pwd)

    # 定位登录按钮并点击
    login_btn = browser.find_element(
        By.XPATH, '//*[@id="apply"]/div[2]/button')
    modify_window = browser.current_window_handle
    login_btn.click()
    sleep(2)

    # 定位修改请求并点击
    modify_request = browser.find_element(By.CLASS_NAME, 'healthyCheckOver')
    modify_window1 = browser.current_window_handle
    modify_request.click()
    sleep(2)

    # 点选单选框
    agree1 = browser.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/ul/li/div[1]/div/div[1]/div')
    agree2 = browser.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/ul/li/div[2]/div/div[4]/div')
    agree3 = browser.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/ul/li/div[3]/div/div[2]/div')
    agree4 = browser.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/ul/li/div[4]/div/div[1]/div')
    agree5 = browser.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/ul/li/div[4]/div/div[1]/div')
    agree6 = browser.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/ul/li/div[6]/div/div[1]/div')
    agree1.click()
    agree2.click()
    agree3.click()
    agree4.click()
    agree5.click()
    agree6.click()

    # 提交
    submit_btn = browser.find_element(
        By.XPATH, '//*[@id="app"]/div/div[3]/button')
    submit_btn.click()
    confirm_btn = browser.find_element(
        By.XPATH, '/html/body/div[4]/div[3]/button[2]')
    confirm_window = browser.current_window_handle
    confirm_btn.click()
    print(f'+++++++++++++{usr} 打卡完成!++++++++++++++')

    # 定位重新提交
    # resubmit = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/a')
    # resubmit_window = browser.current_window_handle
    # resubmit.click()

    # 弹窗处理
    # confirm_btn = browser.find_element(By.XPATH, '/html/body/div[4]/div[3]/button[2]')
    # confirm_window = browser.current_window_handle
    # confirm_btn.click()
    # sleep(2)
