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
# 获取当前分钟
nowtime = time.strftime('%m%d%H%M', time.localtime(time.time()))
# 数据准备
enterpriseName = '单位名称' + nowtime
name = '实习岗位' + nowtime
linkman = '企业联系人' + nowtime
enterpriseTel = '18814887520'
enterpriseEmail = 'chenmai@xybsyw.com'
trainer = '企业导师' + nowtime
trainerTel = '18814887520'
salary = '3000'
responsibilities = '1、负责产品的市场渠道开拓与销售工作，执行并完成公司产品年度销售计划。 ' \
                   '2、根据公司市场营销战略，提升销售价值，控制成本，扩大产品在所负责区域的销售，积极完成销售量指标，扩大产品市场占有率；' \
                   '3、与客户保持良好沟通，实时把握客户需求。为客户提供主动、热情、满意、周到的服务' \
                   '4、根据公司产品、价格及市场策略，独立处置询盘、报价、合同条款的协商及合同签订等事宜。在执行合同过程中，协调并监督公司各职能部门操作。' \
                   '5、动态把握市场价格，定期向公司提供市场分析及预测报告和个人工作周报。' \
                   '6、维护和开拓新的销售渠道和新客户，自主开发及拓展上下游用户，尤其是终端用户。' \
                   '7、收集一线营销信息和用户意见，对公司营销策略、售后服务、等提出参考意见。'
address = '北京市东城区东华门街道天安门'
# 学生账号密码
username = '9060@xybsyw.com'
password = 'qaz147'
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
    i.click()
    for j in driver.find_elements_by_class_name('area-list ')[1].find_elements_by_tag_name('li'):
        name2 = j.text
        j.click()
        if len(driver.find_elements_by_class_name('area-list ')) == 3:
            for k in driver.find_elements_by_class_name('area-list ')[2].find_elements_by_tag_name('li'):
                name3 = k.text
                print(name3)
                list1.append(name3)
                if k == driver.find_elements_by_class_name('area-list ')[2].find_elements_by_tag_name('li').pop():
                    driver.find_element_by_class_name('tab').find_element_by_link_text(name2).click()
                    break
        else:
            driver.find_element_by_class_name('loc_csl_width').click()
            print(name2)
            list1.append(name2)
        # else:
        #     driver.find_element_by_css_selector('input.base_input_h_33.inline_s ').click()
        #     time.sleep(2)
        #     driver.find_element_by_class_name('loc_csl_width').click()
        if j == driver.find_elements_by_class_name('area-list ')[1].find_elements_by_tag_name('li').pop():
            driver.find_element_by_class_name('tab').find_element_by_link_text(name1).click()
            break
    if i == driver.find_elements_by_class_name('area-list ')[0].find_elements_by_tag_name('li').pop():
        print('stop')
        print(list1)
#
# with open(file_path + '/address', 'w') as f:
#     for i in list1:
#             f.write(str(i)+'\n')
# print('结束')
