import requests
import time
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from appium.webdriver import Remote
from selenium.webdriver.common.by import By

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def send(value):
    url = "https://fm.uat.missevan.com/api/chatroom/gift/send"
    payload = "{\"room_id\":399897266,\"gift_id\":128,\"gift_num\":1,\"combo\":0}"
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': value
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text + '\r\n' + '普通礼物赠送成功')


def login():
    # 获取送礼账号cookie
    login_url = "https://app.uat.missevan.com/member/login"
    login_params = {
        'account': 13862900236,
        'password': 'Aa111111',
        'region': 'CN'
    }
    login_headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "45",
        "User-Agent": "MissEvanApp/5.6.0 (iOS;14.2;iPhone9,1)",
        "Connection": "keep-alive",
        "Cookie": "buvid=ZE45EEECCB97788B4B309262BD5D161AC00E; equip_id=eeeccb97-788b-4b30-9262-bd5d161ac00e",
        "X-M-Swimlane": "wujun"
    }
    one_session = requests.Session()
    login_res = one_session.post(login_url, data=login_params, headers=login_headers, verify=False)
    login_token = json.loads(login_res.text).get('info').get('token')
    first_str = "buvid=ZE45EEECCB97788B4B309262BD5D161AC00E; equip_id=eeeccb97-788b-4b30-9262-bd5d161ac00e; token="
    end_str = "; Hm_lvt_91a4e950402ecbaeb38bd149234eb7cc=1609848083; FM_SESS=20210105|22xh4qmqa6he0i7v6ech3eejw; FM_SESS.sig=Ridhf1s9AMaZgpAKYGGFjHk7EHk"
    audience_Cookie = first_str + login_token + end_str
    return audience_Cookie


def live():
    # 获取开播账号cookie
    login_url = "https://app.uat.missevan.com/member/login"
    login_params = {
        'account': 13605169493,
        'password': '123456',
        'region': 'CN'
    }
    login_headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "45",
        "User-Agent": "MissEvanApp/5.6.0 (iOS;14.2;iPhone9,1)",
        "Connection": "keep-alive",
        "Cookie": "buvid=ZE45EEECCB97788B4B309262BD5D161AC00E; equip_id=eeeccb97-788b-4b30-9262-bd5d161ac00e",
        "X-M-Swimlane": "wujun"
    }
    one_session = requests.Session()
    login_res = one_session.post(login_url, data=login_params, headers=login_headers, verify=False)
    login_token = json.loads(login_res.text).get('info').get('token')
    first_str = "buvid=ZE45EEECCB97788B4B309262BD5D161AC00E; equip_id=eeeccb97-788b-4b30-9262-bd5d161ac00e; token="
    end_str = "; Hm_lvt_91a4e950402ecbaeb38bd149234eb7cc=1609848083; FM_SESS=20210105|22xh4qmqa6he0i7v6ech3eejw; FM_SESS.sig=Ridhf1s9AMaZgpAKYGGFjHk7EHk"
    live_Cookie = first_str + login_token + end_str

    # 获取送礼账号cookie
    login_url = "https://app.uat.missevan.com/member/login"
    login_params = {
        'account': 13862900236,
        'password': 'Aa111111',
        'region': 'CN'
    }
    login_headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "45",
        "User-Agent": "MissEvanApp/5.6.0 (iOS;14.2;iPhone9,1)",
        "Connection": "keep-alive",
        "Cookie": "buvid=ZE45EEECCB97788B4B309262BD5D161AC00E; equip_id=eeeccb97-788b-4b30-9262-bd5d161ac00e",
        "X-M-Swimlane": "wujun"
    }
    one_session = requests.Session()
    login_res = one_session.post(login_url, data=login_params, headers=login_headers, verify=False)
    login_token = json.loads(login_res.text).get('info').get('token')
    first_str = "buvid=ZE45EEECCB97788B4B309262BD5D161AC00E; equip_id=eeeccb97-788b-4b30-9262-bd5d161ac00e; token="
    end_str = "; Hm_lvt_91a4e950402ecbaeb38bd149234eb7cc=1609848083; FM_SESS=20210105|22xh4qmqa6he0i7v6ech3eejw; FM_SESS.sig=Ridhf1s9AMaZgpAKYGGFjHk7EHk"
    audience_Cookie = first_str + login_token + end_str

    online_url = "https://fm.uat.missevan.com/api/chatroom/online"
    online_params = {
        "counter": 0,
        "room_id": 399897266,
    }
    online_headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "55",
        "User-Agent": "MissEvanApp/4.6.0 (iOS;14.2;iPhone9,1)",
        "Connection": "keep-alive",
        "X-M-Date": "2021-01-05T11:51:35Z",
        "Cookie": live_Cookie,
    }
    res = one_session.post(url=online_url, data=online_params, headers=online_headers, verify=False)
    print(f"{res.text}")


# 在 scrcpy 目录下命令行输入 scrcpy --record file.mp4 来进行屏幕录制，按 Ctrl c 结束录屏，可以在当前目录下找到录屏文件
def observation(room_id):
    desired_caps = {
        'platformName': 'Android',  # 被测手机是安卓
        'platformVersion': 11,  # 手机安卓版本
        'deviceName': '1158729196的Mi 10',  # 设备名，安卓手机可以随意填写
        'appPackage': 'cn.missevan',  # 启动APP Package名称
        'appActivity': '.activity.SplashActivity',  # 启动Activity名称
        'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
        'resetKeyboard': True,  # 执行完程序恢复原来输入法
        'noReset': True,  # 不要重置App，如果为False的话，执行完脚本后，app的数据会清空，比如你原本登录了，执行完脚本后就退出登录了
        'newCommandTimeout': 6000,
        'automationName': 'UiAutomator2'
    }

    driver = Remote(command_executor='http://localhost:4723/wd/hub',
                    desired_capabilities=desired_caps)  # 连接Appium Server，初始化自动化环境
    driver.implicitly_wait(10)  # 设置隐式等待10秒
    driver.find_element(By.ID, 'cn.missevan:id/fl_search').click()  # 点击搜索框
    driver.find_element(By.ID, 'cn.missevan:id/et_search').send_keys(room_id)  # 输入测试直播间号
    driver.find_element(By.ID, 'cn.missevan:id/tv_hot_search').click()  # 搜索
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                  '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                  '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android'
                                  '.widget.RelativeLayout[3]/android.widget.TextView').click()  # 切换到直播tab
    driver.find_element(By.ID, 'cn.missevan:id/live_cover').click()  # 进入测试直播间
    time.sleep(5)  # 缓冲时间
    for i in range(1,10):
        send(login())
        time.sleep(2)
    time.sleep(10)  # 缓冲时间
    driver.quit()


if __name__ == '__main__':
    live()
    observation(399897266)

