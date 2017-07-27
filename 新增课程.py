# coding=utf-8
from selenium import webdriver
import logging
import time
import os

log_time = time.strftime('%y-%m-%d', time.localtime(time.time()))
file_path = os.getcwd().replace('\\', '/')
log_path = file_path + '/log/' + log_time + '.log'
if not os.path.exists(file_path + '/log'):
    os.makedirs(file_path + '/log')
logging.basicConfig(filename=log_path, filemode="a+", level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(filename)s %(lineno)s %(message)s')
console = logging.StreamHandler()
logging.getLogger('').addHandler(console)

# 浏览器处理
path = file_path + '/chromedriver.exe'
# 隐式等待时间
waittime = 5
# 获取当前秒
nowtime = time.strftime('%m%d%H%M%S', time.localtime(time.time()))

# 管理员账号密码
schoolname = '校友邦开放学院'
username = '开放学院'
password = 'wsx258'
# 数据准备
klassname = '课程名称' + nowtime
klasscode = '课程代码' + nowtime
klasscredit = 2
klassperiod = 3
# 地址
domain = 'http://test2.xybsyw.com/'
# 开始
driver = webdriver.Chrome(executable_path=path)
# 设置等待时间
driver.set_script_timeout(waittime)
driver.set_page_load_timeout(10)
driver.implicitly_wait(waittime)
# 窗口最大化
driver.maximize_window()

try:
    logging.info('新增课程 开始')

    driver.get(domain + 'login.xhtml')
    driver.find_element_by_link_text('我是老师').click()
    time.sleep(1)
    driver.find_element_by_id('schoolSelect').click()
    driver.find_element_by_id('schoolSelectsearch').send_keys(schoolname)
    driver.find_element_by_id('schoolSelectsearchB').click()
    time.sleep(1)
    driver.find_element_by_class_name('school-item').click()
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login').click()

    driver.get(domain + 'practice/school/practicecurriculum/curriculumManage.xhtml')
    driver.find_element_by_css_selector('span.inline_mid.text1').click()
    driver.find_element_by_id('name').send_keys(klassname)
    driver.find_element_by_id('cid').send_keys(klasscode)
    driver.find_elements_by_css_selector('input.textbox-text.validatebox-text.textbox-prompt')[0].click()
    driver.find_element_by_id('_easyui_tree_1').click()
    driver.find_elements_by_css_selector('input.textbox-text.validatebox-text.textbox-prompt')[1].send_keys(klasscredit)
    driver.find_elements_by_css_selector('input.textbox-text.validatebox-text.textbox-prompt')[2].click()
    driver.find_element_by_id('_easyui_combobox_i2_0').click()
    driver.find_elements_by_css_selector('span.textbox.numberbox')[1].find_element_by_css_selector(
        'input.textbox-text.validatebox-text.textbox-prompt').send_keys(klassperiod)
    driver.find_element_by_css_selector(
        'input.textbox-text.textbox-text-readonly.validatebox-text.textbox-prompt').click()
    driver.find_element_by_id('_easyui_combobox_i1_0').click()
    driver.find_element_by_css_selector(
        'input.textbox-text.textbox-text-readonly.validatebox-text.textbox-prompt').click()
    driver.find_element_by_id('_easyui_combobox_i3_0').click()
    driver.find_element_by_id('specialtyTool').click()
    driver.find_element_by_id('specialtyfacultyList').find_elements_by_tag_name('li')[1].click()
    driver.find_element_by_id('specialtyspecialtyList').find_elements_by_tag_name('li')[1].click()
    driver.find_element_by_id('specialtygradeList').find_elements_by_tag_name('li').pop().click()
    driver.find_element_by_id('specialtyconfirmAddTag').click()
    driver.find_element_by_id('submitButton').click()
    logging.info('新增课程 结束')
except:
    logging.error('新增课程 出错')
finally:
    driver.quit()
