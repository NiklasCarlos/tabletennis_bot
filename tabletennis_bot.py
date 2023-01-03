#tabletennis_bot
#select and interact workflow after venv activation
    #from cmd
    #.\myvenvTT\Scripts\activate
    # python -i tabletennis_bot.py ------> exit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class tabletennis_bot:


    def __init__(self):
        self.driver = webdriver.Chrome('C:/Users/Niklas/Desktop/Projekte/chromedriver.exe')


    def open_website(self):
        self.driver.get("https://www.contra-berlin.de/conb_de/tt-schule-spielen/tischvermietung.html")
        
        sleep(4)
        #popup cookies button -> accept fun
        log_btn =  self.driver.find_element("xpath", '//*[@id="ccm-widget"]/div/div[2]/div[2]/button[2]')
        #evtl wait to load fun einbinden
        
         #click btn 
        log_btn.click()

        #Terminbuchen btn
    def open_booking_screen(self):

        #find element 
        l2 = self.driver.find_element("xpath", '//*[@id="top"]/body/div[1]/div/div/section/div/div/div[2]/div/div/div')
        #TODO wait function einbauen 
        l2.click()

        sleep(4)

    def switch_frame(self):
        #switch frame
        iframe = self.driver.find_elements(By.TAG_NAME,'iframe')[0]
        self.driver.switch_to.frame(iframe)

       #vermietung 60min suchen ->  iframe von timify
        l3 = self.driver.find_element("xpath", '//*[@id="app"]/div[2]/div[2]/div[2]/div[5]/div/div/div/div[2]/div/div[1]/div/div[3]/button')
        
        l3.click()

    def check_date(self):
        #get elements

        #check if Di 18.00, 19.00 oder 1930 is available 
      element = self.driver.find_element(By.XPATH,'//*[contains(text(), "Di")]')
      #from selenium.webdriver.common.by import By
    #https://stackoverflow.com/questions/24795198/get-all-child-elements
    #parentElement = driver.find_element(By.CLASS_NAME,"bar")
    #elementList = parentElement.find_elements(By.TAG_NAME,"li")

    #learn xpath
    #https://www.tutorialspoint.com/find-next-sibling-element-in-selenium-python#:~:text=We%20can%20find%20a%20next,with%20the%20help%20of%20xpath.



      

#bot = tabletennis_bot()

#bot.open_website()
#sleep(3)
#bot.open_booking_screen()
#sleep(3)
#bot.switch_frame()

        # driver.page_source
        #For improved reliability, you should consider using WebDriverWait in combination with element_to_be_clickable.