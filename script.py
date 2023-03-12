from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import requests

def send_msg(text):
    token="your bot token here"
    chat_id="the chat id bot is going to message to"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="+text
    results=requests.get(url_req)
    
def intfilter(string):
    number=""
    for k in string:
        if (k.isdigit()):
            number+=k
    return number

username = '' #Your username 
password = '' #Your password
driver = webdriver.Chrome('C:/chromedriver') #Locate your chromedriver. You can find the source at https://chromedriver.chromium.org/,
#Once you put your chromedriver under C:/, you don't need to manually adjust this path. Otherwise please specify.
driver.get("https://rez.metu.edu.tr/")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/section/div/div/div/div[2]/form[1]/div[2]/div[1]/div/input').send_keys(username)
driver.find_element(By.XPATH,'/html/body/section/div/div/div/div[2]/form[1]/div[2]/div[2]/div/input').send_keys(password)
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/section/div/div/div/div[2]/form[1]/div[2]/button').click()
time.sleep(1)

def select():
    driver.get("https://rez.metu.edu.tr/view/home.jsf")
    Select(driver.find_element(By.XPATH,'/html/body/section/div[2]/div/div[2]/div[2]/form/select')).select_by_index(11)
    time.sleep(1)


sentMessage9 = 0
sentMessage12 = 0
sentMessage14 = 0
sentMessage16 = 0
sentMessage18 = 0
sentMessage20 = 0
prevVar_9=0
prevVar_12=0
prevVar_14=0
prevVar_16 =0
prevVar_18=0
prevVar_20=0
while True:   
    var_9 =  0
    var_12 = 0
    var_14 = 0
    var_16 = 0
    var_18 = 0
    var_20 = 0  
    free9=0
    free12=0
    free14=0
    free16=0
    free18=0
    free20=0
    found_none = 0
    found=0
    select()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    for k in range(1,10):
        try:   
            value = driver.find_element(By.XPATH, '/html/body/section/div[2]/div/div[2]/div[2]/form/div/div/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a['+str(k)+']/div[1]/div[1]/span')
            if value:
                if value.text != "12:00 - 13:30":
                    
                    if value.text == "9:30 - 11:30":
                        var_9 = 1
                        free9 =  intfilter(driver.find_element(By.XPATH, '/html/body/section/div[2]/div/div[2]/div[2]/form/div/div/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a['+str(k)+']/div[1]/div[2]').text)
                    if value.text == "14:00 - 15:30":
                        var_14 = 1
                        free14 = intfilter(driver.find_element(By.XPATH, '/html/body/section/div[2]/div/div[2]/div[2]/form/div/div/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a['+str(k)+']/div[1]/div[2]').text)
                    elif value.text == "16:00 - 17:30":
                        var_16 = 1
                        free16= intfilter(driver.find_element(By.XPATH, '/html/body/section/div[2]/div/div[2]/div[2]/form/div/div/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a['+str(k)+']/div[1]/div[2]').text)
                    elif value.text == "17:50 - 19:20":
                        var_18 = 1
                        free18= intfilter(driver.find_element(By.XPATH, '/html/body/section/div[2]/div/div[2]/div[2]/form/div/div/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a['+str(k)+']/div[1]/div[2]').text)
                    elif value.text == "19:30 - 21:00":
                        var_20 = 1
                        free20=intfilter(driver.find_element(By.XPATH, '/html/body/section/div[2]/div/div[2]/div[2]/form/div/div/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a['+str(k)+']/div[1]/div[2]').text)
                    found=1 
                    
            else:
                pass
        except:
            pass
    if found==1:
        if var_9 == 1 and prevVar_9 ==0:
            send_msg("["+current_time + " ] 9.30 seansında "+ free9+ " yer var bro")
            sentMessage9=1
            prevVar_9 =1
        else:
            prevVar_9 = 0
        
        if var_9 == 0 and sentMessage9 == 1:
            send_msg("["+current_time + " ] 9.30 seansında artık yer yok bro :D")
            sentMessage9=0
        elif var_9==0 and sentMessage9==0:
            pass
        else:
            pass
        
        if var_12 == 1 and prevVar_12==0:
            send_msg("["+current_time + " ] 12.00 seansında "+ free12+" yer var bro")
            prevVar_12 =1
            sentMessage12=1
        else:
            prevVar_12 = 0
            
        if var_12 == 0 and sentMessage12 == 1:
            send_msg("["+current_time + " ] 12.00 seansında artık yer yok bro :D")
            sentMessage12=0
        elif var_12 == 0 and sentMessage12==0:
            pass
            
        else:
            pass
            
            
        if var_14 == 1 and prevVar_14==0:
            send_msg("["+current_time + " ] 14.00 seansında" +free14+" yer var bro")
            prevVar_14 =1
            sentMessage14=1
        
        else:
            prevVar_14 = 0
            
          
        if var_14 == 0 and sentMessage14 == 1:
            send_msg("["+current_time + " ] 14 seansında artık yer yok bro :D")
            sentMessage14=0
        elif var_14 == 0 and sentMessage14==0:
            pass
        else:
            pass
            
            
        if var_16 == 1 and prevVar_16==0:
            send_msg("["+current_time + " ] 16.00 seansında"+free16+" yer var bro")
            prevVar_16 =1
            sentMessage16=1
        else:
            prevVar_16=0
          
        if var_16 == 0 and sentMessage16 == 1:
            send_msg("["+current_time + " ] 16.00 seansında "+free18+" artık yer yok bro :D")
            sentMessage16=0
        elif var_16 == 0 and sentMessage16==0:
            pass
        else:
            pass
            
            
        if var_18 == 1 and prevVar_18==0:
            send_msg("["+current_time + " ] 17.50 seansında "+free18+" yer var bro")
            prevVar_18 =1
            sentMessage18=1
        else:
            prevVar_18=0
            
            
        if var_18 == 0 and sentMessage18 == 1:
            send_msg("["+current_time + " ] 17.50 seansı artık yok bro :D")
            sentMessage18=0
        elif var_18 == 0 and sentMessage18==0:
            pass   
        else:
            pass
            
        if var_20 == 1 and prevVar_20==0:
            send_msg("["+current_time + " ] 19.20 seansında "+free20+" yer var bro")
            prevVar_20 =1
            sentMessage20=1
        else:
            prevVar_20 = 0
            
        if var_20 == 0 and sentMessage20 == 1:
            send_msg("["+current_time + " ] 19.20 seansı artık yok bro :D")
            sentMessage20=0
            
        elif var_20 == 0 and sentMessage20==0:
            pass
            
        else:
            pass
        
    else:
        print(current_time+" The bot is checking still")
    time.sleep(5)
