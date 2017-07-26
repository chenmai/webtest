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

# 地址
domain = 'http://test2.xybsyw.com/'
# 开始
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()

majorname = '通信工程'
# majorname = '专业名称' + nowtime
majorcode = '专业代码' + nowtime

logging.info('新增专业 开始')

driver.get(domain + 'login.xhtml')
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
driver.get(domain + 'center/school/organization/specialtyManage.xhtml')
driver.implicitly_wait(waittime)
driver.find_element_by_id('addSpecialty').click()
time.sleep(1)
driver.find_elements_by_css_selector('input.textbox-text.textbox-text-readonly.validatebox-text.textbox-prompt')[
    0].click()
driver.find_element_by_id('_easyui_combobox_i1_0').click()
driver.find_element_by_css_selector('input.textbox-text.textbox-text-readonly.validatebox-text.textbox-prompt').click()
driver.find_element_by_id('_easyui_combobox_i2_0').click()
driver.find_element_by_id('specialtyName').send_keys(majorname)
driver.find_element_by_id('specialtyCode').send_keys(majorcode)
driver.find_element_by_id('saveSpecialtyBtn').click()
time.sleep(5)
driver.find_element_by_id('specialtysTable').find_elements_by_tag_name('tr')[0].find_element_by_class_name(
    'text3').find_element_by_link_text('删除').click()
driver.find_element_by_link_text('确认').click()
driver.quit()
logging.INFO('新增专业正常结束')