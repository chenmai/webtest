from selenium import webdriver
import logging
import time
import os
from selenium.webdriver.common.action_chains import ActionChains

log_time = time.strftime('%y-%m-%d', time.localtime(time.time()))
file_path = os.getcwd().replace('\\', '/')
log_path = file_path + '/log/' + log_time + '.log'
if not os.path.exists(file_path + '/log'):
    os.makedirs(file_path + '/log')
logging.basicConfig(filename=log_path, filemode="a+", level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(filename)s %(lineno)s %(message)s')
# 浏览器处理
path = file_path + '/chromedriver.exe'
# 隐式等待时间
waittime = 5
# 获取当前分钟
nowtime = time.strftime('%m%d%H%M', time.localtime(time.time()))
# 数据
schoolname = '校友邦开放学院'
mark = '60'
level = '中'
remark = '评语' + nowtime
# 账号
username = '20000'
password = '123456'
# 开始
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()

logging.info('教师批阅周日志脚本开始')
try:
    driver.get("http://test.xybsyw.com/login.xhtml")
    driver.implicitly_wait(waittime)
    driver.find_element_by_link_text('我是老师').click()
    driver.find_element_by_id('schoolSelect').click()
    driver.find_element_by_id('schoolSelectsearch').send_keys(schoolname)
    driver.find_element_by_id('schoolSelectsearchB').click()
    driver.implicitly_wait(waittime)
    time.sleep(1)
    driver.find_element_by_class_name('school-item').click()
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login').click()
    driver.implicitly_wait(waittime)
    time.sleep(2)
    driver.find_element_by_link_text('周日志批阅').click()
    driver.implicitly_wait(waittime)
    time.sleep(1)
    driver.find_element_by_link_text('通过').click()

    try:
        driver.find_element_by_css_selector(
            'input.textbox-text,validatebox-text.textbox-prompt.validatebox-invalid').send_keys(
            mark)
    except:
        logging.info('不是百分制')
    try:
        driver.find_element_by_id('scoreTypeDiv').find_elements_by_tag_name('label')[2].click()
    except:
        logging.info('不是等级制')
    try:
        driver.find_element_by_id('fastReplyTextarea').send_keys(remark)
    except:
        logging.info('不需要评语')
    driver.find_element_by_id('reviewSuccessBtn').click()
    time.sleep(3)
    driver.find_element_by_id('passCount').click()
    driver.implicitly_wait(waittime)
    time.sleep(1)
    driver.find_element_by_link_text('重新退回修改').click()
    driver.find_element_by_id('backReason').send_keys('重新退回修改' + nowtime)
    driver.find_element_by_id('backEditBtn').click()
    time.sleep(3)
    driver.find_element_by_id('backCount').click()
    driver.implicitly_wait(waittime)
    time.sleep(1)
    driver.find_element_by_link_text('重新批阅').click()
    try:
        driver.find_element_by_css_selector(
            'input.textbox-text,validatebox-text.textbox-prompt.validatebox-invalid').send_keys(
            mark)
    except:
        logging.info('不是百分制')
    try:
        driver.find_element_by_id('scoreTypeDiv').find_elements_by_tag_name('label')[2].click()
    except:
        logging.info('不是等级制')
    try:
        driver.find_element_by_id('fastReplyTextarea').send_keys(remark)
    except:
        logging.info('不需要评语')
    driver.find_element_by_id('reviewSuccessBtn').click()
    ActionChains(driver).move_to_element(driver.find_element_by_id('emailE')).perform()
    driver.find_element_by_link_text('退出').click())
    logging.info('教师批阅日志正常结束')
except:
    logging.error('教师批阅日志出错')
finally:
    driver.quit()
