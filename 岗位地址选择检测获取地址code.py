from selenium import webdriver
import logging
import time
import os

log_time = time.strftime('%y-%m-%d', time.localtime(time.time()))
file_path = os.getcwd().replace('\\', '/')
log_path = file_path + '/log/' + log_time + '.log'
if not os.path.exists(file_path + '/log'):
    os.makedirs(file_path + '/log')
logging.basicConfig(filename=log_path, filemode="a+", level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(filename)s %(lineno)s %(message)s')
# 浏览器处理
path = file_path + '/chromedriver.exe'
# 等待时间
waittime = 5
# 学生账号密码
username = '18814887520'
password = 'qaz147'
# 地址
domain = 'http://www.xybsyw.com/'
# 开始
driver = webdriver.Chrome(executable_path=path)
# 设置等待时间
driver.set_script_timeout(waittime)
driver.set_page_load_timeout(10)
driver.implicitly_wait(waittime)
# 窗口最大化
driver.maximize_window()

driver.get(domain + 'login.xhtml')
driver.find_element_by_partial_link_text('我是学生').click()
driver.find_element_by_id('username').click()
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('login').click()
time.sleep(1)
driver.find_element_by_link_text('自主岗位库').click()
time.sleep(1)
driver.find_element_by_css_selector('span.inline_mid.text1').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_class_name('loc_csl_width').click()
list1 = []
for i in driver.find_elements_by_class_name('area-list ')[0].find_elements_by_tag_name('li'):
    name1 = i.text
    if i.text == '台湾':
        list1.append(i.find_element_by_tag_name('a').get_attribute("data-code"))
        continue
    i.click()
    for j in driver.find_elements_by_class_name('area-list ')[1].find_elements_by_tag_name('li'):
        name2 = j.text
        code2 = j.find_element_by_tag_name('a').get_attribute("data-code")
        j.click()
        if len(driver.find_elements_by_class_name('area-list ')) == 3:
            for k in driver.find_elements_by_class_name('area-list ')[2].find_elements_by_tag_name('li'):
                name3 = k.text
                code3 = k.find_element_by_tag_name('a').get_attribute("data-code")
                print(code3)
                list1.append(code3)
                if k == driver.find_elements_by_class_name('area-list ')[2].find_elements_by_tag_name('li').pop():
                    driver.find_element_by_class_name('tab').find_element_by_link_text(name2).click()
                    break
        else:
            driver.find_element_by_class_name('loc_csl_width').click()
            print(code2)
            list1.append(code2)
        if j == driver.find_elements_by_class_name('area-list ')[1].find_elements_by_tag_name('li').pop():
            driver.find_element_by_class_name('tab').find_element_by_link_text(name1).click()
            break
    if i == driver.find_elements_by_class_name('area-list ')[0].find_elements_by_tag_name('li').pop():
        print('stop')
        print(list1)
        print(len(list1))

with open(file_path + '/addresscode', 'w') as f:
    for i in list1:
        f.write(str(i) + '\n')
print('结束')
