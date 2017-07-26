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
username = '9057@xybsyw.com'
password = 'qaz147'
# 地址
domain = 'http://test2.xybsyw.com/'
# 开始
driver = webdriver.Chrome(executable_path=path)
#设置等待时间
driver.set_script_timeout(waittime)
driver.set_page_load_timeout(10)
driver.implicitly_wait(waittime)
#窗口最大化
driver.maximize_window()

logging.info('新增自主岗位的脚本开始')
try:
    driver.get(domain+'login.xhtml')
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
    driver.find_element_by_id('enterpriseName').send_keys(enterpriseName)
    driver.find_element_by_id('name').send_keys(name)
    driver.find_element_by_id('linkman').send_keys(linkman)
    driver.find_element_by_id('enterpriseTel').send_keys(enterpriseTel)
    driver.find_element_by_id('enterpriseEmail').send_keys(enterpriseEmail)
    driver.find_element_by_id('trainer').send_keys(trainer)
    driver.find_element_by_id('trainerTel').send_keys(trainerTel)
    driver.find_element_by_css_selector(
        'input.textbox-text.validatebox-text.textbox-prompt.validatebox-invalid').send_keys(
        salary)
    driver.find_element_by_id('responsibilities').send_keys(responsibilities)
    # 行业选择
    driver.find_element_by_id('multiLevelSingle_selectedText').click()
    driver.find_element_by_id('multiLevelSingle_1').click()
    driver.find_element_by_class_name('MultiLevelSingle_btn').find_elements_by_tag_name('span')[1].click()
    # 实践类型
    driver.find_element_by_css_selector(
        'input.textbox-text.textbox-text-readonly.validatebox-text.textbox-prompt').click()
    driver.find_elements_by_class_name('tree-node').pop().click()
    # 岗位时间
    driver.find_element_by_css_selector(
        'input.textbox-text.textbox-text-readonly.validatebox-text.validatebox-invalid.textbox-prompt').click()
    driver.find_elements_by_class_name('datebox-button')[0].find_elements_by_tag_name('a')[0].click()
    driver.find_element_by_css_selector(
        'input.textbox-text.textbox-text-readonly.validatebox-text.validatebox-invalid.textbox-prompt').click()
    driver.find_elements_by_class_name('calendar-nextmonth').pop().click()
    driver.find_elements_by_css_selector('td.calendar-day.calendar-sunday.calendar-first').pop().click()
    # 地址选择
    driver.find_element_by_class_name('loc_csl_width').click()
    driver.find_element_by_class_name('stock_2_li').click()
    driver.find_element_by_css_selector('input.base_input_h_33.inline_s ').click()
    driver.find_element_by_css_selector('input.base_input_h_33.inline_s ').send_keys(address)
    time.sleep(1)
    driver.execute_script(
        'document.getElementById("longitude").value="116.39748";document.getElementById("latitude").value="39.90868";')
    driver.find_element_by_id('submitPostBtn').click()
    # 让提交超过
    time.sleep(2)
    driver.find_element_by_link_text('退出').click()
    logging.info('新增自主岗位的脚本结束')
except:
    logging.error('新增自主岗位的脚本出错')
finally:
    driver.quit()
