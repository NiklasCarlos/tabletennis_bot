#tabletennis_bot
#select and interact workflow
    # python -i tabletennis.py ------> exit()

from selenium import webdriver
from selenium.webdriver.common.by import By

class tabletennis_bot:


    def __init__(self):
        self.driver = webdriver.Chrome()


    def loggin(self):
        self.driver.get("https://www.contra-berlin.de/conb_de/tt-schule-spielen/tischvermietung.html")
        
        #popup cookies button -> accept fun
        log_btn =  self.driver.find_element("xpath", '//*[@id="ccm-widget"]/div/div[2]/div[2]/button[2]')
         #click btn
        log_btn.click()

        #Terminbuchen btn

        l2 = self.driver.find_element("xpath", '//*[@id="top"]/body/div[1]/div/div/section/div/div/div[2]/div/div/div')
       


        #switch frame
        iframe = self.driver.find_elements(By.TAG_NAME,'iframe')[0]
        self.driver.switch_to.frame(iframe)

       #vermietung 60min suchen ->  iframe von timify
        l3 = self.driver.find_element("xpath", '//*[@id="app"]/div[2]/div[2]/div[2]/div[5]/div/div/div/div[2]/div/div[1]/div/div[3]/button')
        


        

        # driver.page_source
        #For improved reliability, you should consider using WebDriverWait in combination with element_to_be_clickable.