import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

USERNAME = "15201784147"
PASSWORD = "baojiacheng1998"

chromedriver = "/Users/bjc/Desktop/skd/形势与政策/chromedriver"
web = Chrome(chromedriver)

web.get('http://passport2.chaoxing.com/login?loginType=4&newversion=true&fid=10572&refer=http://i.mooc.chaoxing.com')

# 1. 登录
phone = web.find_element(By.CLASS_NAME,'ipt-tel')
pwd = web.find_element(By.CLASS_NAME,'ipt-pwd')
login = web.find_element(By.ID,'phoneLoginBtn')

phone.send_keys(USERNAME)
pwd.send_keys(PASSWORD)
login.click()
time.sleep(6)

#进入课程
iframe = web.find_element(By.ID,'frame_content')
web.switch_to.frame(iframe)
lesson = web.find_element(By.XPATH,"//div[@class='course-cover']//img")
lesson.click()
time.sleep(3)

# 问题原因：是跳转到新页面，无法定位元素问题
#获取当前页句柄
num = web.window_handles
#跳转到新标签页
web.switch_to.window(num[1])
# 进入iframe
frame_content = web.find_element(By.XPATH,"//*[@id='frame_content-zj']")
web.switch_to.frame(frame_content)

time.sleep(4)

#起始页面
begin_class = web.find_element(By.XPATH,'//div[@class="chapter_td"]/div[2]/div[2]/ul/li[1]/div')
#第二个div【章节数+1】，li【课程数】
# 跳转到第一个知识点页面
begin_class.click()
time.sleep(5)
# 进行视频的播放
web.switch_to.window(web.window_handles[-1])
iframe1 = web.find_element(By.ID,'iframe')  # 每次刷新后，都要进入内部iframe
web.switch_to.frame(iframe1)
#class元素包含空格
# 1.使用xpath通过完整的class属性定位: find_element_by_xpath('//div[@class="img-box my"]')
#
# 2.通过某一个class_name定位，driver.find_element_by_class_name('my')  （该属性唯一）
#
# 3.使用css selector, 结合多个class_name组合来定位： driver.find_element_by_css_selector('.img-box.my')
iframe2 = web.find_element(By.XPATH,'//*[@class="ans-attach-online ans-insertvideo-online"]')
web.switch_to.frame(iframe2)
time.sleep(3)
web.find_element(By.CLASS_NAME,'vjs-big-play-button').click()  # 点击播放按钮
print("开始播放")
time.sleep(10)
# 播放和暂停按钮
pause_btn = web.find_element(By.XPATH,'//div[@class="vjs-control-bar"]/button')

while (1):  # 播放等待
    try:
        time.sleep(5)  # 每1秒，检查视频是否播放完毕
        if (pause_btn.get_attribute('title') == "播放"):  #暂停时播放
            pause_btn.click()
            print("继续播放")
        if (pause_btn.get_attribute('title') == "重播"):  # 点击后播放，即播放完毕状态
            print('视频播放完毕')
            web.refresh()
            web.maximize_window()
            time.sleep(5)
            web.find_element(By.XPATH, '//div[@class="jb_btn jb_btn_92 fs14 prev_next next"]').click()
            print("进入章节测验")
            time.sleep(8)
            web.find_element(By.XPATH, '//*[@class="jb_btn jb_btn_92 fs14 prev_next next"]').click()
            time.sleep(3)
            web.find_element(By.XPATH, '//*[@class="jb_btn jb_btn_92 fr fs14 nextChapter"]').click()
            print("进入下一章")
            time.sleep(6)
            iframe1 = web.find_element(By.ID, 'iframe')  # 每次刷新后，都要进入内部iframe
            web.switch_to.frame(iframe1)
            iframe2 = web.find_element(By.XPATH, '//*[@class="ans-attach-online ans-insertvideo-online"]')
            web.switch_to.frame(iframe2)
            time.sleep(3)
            web.find_element(By.CLASS_NAME, 'vjs-big-play-button').click()  # 点击播放按钮
            print("开始播放")
            time.sleep(10)
            # 播放和暂停按钮
            pause_btn = web.find_element(By.XPATH, '//div[@class="vjs-control-bar"]/button')
    except:

        print("出现问题")
        web.find_element(By.CLASS_NAME, 'ans-videoquiz-opt').click()
        web.find_element(By.LINK_TEXT,'提交').click()





