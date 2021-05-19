import datetime
import time
from selenium import webdriver
import pyautogui as auto
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice', voices[len(voices) - 2].id)
engine.setProperty('rate', 170)
#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wish():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak(f"Good morning")
    elif hour>12 and hour<18:
        speak(f"Good afternoon")
    else:
        speak(f"Good evening")
    speak("Importing all preferances from your personal server.")
 

if __name__ == '__main__':
    wish()

    driver = webdriver.Edge("msedgedriver.exe")
    driver.get('https://office.com')


    e_mail = 'YOUR EMAIL'

    SignIn = driver.find_element_by_xpath('//*[@id="hero-banner-sign-in-to-office-365-link"]')
    SignIn.click()
    time.sleep(int('10'))
    speak('Please wait sir\n')

    input_1 = driver.find_element_by_xpath('//*[@id="i0116"]')
    time.sleep(int('3'))
    input_1.send_keys(e_mail)
    time.sleep(int('3'))
    speak('Entering e-mail address\n')

    SigInNext = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    SigInNext.click()
    time.sleep(int('3'))

    input_2 = driver.find_element_by_xpath('//*[@id="i0118"]')
    input_2.send_keys('YOUR PASSWORD')
    time.sleep(int('3'))
    speak('entering your password')

    SignInrll = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    time.sleep(int('3'))
    SignInrll.click()

    Yes = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    Yes.click()
    time.sleep(int('3'))
    speak('All done sir')

    speak('Do you want me to open anything?')

    query = input()

    if query == 'teams':
        speak('Sure sir. Give me a sec')
        ms_teams = driver.find_element_by_xpath('//*[@id="ShellSkypeTeams_link"]/div/i')
        time.sleep(int('3'))
        ms_teams.click()
    
    elif query == 'word':
        speak('Yes sir, I need some time')
        word = driver.find_element_by_xpath('//*[@id="officeHome"]/div[1]/ohp-left-nav-react/ohp-left-nav-react-content/div/div[1]/ul/li[3]')
        time.sleep(int('3'))
        word.click()
    
    elif query == 'power point':
        speak('Sure sir, Give me sec')
        pp = driver.find_element_by_xpath('//*[@id="officeHome"]/div[1]/ohp-left-nav-react/ohp-left-nav-react-content/div/div[1]/ul/li[5]')
        time.sleep(int('3'))
        pp.click()

