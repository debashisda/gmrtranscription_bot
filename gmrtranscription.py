#This simple script is made to clear the typing test for GMR Transcription, with 100% accuracy

import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

def load_driver():
    global driver
    options = Options()
    options.add_experimental_option("excludeSwitches",["enable-logging"])
    driver = webdriver.Chrome(executable_path="C:/chromedriver.exe",options=options)

def login_to_gmrtranscription():
    driver.execute_script("window.open('https://www.gmrtranscription.com/careers-test/typist-test.aspx','_self');")    
    driver.find_element("id","txtemail").send_keys("email@example.com")# Email ID      
    time.sleep(3)
    driver.execute_script("document.getElementById('btnsubmit').click()") 
    
def start_typing():    
    time.sleep(5)
    driver.find_element("xpath","/html/body/section/div/div[2]/div/div/div[5]/textarea").send_keys("")
    paragraph = driver.execute_script("return document.querySelector('body>section>div>div.row.justify-content-center>div>div>div.words>div').innerText;")
    time.sleep(2)
    for letter in paragraph:
        ActionChains(driver).send_keys(letter).perform()
        time.sleep(1/10) # avg 75WPM - reduce the value to increase typing speed

def main():    
    load_driver()
    login_to_gmrtranscription()
    start_typing()
            
if __name__ == "__main__":
    main()    
