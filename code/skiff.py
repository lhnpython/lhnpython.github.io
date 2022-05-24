import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument("headless")



def login():
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div[3]/form/div[1]/div/div/input').send_keys("lhn0225@163.com")
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div[3]/form/div[2]/div/div[1]/input').send_keys("mima15130078794")
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div[3]/form/div[3]').click()

def sendmail(address, subj, message):
    driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div/div[2]/div[1]/div[2]/div[1]/div/span/span').click()
    alive = True
    while alive == True:
        try:
            driver.find_element(by=By.XPATH, value='//*[@placeholder="Search and add people"]').send_keys(address)
            alive = False
        except:
            driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div/div[2]/div[1]/div[2]/div[1]/div/span/span').click()
    driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/input').send_keys(subj)
    messagelable = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div/div[2]/div[3]/div/div[2]/div[4]/div/div')
    messagelable.clear()
    messagelable.send_keys(message)
    time.sleep(slp)
    driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div/div[2]/div[3]/div/div[2]/div[5]/div/div[1]/span/span').click()


SUBJ = input("主题: ")
Message = input("正文: ")
slp = float(input("睡眠(0.4左右): "))
print("正在初始化 10s......")
driver = webdriver.Edge(options=options)
driver.get("https://app.skiff.com/")
login()
time.sleep(5)
driver.get("https://app.skiff.com/mail/inbox")
time.sleep(5)
addresslist = open("a.txt", 'r').readlines()
for a in addresslist:
    f = open("finish.csv", 'a')
    address = a.replace("\n", '')
    oldtime = time.time()
    sendmail(address, SUBJ, Message)
    newtime = time.time()
    print("发送成功, 耗时{:0.1f} s".format(newtime-oldtime), address)
    f.write(address+"\n")
    f.close()
driver.close()
