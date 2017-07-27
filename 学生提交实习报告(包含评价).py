# coding=utf-8
from selenium import webdriver, common
import logging
import time
import os
import win32gui
import win32con

log_time = time.strftime('%y-%m-%d', time.localtime(time.time()))
reportname = os.getcwd() + '\\' + '思政理论课暑期社会实践报告（论文）.doc'
picturename = os.getcwd() + '\\' + '实习证明.jpg'
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
# 获取当前分钟
nowtime = time.strftime('%m/%d/%H/%M', time.localtime(time.time()))
# 数据准备
advice = "希望学校加强学生的实践能力，多组织一些团体的活动，有助于培养团队合作的意识，这对于一个企业来说，员工的团队合作能力是至关重要的。再就是出行的安全，可以多开展这方面的讲座，加强学生的安全防范意识。还有在学校要适当的训练学生的沟通技巧，有时候，一句话换一种方式表达，会起到截然不同的效果。这些都能够加快学生在公司的成长；提升自己。"
evaluate_for_teacher = "老师细致。作为一名党员教师，她能够模范带头参与各种政治学习活动，她尊敬尊重待人热爱学生，人际关系和谐融洽，是老师们的好榜样。作为一名政治教师，她为了上好课，看查找实例……乐在其中。由于尊重学生，能够切中学生的兴趣点进行教学，她的课堂上，学生积极主动，气氛活跃。作为一名对外联络员，她一趟一趟地奔波，为毕业生寻找合适的工作，智慧地和用人单位恰谈协商，使得每个学生都能有用武之地，能够扬其所长。作为团支部书记，她积极开展团的工作，加强了校内外的联系，有条不紊地组织了各项有声有色的活动，开拓了学生视野。因此被评为市特教学校先进教师。"
addclass = "野外求生基础知识"
appraisal = '大学四年的美好时光已接近尾声，同时也是我人生的一大转折点。我通过系统化、理论化的学习;学到了很多专业知识，更重要的是，我学会了如何以较快速度掌握一种新事物的能力，思想成熟了很多，性格更坚毅了。我以严谨的态度和积极的热情投身于学习和工作中，然而日益激烈的社会竟争也使我充分地认识到成为一名德智体全面发展的优秀大学生的重要性。无论如何，过去的是我不断奋斗、不断完善自我的一个过程。 大学生活与社会生活是相互映射的，所以大学阶段的提高是个人综合素质与能力的培养、提高;才是我们作为当代大学生的主题。除此之外，课余时间我经常利用网络带来的便利，关注最新科学技术动态;尤其是有关本专业的知识。使自己始终紧跟世界最新发展潮流和时代的步伐。人无完人，我也有很多缺点需要我不断的去克服，改正。在未来的生活中我会不断的学习充实自己，改正缺点错误，充分利用大学学到的知识继续努力实现自己的梦想，人生价值。'
# 学生账号密码
username = '9040@xybsyw.com'
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

try:
    logging.info('学生实习报告的脚本开始')
    driver.get(domain + 'login.xhtml')
    driver.find_element_by_partial_link_text('我是学生').click()
    driver.find_element_by_id('username').click()
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login').click()
    # 有蒙版，先等加载完全
    time.sleep(1)
    driver.find_element_by_link_text('实习报告').click()
    try:
        driver.find_element_by_link_text('尾页').click()
        time.sleep(1)
    except Exception as e:
        logging.info('实习报告只有一页，没有尾页' + str(e))
    reportbutton = driver.find_elements_by_partial_link_text('提交实习报告').pop()
    reportbutton.click()
    try:
        driver.find_element_by_link_text('去评价').click()
        driver.switch_to.window(driver.window_handles[1])
        [i.send_keys('2') for i in
         driver.find_elements_by_css_selector('input.textbox-text.validatebox-text.textbox-prompt')[0:2]]
        driver.find_element_by_id('workHard').find_elements_by_tag_name('img')[0].click()
        driver.find_element_by_id('beCompetent').find_elements_by_tag_name('img')[1].click()
        driver.find_element_by_id('satisfyDegree').find_elements_by_tag_name('img')[2].click()
        driver.find_element_by_id('practiceSuggest').send_keys(advice + nowtime)
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
                [i.find_elements_by_tag_name('img')[2].click() for i in
                 enterprise.find_elements_by_css_selector('span.star')]
                enterprise.find_elements_by_tag_name('label')[1].click()
            except:
                continue
        driver.find_element_by_css_selector('input.base_input.placeholder.base_btn_h35').send_keys(addclass + nowtime)
        driver.find_element_by_id('courseBtn').click()
        try:
            driver.find_element_by_id('selfAppraisal').send_keys(appraisal + nowtime)
        except:
            logging.info('不需要自我鉴定')
        try:
            driver.find_element_by_id('downLoadBtn').click()
            time.sleep(1)
            driver.find_element_by_link_text('下载').click()
            driver.switch_to.window(driver.window_handles[2])
            driver.close()
            driver.switch_to.window(driver.window_handles[1])
            driver.find_element_by_link_text('关闭').click()
            driver.find_element_by_id('fileUpload').click()
            # 处理上传
            time.sleep(3)
            dialog = win32gui.FindWindow('#32770', u'打开')
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, None, 'ComboBoxEx32', None)
            ComboBox = win32gui.FindWindowEx(ComboBoxEx32, None, 'ComboBox', None)
            Edit = win32gui.FindWindowEx(ComboBox, None, 'Edit', None)
            win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, picturename)
            button = win32gui.FindWindowEx(dialog, None, 'Button', '打开(&O)')
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        except:
            logging.info('不需要自我鉴定')
        time.sleep(1)
        driver.find_element_by_id('submitButton').click()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        reportbutton.click()
    except:
        logging.info('该实习报告已经被评价，无需再次评价')
    time.sleep(2)
    driver.find_element_by_link_text('确定').click()
    driver.switch_to.window(driver.window_handles[1])

    try:
        if driver.find_element_by_css_selector('span.error_text').is_displayed():
            print('显示了错误信息')
            raise SyntaxError
    except common.exceptions.WebDriverException:
        logging.info('正常进入提交页')
    driver.find_element_by_link_text('下载实习报告模板').click()
    driver.find_element_by_link_text('下一步，上传提交实习报告').click()  # 这个按钮提示不合理
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
    time.sleep(3)
    if driver.find_element_by_class_name('import_success').is_enabled():
        logging.info('报告提交成功')
    time.sleep(3)
    driver.find_element_by_link_text('退出').click()
    logging.info('学生实习报告的脚本正常结束')

except SyntaxError:
    logging.error('提交实习报告出错，可能模板不存在或者规则问题')
except Exception as e:
    logging.error('学生实习报告的脚本错误' + ':' + str(e))
finally:
    driver.quit()
