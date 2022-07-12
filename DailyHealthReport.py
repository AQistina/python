from selenium import webdriver
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
# options.headless = True     #for the code to run in the background without opening a window.
options.add_argument("--enable-javascript")
browser = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), options=options)
# browser.get('https://login.microsoftonline.com/common/oauth2/authorize?client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&resource=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&response_type=code%20id_token&scope=openid%20profile&state=OpenIdConnect.AuthenticationProperties%3DeyJ2ZXJzaW9uIjoxLCJkYXRhIjp7IklkZW50aXR5UHJvdmlkZXIiOiJBWXl1cjI1bGVvZWM2VG0tRDFHSUZUQ0tSQl9WclZNa1diVDh0MkUyWVlDRWxiNUpTRFNGdkZZOW11YVFYcXhtZFFKRDVHMFZUbEVIOGdZYkNQLUpaLTdCT2pxbERIc29EblVLczJvcWhBY184OHlOeEdTTEQtRWJ2bmxIb2dzTU53IiwiLnJlZGlyZWN0IjoiLyJ9fQ&response_mode=form_post&nonce=637929506899509872.NjA3ZmVlODYtZjhlYi00MWFlLTg2ZDAtNDEyNTIzYTM2NjhmODQ1NGQ3Y2ItOWNhZi00Y2NjLThhMTktNGM4MTE5YmQ4Y2Rl&redirect_uri=https%3A%2F%2Fforms.office.com%2Flanding&x-client-SKU=ID_NET472&x-client-ver=6.15.1.0')

# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


#to open the form page

browser.get('https://forms.office.com/r/RsgCT67LWX')


#to fill ms form: well & WFO
question1 = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[3]/div/div[4]/div/label/input').click()
question2 = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys('EM074')
question3 = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div[1]/div/label/input').click()
question4 = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div[1]/div/label/input').click()

# question1 = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[3]/div/div[4]/div/label/input').click()
# question2 = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys('EM074')
# question3 = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div[1]/div/label/input').click()
# question4 = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div[1]/div/label/input').click()


#to fill ms form: well & WFH
# question1 = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[3]/div/div[4]/div/label/input').click()
# question2 = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys('EM074')
# question3 = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div[1]/div/label/input').click()
# question4 = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div[2]/div/label/input').click()

submitform = browser.find_element_by_xpath('//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()
