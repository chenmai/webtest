# coding=utf-8
import logging
import time
from selenium import webdriver, common
import os
import win32gui
import win32con

log_time = time.strftime('%y-%m-%d', time.localtime(time.time()))
reportname = os.getcwd() + '\\' + '思政理论课暑期社会实践报告（论文）.doc'
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
# 数据准备
nowtime = time.strftime('%m%d%H%M', time.localtime(time.time()))

# 学生账号密码
username = '16175@xybsyw.com'
password = 'qaz147'
# 开始
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()
logging.info('学生预实习报告的脚本开始')

try:
    driver.get("http://test.xybsyw.com/login.xhtml")
    driver.implicitly_wait(waittime)
    driver.find_element_by_partial_link_text('我是学生').click()
    driver.find_element_by_id('username').click()
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login').click()
    driver.implicitly_wait(waittime)
    # 有蒙版，先等加载完全
    time.sleep(1)
    driver.find_element_by_link_text('预实习报告').click()
    driver.implicitly_wait(waittime)
    try:
        driver.find_element_by_link_text('尾页').click()
        driver.implicitly_wait(waittime)
        time.sleep(1)
    except Exception as e:
        logging.info('预实习报告只有一页，没有尾页' + str(e))
    driver.find_elements_by_partial_link_text('提交预实习报告').pop().click()
    driver.switch_to.window(driver.window_handles[1])

    try:
        if driver.find_element_by_css_selector('span.error_text').is_displayed():
            print('显示了错误信息')
            raise SyntaxError
    except common.exceptions.WebDriverException:
        logging.info('正常进入提交页')
    driver.find_element_by_link_text('下载预实习报告模板').click()
    driver.find_element_by_link_text('下一步，上传预实习报告').click()
    driver.implicitly_wait(waittime)
    driver.find_element_by_id('selectFile').click()
    # 处理上传
    time.sleep(3)
    dialog = win32gui.FindWindow('#32770', u'打开')
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, None, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, None, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, None, 'Edit', None)
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, reportname)
    button = win32gui.FindWindowEx(dialog, None, 'Button', '打开(&O)')
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    # 上传文件等待
    time.sleep(3)
    driver.find_element_by_id('submitFile').click()
    driver.implicitly_wait(waittime)
    if driver.find_element_by_class_name('import_success').is_enabled():
        logging.info('预实习报告提交成功')
    time.sleep(3)
    driver.find_element_by_link_text('退出').click()
    logging.info('学生预实习报告的脚本正常结束')
except SyntaxError:
    logging.error('提交实习报告出错，可能模板不存在或者规则问题')
except Exception as e:
    logging.error('学生实习报告的脚本错误' + ':' + str(e))
finally:
    driver.quit()
