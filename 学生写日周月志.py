# coding=utf-8
from selenium import webdriver
import logging
import time
import os

# 日志处理
log_time = time.strftime('%y-%m-%d', time.localtime(time.time()))
file_path = os.getcwd().replace('\\', '/')
log_path = file_path + '/log/' + log_time + '.log'
if not os.path.exists(file_path + '/log'):
    os.makedirs(file_path + '/log')
logging.basicConfig(filename=log_path, filemode="a+", level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(filename)s %(lineno)s %(message)s')
# 浏览器处理
path = file_path + '/chromedriver.exe'
# 隐式等待时间
waittime = 5
# 获取当前分钟
nowtime = time.strftime('%m%d%H%M', time.localtime(time.time()))
blog_daily_content = "今天至于我来说，具有特殊的意义；因为今天是我在某某某公司实习的第一天，也是我为不久的将来迈向社会大舞台的第一步，心里紧张而又激动。古人云天行健以自强不息，地势坤以厚德载物，对未来的实习生活，我愿意付出极大的热诚和努力。早晨八点我准时来到位于新华街某某某位置的某某公司，迎面就遇上当时面试我的王副总，副总热情地带我到了我的办公室旁，给我介绍了其它同事。我坐在公司为我准备的办公桌上开始熟悉负责人给我的一些资料。部门同事都开始陆续来上班，十分热情的跟我交流，他们看起来都很友好。我感觉心里也很轻松。但是当我接触到具体要处理的文件时，我深深的发现自己所具有的专业知识完全不够用，很多时候必须借助同事们的帮助，这让我认识到自己不足。整整一天我都在努力的听取领导和同事们的建议和帮助，对于公司基本业务和条例掌握的越来越精熟。一天的时间没感觉就一晃过去了，看起来不大的公司，里面的结构却很复杂。明天的工作我一定会更加用心，我在心里暗暗下定决心"
blog_weekly_content = "时间过的很快，一个星期就过去了，在这里，我们一行的同学一起先进行了为期3天的上岗前培训，培训的内容是：1.公司的基本情况，比如发展历史，人员数量，产品的卖点等等，2.公司的基本制度比如：上班时间，下班时间，节假日的放假情况等。3.公司的组成，有多个车间组成的：C1C2C3车间B1B2B3车间A1车间D1车间等。4.公司的业余安排等，每个星期的一三五晚上有最新的电影免费在二楼的食堂播放等。最后一天的下午和单位签署了劳动合同。工作的地点也去看过了，迷迷糊糊之间，一个星期过去了。很多东西在培训时说过，但有一点记住了，这个公司是10年前亚洲最大的此类专业的公司。公司的每一个车间，都和其他地方的小加工厂有的一比，这或许是骄傲的一个卖点吧。"
blog_monthly_content = "在整个实习生涯中，我本着对学生负责的态度尽心尽力做好每一件事情。自己在实践活动中得到了极大的提升，学到了许多书本上根本学不到的东西，受益匪浅，为以后做一名光荣的人民教师积累了宝贵的教学经验。但是，在教学过程中，时间把握不当，不能在有限的45分钟内完成教学目标任务，教学过程和教学环节常常出现疏漏的地方，给学生造成一定的理解困难。所以，我想，作为一名师范生，要真正走向了工作岗位，还需要自己以后两个月的实习不断地努力实践，追求进步。实习尽管辛苦忙碌，但却是对我人生的一大有益的尝试和磨练。最后，我要特别感谢辛勤指导我的武老师，是他让我学到了很多的教学知识，使我从稚嫩的教学走向了成熟的教学。同时，我也要向指导和勉励我的孙老师以及六中的老师们表示衷心的感谢和崇高的敬意!"
# 学生账号密码
username = '16175@xybsyw.com'
password = 'qaz147'
# 开始
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()
try:
    logging.info('学生写周日志的脚本开始')
    driver.get("http://test.xybsyw.com/login.xhtml")
    driver.implicitly_wait(waittime)
    driver.find_element_by_partial_link_text('我是学生').click()
    driver.find_element_by_id('username').click()
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login').click()
    driver.implicitly_wait(waittime)
    # 有蒙版，先等加载完全
    # 日志
    time.sleep(1)
    driver.find_element_by_link_text('日志').click()
    driver.implicitly_wait(waittime)
    driver.find_element_by_link_text('新建').click()
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(waittime)
    driver.find_element_by_id('title').send_keys('日志' + nowtime)
    driver.find_element_by_xpath('//*[@id="blogsForm"]/div/div[2]/dl/dd/div[1]/span/input[1]').click()
    driver.find_elements_by_class_name('combobox-item').pop().click()
    if driver.find_element_by_xpath('//*[@id="practiceDateDiv"]/span/input[1]').is_displayed():
        driver.find_element_by_xpath('//*[@id="practiceDateDiv"]/span/input[1]').click()
        driver.find_element_by_id('_easyui_combobox_i4_0').click()
    # 切换层级
    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    driver.find_element_by_class_name('ke-content').send_keys(blog_daily_content + nowtime)
    driver.switch_to.parent_frame()
    driver.find_element_by_id('applyBtn').click()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # 周志
    driver.find_element_by_link_text('周志').click()
    driver.implicitly_wait(waittime)
    driver.find_element_by_link_text('新建').click()
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(waittime)
    driver.find_element_by_id('title').send_keys('周志' + nowtime)
    driver.find_element_by_xpath('//*[@id="blogsForm"]/div/div[2]/dl/dd/div[1]/span/input[1]').click()
    driver.find_elements_by_class_name('combobox-item').pop().click()
    if driver.find_element_by_xpath('//*[@id="practiceDateDiv"]/span/input[1]').is_displayed():
        driver.find_element_by_xpath('//*[@id="practiceDateDiv"]/span/input[1]').click()
        driver.find_element_by_id('_easyui_combobox_i4_0').click()
    # 切换层级
    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    driver.find_element_by_class_name('ke-content').send_keys(blog_weekly_content + nowtime)
    driver.switch_to.parent_frame()
    driver.find_element_by_id('applyBtn').click()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # 月志
    driver.find_element_by_link_text('月志').click()
    driver.implicitly_wait(waittime)
    driver.find_element_by_link_text('新建').click()
    driver.switch_to_window(driver.window_handles[1])
    driver.implicitly_wait(waittime)
    driver.find_element_by_id('title').send_keys('月志' + nowtime)
    driver.find_element_by_xpath('//*[@id="blogsForm"]/div/div[2]/dl/dd/div[1]/span/input[1]').click()
    driver.find_elements_by_class_name('combobox-item').pop().click()
    if driver.find_element_by_xpath('//*[@id="practiceDateDiv"]/span/input[1]').is_displayed():
        driver.find_element_by_xpath('//*[@id="practiceDateDiv"]/span/input[1]').click()
        driver.find_element_by_id('_easyui_combobox_i4_0').click()
    # 切换层级
    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    driver.find_element_by_class_name('ke-content').send_keys(blog_monthly_content + nowtime)
    driver.switch_to.parent_frame()
    driver.find_element_by_id('applyBtn').click()
    driver.implicitly_wait(waittime)
    driver.find_element_by_link_text('退出').click()
    logging.info('学生写周日志的脚本正常结束')
except Exception as e:
    logging.error('学生写周日志的脚本错误')
finally:
    driver.quit()
