# coding=utf-8
from selenium import webdriver, common
import logging
import time
import os
import win32gui
import win32con

# 日志处理
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
advice = "希望学校加强学生的实践能力，多组织一些团体的活动，有助于培养团队合作的意识，这对于一个企业来说，员工的团队合作能力是至关重要的。再就是出行的安全，可以多开展这方面的讲座，加强学生的安全防范意识。还有在学校要适当的训练学生的沟通技巧，有时候，一句话换一种方式表达，会起到截然不同的效果。这些都能够加快学生在公司的成长；提升自己。"
evaluate_for_teacher = "老师细致。作为一名党员教师，她能够模范带头参与各种政治学习活动，她尊敬尊重待人热爱学生，人际关系和谐融洽，是老师们的好榜样。作为一名政治教师，她为了上好课，看查找实例……乐在其中。由于尊重学生，能够切中学生的兴趣点进行教学，她的课堂上，学生积极主动，气氛活跃。作为一名对外联络员，她一趟一趟地奔波，为毕业生寻找合适的工作，智慧地和用人单位恰谈协商，使得每个学生都能有用武之地，能够扬其所长。作为团支部书记，她积极开展团的工作，加强了校内外的联系，有条不紊地组织了各项有声有色的活动，开拓了学生视野。因此被评为市特教学校先进教师。"
addclass = "野外求生基础知识"

# 学生账号密码
username = '16175@xybsyw.com'
password = 'qaz147'
# 开始
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()

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
time.sleep(1)
driver.find_element_by_link_text('实习报告').click()
driver.implicitly_wait(waittime)
try:
    driver.find_element_by_link_text('尾页').click()
    driver.implicitly_wait(waittime)
    time.sleep(1)
except Exception as e:
    logging.info('实习报告只有一页，没有尾页' + str(e))
reportbutton = driver.find_elements_by_partial_link_text('提交实习报告').pop()
reportbutton.click()
driver.find_element_by_link_text('去评价').click()
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(waittime)
[i.send_keys('2') for i in
 driver.find_elements_by_css_selector('input.textbox-text.validatebox-text.textbox-prompt')[0:2]]
# [i.find_element_by_css_selector('input.textbox-text.validatebox-text.textbox-prompt').send_keys('2') for i in
#  driver.find_elements_by_css_selector('span.textbox.numberbox')]
driver.find_element_by_id('workHard').find_elements_by_tag_name('img')[0].click()
driver.find_element_by_id('beCompetent').find_elements_by_tag_name('img')[1].click()
driver.find_element_by_id('satisfyDegree').find_elements_by_tag_name('img')[2].click()
driver.find_element_by_id('practiceSuggest').send_keys(advice)
for star in driver.find_elements_by_class_name('dd_info'):
    try:
        star.find_element_by_css_selector('span.star.inline_s').find_elements_by_tag_name('img')[2].click()
        star.find_element_by_css_selector('textarea.targetText.placeholder').send_keys(
            evaluate_for_teacher + nowtime)
    except:
        continue
driver.find_element_by_class_name('text_p').find_elements_by_tag_name('label')[0].click()
driver.find_element_by_id('problemSolving').find_elements_by_tag_name('img')[2].click()
driver.find_element_by_id('webUse').find_elements_by_tag_name('img')[2].click()
driver.find_element_by_id('webValue').find_elements_by_tag_name('img')[2].click()
for enterprise in driver.find_elements_by_class_name('dd_info'):
    try:
        [i.find_elements_by_tag_name('img')[2].click()for i in enterprise.find_elements_by_css_selector('span.star')]
        enterprise.find_elements_by_tag_name('label')[1].click()
    except:
        continue
driver.find_element_by_css_selector('input.base_input.placeholder.base_btn_h35').send_keys(addclass)
driver.find_element_by_id('courseBtn').click()
driver.find_element_by_id('submitButton').click()
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.implicitly_wait(waittime)
reportbutton.click()
driver.implicitly_wait(waittime)
time.sleep(1)
logging.info('该实习报告已经被评价，无需再次评价')
driver.find_element_by_link_text('确定').click()
driver.switch_to.window(driver.window_handles[1])

try:
    if driver.find_element_by_css_selector('span.error_text').is_displayed():
        print('显示了错误信息')
        raise SyntaxError
except common.exceptions.WebDriverException:
    logging.info('不需要提交实习报告')
driver.find_element_by_link_text('下载实习报告模板').click()
driver.find_element_by_link_text('下一步，上传提交实习报告').click()
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
    logging.info('报告提交成功')
time.sleep(1)
driver.find_element_by_link_text('退出').click()
logging.info('学生写周日志的脚本正常结束')

# except SyntaxError:
#     logging.error('提交实习报告出错，可能模板不存在或者规则问题')
# except Exception as e:
#     logging.error('学生写周日志的脚本错误' + ':' + str(e))
# finally:
#     driver.quit()
