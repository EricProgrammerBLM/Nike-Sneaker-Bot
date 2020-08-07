from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
#Import this for the Try and Except. This is used to locate errors in selenium and create a solution
import datetime, time


#DO NOT SELL THIS CODE WITHOUT REMOVING PERSONAL INFO
#
#          THERE ARE 4 STEPS
#


CheckOutTime = 50000 #STEP 1 CHANGE TO ZERO 0
Shoe_Name = ("Nike Air Zoom SuperRep") #STEP 2 PUT EXACT SHOE NAME
#Name of the shoes we will be ordering goes here
#Nike Adapt BB 2.0



#--------------Function to Pick Out Shoe Size and Continue Script----------

def continueCheckOut():
    AddTo = "//*[@id='buyTools']/div[2]/button[1]"
    wait = WebDriverWait(driver,200)
    wait.until(EC.presence_of_element_located((By.XPATH, AddTo)))
#Instead waits for Add to Cart button to load




    def PickLowestSize():
        FirstSize = 1
#This variable is used for the xpath to check the first size of every Size Chart for every sneaker it searches.
#All first sizes have the same xpath

        SoldOut = ('rgba(247, 247, 247, 1)')
#This is the background color of sold out sneaker sizes

        EndLoop = 0
#This is used to end the while loop below until it finds a size thats avalible
        while EndLoop == 0:
            xpath_OfFirstSize = '//*[@id="buyTools"]/div[1]/fieldset/div/div[{0}]/label'.format(str(FirstSize))
            Size = driver.find_element_by_xpath(xpath_OfFirstSize).value_of_css_property('background-color')
            if (Size) == (SoldOut):
                int(FirstSize)
                (FirstSize) = (FirstSize) + 1
                print ('This Size is Sold Out, Checking Next One...')
            else:
                xpath_string = '//*[@id="buyTools"]/div[1]/fieldset/div/div[{0}]/label'.format(str(FirstSize))
                driver.find_element_by_xpath(xpath_OfFirstSize).click()
                print ('Clicked')
                EndLoop = EndLoop + 1

    PickLowestSize()
#Clicks on the lowest size avaliable
#ADD if statement in case shoe size isn't aviliable
    
    driver.find_element_by_xpath('//*[@id="buyTools"]/div[2]/button[1]').click()
#Clicks on Add to Cart


    COut = "//a[@title='Cart Items: 1']"
    wait = WebDriverWait(driver,200)
    wait.until(EC.presence_of_element_located((By.XPATH, COut)))
#Waits for the Cart to Change to 1

#COut = "//button[@data-test='qa-cart-checkout']"
#wait = WebDriverWait(driver,20)
#wait.until(EC.presence_of_element_located((By.XPATH, COut)))
#Waits for the Check Out pop up
#sleep(2)

    driver.find_element_by_xpath('//*[@id="gen-nav-commerce-header"]/header/nav[1]/section[1]/div/div/ul[2]/li[3]/div/a').click()
#Clicks on the Cart

    Checkout2 = "//*[@id='maincontent']/div[2]/div[2]/aside/div[7]/div/button[1]"
    wait = WebDriverWait(driver,200)
    wait.until(EC.presence_of_element_located((By.XPATH, Checkout2)))
    driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div[2]/aside/div[7]/div/button[1]').send_keys(Keys.RETURN)
#Clicks on the Checkout Button

    driver.implicitly_wait(200)
    sleep(3)
    driver.find_element_by_name('emailAddress').send_keys('Username')
    driver.find_element_by_name('password').send_keys('Password')
#PASSWORD AND USERNAME
    print ('Logging In')

    MemberCheckOut = "//input[@value='MEMBER CHECKOUT']"
    driver.find_element_by_xpath(MemberCheckOut).click()
#Clicks checkout button
    #Error Xpath for Ok Button: //*[@id="checkout-wrapper"]/div/div/div[2]/div/div/div/div/div/div/button
    #                         : //*[@id="checkout-wrapper"]/div/div/div[2]/div/div/div/div/div/div/button


    Edit = "//a[@aria-label='Edit Shipping']"
    wait = WebDriverWait(driver,200)
    wait.until(EC.presence_of_element_located((By.XPATH, Edit)))
#Web driver stops until it finds the xpath of the
#edit button from the check out page
#Then it refreshed the page



    driver.refresh()
    print ('Refreshed')
    driver.implicitly_wait(200)

    frame = driver.find_element_by_xpath('//*[@id="mastercard-cvv-form"]/div/div[3]/div/iframe')
    driver.switch_to.frame(frame)
#Switched into the iframe and enters the cvv number

    driver.implicitly_wait(200)
    sleep(1)
    driver.find_element_by_id('cvNumber').send_keys('111')

    driver.switch_to.default_content()
#Switches out of Frame

    sleep(CheckOutTime) #Change when using bot on release day
    driver.find_element_by_xpath('//*[@id="placeorderAB3576"]/div/div[1]/button').click()
#Places the order

#----------------------- End ---------

    

driver = webdriver.Chrome(executable_path=(r'C:\Users\John Doe\Desktop\Driver\chromedriver_win32\chromedriver.exe'))
driver.get('https://www.nike.com/')

today = datetime.datetime.now()

Activate = (datetime.datetime(today.year, today.month, today.day, 3, 15, 0) - today).seconds     #STEP 3 CHOOSE THE TIME YOU WANT IT TO CONTINUE AT AFTER LAUNCHING THE BROWSER
#Uses Military Time 23, 25, 0 = 11:25:00PM                                                       #STEP 4 MAKE SURE YOUR NIKE CART IS COMPLETELY EMPTY
print('Waiting for ' + str(datetime.timedelta(seconds=Activate)))
time.sleep(Activate)
#Rest of the code will activate at the correct time that you set it

driver.maximize_window()

driver.find_element_by_id('TypeaheadSearchInput').send_keys(Shoe_Name)
#Will enter/type the name of the shoe we're going to buy

driver.find_element_by_xpath('//*[@id="gen-nav-commerce-header"]/header/nav[1]/section[2]/div/div[3]/div[1]/div/div/div/button[2]/i').click()
#Will click the search button
print ('Searching for ' + Shoe_Name)


SearchResults = "//div[@id='Wall']"
wait = WebDriverWait(driver,900)
wait.until(EC.presence_of_element_located((By.XPATH, SearchResults)))

sleep(2)
#sleep(3) #This was originally here

#May have to add a try and except function here where it continues by clocking the shoe size
#For shoes like Nike Adapt BB 2.0

Mens = "//button[@aria-label='Filter for Men']"
Men = "//a[@aria-label='Filter for Men']"

#Function to look for the men's filter button
def try_this():
    try:
        driver.find_element_by_xpath(Men).click()
    except NoSuchElementException: #Error name goes here
        print ("Wasn't found. Trying different xpath")
        driver.find_element_by_xpath(Mens).click()

#                        BUG HERE
try:
    driver.find_element(By.ID,'pdp_product_title')
    continueCheckOut()
except NoSuchElementException:
    try_this()


    
#Clicks on the Men Filter

#sleep(3) #This was originally here, if becomes issue uncomment this
sleep(1) #Need a sleep statement or it may click on a womens shoe

driver.find_element_by_link_text(Shoe_Name).send_keys(Keys.RETURN)
#Clicks on the exact shoe name
#Might add try statement here for partial link text
print ('Clicked on ' + Shoe_Name)


AddTo = "//*[@id='buyTools']/div[2]/button[1]"
wait = WebDriverWait(driver,200)
wait.until(EC.presence_of_element_located((By.XPATH, AddTo)))
#Instead waits for Add to Cart button to load




def PickLowestSize():
    FirstSize = 1
#This variable is used for the xpath to check the first size of every Size Chart for every sneaker it searches.
#All first sizes have the same xpath

    SoldOut = ('rgba(247, 247, 247, 1)')
#This is the background color of sold out sneaker sizes

    EndLoop = 0
#This is used to end the while loop below until it finds a size thats avalible
    while EndLoop == 0:
        xpath_OfFirstSize = '//*[@id="buyTools"]/div[1]/fieldset/div/div[{0}]/label'.format(str(FirstSize))
        Size = driver.find_element_by_xpath(xpath_OfFirstSize).value_of_css_property('background-color')
        if (Size) == (SoldOut):
            int(FirstSize)
            (FirstSize) = (FirstSize) + 1
            print ('This Size is Sold Out, Checking Next One...')
        else:
            xpath_string = '//*[@id="buyTools"]/div[1]/fieldset/div/div[{0}]/label'.format(str(FirstSize))
            driver.find_element_by_xpath(xpath_OfFirstSize).click()
            print ('Clicked')
            EndLoop = EndLoop + 1

PickLowestSize()
#Clicks on the lowest size avaliable
#ADD if statement in case shoe size isn't aviliable
    
driver.find_element_by_xpath('//*[@id="buyTools"]/div[2]/button[1]').click()
#Clicks on Add to Cart


COut = "//a[@title='Cart Items: 1']"
wait = WebDriverWait(driver,900)
wait.until(EC.presence_of_element_located((By.XPATH, COut)))
#Waits for the Cart to Change to 1

#COut = "//button[@data-test='qa-cart-checkout']"
#wait = WebDriverWait(driver,20)
#wait.until(EC.presence_of_element_located((By.XPATH, COut)))
#Waits for the Check Out pop up
#sleep(2)

driver.find_element_by_xpath('//*[@id="gen-nav-commerce-header"]/header/nav[1]/section[1]/div/div/ul[2]/li[3]/div/a').click()
#Clicks on the Cart

Checkout2 = "//*[@id='maincontent']/div[2]/div[2]/aside/div[7]/div/button[1]"
wait = WebDriverWait(driver,900)
wait.until(EC.presence_of_element_located((By.XPATH, Checkout2)))
driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div[2]/aside/div[7]/div/button[1]').send_keys(Keys.RETURN)
#Clicks on the Checkout Button

driver.implicitly_wait(900)
sleep(3)
driver.find_element_by_name('emailAddress').send_keys('Email)
driver.find_element_by_name('password').send_keys('Your Password')
#PASSWORD AND USERNAME
print ('Logging In')

MemberCheckOut = "//input[@value='MEMBER CHECKOUT']"
driver.find_element_by_xpath(MemberCheckOut).click()
#Clicks checkout button
    #Error Xpath for Ok Button: //*[@id="checkout-wrapper"]/div/div/div[2]/div/div/div/div/div/div/button
    #                         : //*[@id="checkout-wrapper"]/div/div/div[2]/div/div/div/div/div/div/button


Edit = "//a[@aria-label='Edit Shipping']"
wait = WebDriverWait(driver,200)
wait.until(EC.presence_of_element_located((By.XPATH, Edit)))
#Web driver stops until it finds the xpath of the
#edit button from the check out page
#Then it refreshed the page



driver.refresh()
print ('Refreshed')
driver.implicitly_wait(200)

frame = driver.find_element_by_xpath('//*[@id="mastercard-cvv-form"]/div/div[3]/div/iframe')
driver.switch_to.frame(frame)
#Switched into the iframe and enters the cvv number

driver.implicitly_wait(200)
sleep(1)
driver.find_element_by_id('cvNumber').send_keys('377')

driver.switch_to.default_content()
#Switches out of Frame

sleep(CheckOutTime) #Change when using bot on release day
driver.find_element_by_xpath('//*[@id="placeorderAB3576"]/div/div[1]/button').click()
#Places the order




