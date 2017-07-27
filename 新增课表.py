# coding=utf-8
import win32gui
import win32con
from selenium import webdriver
import logging
import time
import os

log_time = time.strftime('%y-%m-%d', time.localtime(time.time()))
upplanfilename = os.getcwd() + '\\' + '设置考核规则里上传附件.docx'
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
schedulename = '课表名称' + nowtime
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

logging.info('新增课表 开始')

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

driver.find_element_by_name('seeNotice').click()
# driver.find_element_by_css_selector('span.inline_mid.text1').click()
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element_by_css_selector('input.textbox-text.validatebox-text.textbox-prompt.validatebox-invalid').send_keys(schedulename)
# driver.find_element_by_id('selectCourse').click()
# time.sleep(1)
# driver.find_element_by_id('curriculumsList').find_element_by_css_selector('span.text1').click()
# driver.find_element_by_id('courseConfirm').click()
# driver.find_element_by_id('selectClassArea').click()
# time.sleep(1)
# driver.find_element_by_id('classesTable').find_element_by_css_selector('span.text1').click()
# driver.find_element_by_id('saveClassBtn').click()
# driver.find_element_by_id('selectDirectorTeacher').click()
# time.sleep(1)
# driver.find_element_by_id('teacherTable').find_element_by_css_selector('div.icheckbox_square-red').click()
# driver.find_element_by_id('confirmTeacher').click()
# driver.find_element_by_css_selector('span.textbox.textbox-invalid.combo.datebox').click()
# driver.find_element_by_class_name('datebox-button').find_element_by_tag_name('a').click()
# driver.find_element_by_css_selector('span.textbox.textbox-invalid.combo.datebox').click()
# driver.find_elements_by_class_name('calendar-nextmonth').pop().click()
# driver.find_elements_by_css_selector('td.calendar-day.calendar-sunday.calendar-first').pop().click()
# driver.find_element_by_id('addCourseBtn').click()
# driver.find_element_by_id('setTypeLink').click()
driver.find_element_by_link_text('设置考核规则').click()
driver.switch_to.window(driver.window_handles[1])
# driver.find_elements_by_css_selector('div.icheckbox_square-red').pop().click()
# driver.find_elements_by_css_selector('a.inline_mid.upbtn.mgl_30').pop().click()
# time.sleep(1)
# driver.find_element_by_id('ruleList').click()
# driver.find_element_by_css_selector('span.text1').click()
# driver.find_element_by_id('selectRuleBtn').click()
# driver.find_element_by_css_selector('span.textbox.textbox-invalid.combo').click()
# driver.find_element_by_id('_easyui_combobox_i1_9').click()
driver.find_element_by_id('upPlanFile').click()

dialog = win32gui.FindWindow('#32770', u'打开')
ComboBoxEx32 = win32gui.FindWindowEx(dialog, None, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, None, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, None, 'Edit', None)
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, upplanfilename)
button = win32gui.FindWindowEx(dialog, None, 'Button', '打开(&O)')
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
time.sleep(3)
# driver.find_element_by_css_selector('input.base_btn.base_w_300.saveButton').click()
raise SyntaxError
