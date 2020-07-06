# Note: For proper working of this Script Good and Uninterepted Internet Connection is Required
# Keep all contacts unique
# Can save contact with their phone Number

# Import required packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import openpyxl as excel

def display_menu():
    """
        DISPLAY A MENU OF WHAT USER CAN DO
    """
    print("************************************************")
    print("*****  Hello - Hessam Hosseini  ******")
    print("************************************************")
    selected = input(f"""WHICH ONE? (1-8)
    1) RUN easy_wtsup()
    2) RUN op_one
    3) RUN task to do
    4) RUN tahlil_defect
    5) RUN tahlil_defect_op1
    6) RUN scrabbling
    7) RUN myscrabing
    8) Run APIs
    9) Run sendsms BTC pass
    PLEASE SPECIFIE WITH A NUMBER: 
    """)
    print("select Number is:",selected)
    if selected=="1":
        easy_wtsup()
    elif selected=="2":
        pass
        
    elif selected=="3":
        pass
        
    elif selected=="4":
        pass
    elif selected=="5":
        pass
    elif selected=="6":
        readContacts(fileName)
    elif selected=="7":
        pass
    elif selected=="8":
        pass
# function to read contacts from a text file
def readContacts(fileName):
    lst = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    firstCol = sheet['A']
    for cell in range(len(firstCol)):
        contact = str(firstCol[cell].value)
        contact = "\"" + contact + "\""
        lst.append(contact)
    return lst

# Target Contacts, keep them in double colons
# Not tested on Broadcast
    targets = readContacts("contacts.xlsx")

    # can comment out below line
    print(targets)

    # Driver to open a browser
    driver = webdriver.Firefox()

    #link to open a site
    driver.get("https://web.whatsapp.com/")

    # 10 sec wait time to load, if good internet connection is not good then increase the time
    # units in seconds
    # note this time is being used below also
    wait = WebDriverWait(driver, 60)
    wait5 = WebDriverWait(driver,50)
    input("Scan the QR code and then press Enter")

    # Message to send list
    # 1st Parameter: Hours in 0-23
    # 2nd Parameter: Minutes
    # 3rd Parameter: Seconds (Keep it Zero)
    # 4th Parameter: Message to send at a particular time
    # Put '\n' at the end of the message, it is identified as Enter Key
    # Else uncomment Keys.Enter in the last step if you dont want to use '\n'
    # Keep a nice gap between successive messages
    # Use Keys.SHIFT + Keys.ENTER to give a new line effect in your Message
    msgToSend = [
                    [12, 32, 0, "Hello! This is test Msg. Please Ignore." + Keys.SHIFT + Keys.ENTER + "http://bit.ly/mogjm05"]
                ]

    # Count variable to identify the number of messages to be sent
    count = 0
    while count<len(msgToSend):

        # Identify time
        curTime = datetime.datetime.now()
        curHour = curTime.time().hour
        curMin = curTime.time().minute
        curSec = curTime.time().second

        # if time matches then move further
        if msgToSend[count][0]==curHour and msgToSend[count][1]==curMin and msgToSend[count][2]==curSec:
            # utility variables to tract count of success and fails
            success = 0
            sNo = 1
            failList = []

            # Iterate over selected contacts
            for target in targets:
                print(sNo, ". Target is: " + target)
                sNo+=1
                try:
                    # Select the target
                    x_arg = '//span[contains(@title,' + target + ')]'
                    try:
                        wait5.until(EC.presence_of_element_located((
                            By.XPATH, x_arg
                        )))
                    except:
                        # If contact not found, then search for it
                        searBoxPath = '//*[@id="input-chatlist-search"]'
                        wait5.until(EC.presence_of_element_located((
                            By.ID, "input-chatlist-search"
                        )))
                        inputSearchBox = driver.find_element_by_id("input-chatlist-search")
                        time.sleep(0.5)
                        # click the search button
                        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div/button').click()
                        time.sleep(1)
                        inputSearchBox.clear()
                        inputSearchBox.send_keys(target[1:len(target) - 1])
                        print('Target Searched')
                        # Increase the time if searching a contact is taking a long time
                        time.sleep(4)

                    # Select the target
                    driver.find_element_by_xpath(x_arg).click()
                    print("Target Successfully Selected")
                    time.sleep(2)

                    # Select the Input Box
                    inp_xpath = "//div[@contenteditable='true']"
                    input_box = wait.until(EC.presence_of_element_located((
                        By.XPATH, inp_xpath)))
                    time.sleep(1)

                    # Send message
                    # taeget is your target Name and msgToSend is you message
                    input_box.send_keys("Hello, " + target + "."+ Keys.SHIFT + Keys.ENTER + msgToSend[count][3] + Keys.SPACE) # + Keys.ENTER (Uncomment it if your msg doesnt contain '\n')
                    # Link Preview Time, Reduce this time, if internet connection is Good
                    time.sleep(10)
                    input_box.send_keys(Keys.ENTER)
                    print("Successfully Send Message to : "+ target + '\n')
                    success+=1
                    time.sleep(0.5)

                except:
                    # If target Not found Add it to the failed List
                    print("Cannot find Target: " + target)
                    failList.append(target)
                    pass

            print("\nSuccessfully Sent to: ", success)
            print("Failed to Sent to: ", len(failList))
            print(failList)
            print('\n\n')
            count+=1
    driver.quit()

def easy_wtsup():
    driver=webdriver.Firefox()
    driver.get("https://web.whatsapp.com/") 
    wait = WebDriverWait(driver, 60) 
      
    target = '"Baba"'
    string = "Message"
    print(" Message"+ string +" to : "+ target + '\n')
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located(( 
        By.XPATH, x_arg))) 
    group_title.click() 
    inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
    input_box = wait.until(EC.presence_of_element_located(( 
        By.XPATH, inp_xpath))) 
    for i in range(2): 
        input_box.send_keys(string + Keys.ENTER)
         print("Successfully Send Message to : "+ target + '\n') 
        time.sleep(1)

def my_whati():
        target = "'Baba'"

    # can comment out below line
    print(target)

    # Driver to open a browser
    driver = webdriver.Firefox()

    #link to open a site
    driver.get("https://web.whatsapp.com/")

    # 10 sec wait time to load, if good internet connection is not good then increase the time
    # units in seconds
    # note this time is being used below also
    wait = WebDriverWait(driver, 60)
    wait5 = WebDriverWait(driver,50)
    

    # Message to send list
    # 1st Parameter: Hours in 0-23
    # 2nd Parameter: Minutes
    # 3rd Parameter: Seconds (Keep it Zero)
    # 4th Parameter: Message to send at a particular time
    # Put '\n' at the end of the message, it is identified as Enter Key
    # Else uncomment Keys.Enter in the last step if you dont want to use '\n'
    # Keep a nice gap between successive messages
    # Use Keys.SHIFT + Keys.ENTER to give a new line effect in your Message
    msgToSend = [
                    [12, 32, 0, "Hello! This is test Msg. Please Ignore." + Keys.SHIFT + Keys.ENTER + "http://bit.ly/mogjm05"]
                ]

    # Count variable to identify the number of messages to be sent
    count = 0
    while count<len(msgToSend):

        # Identify time
        curTime = datetime.datetime.now()
        curHour = curTime.time().hour
        curMin = curTime.time().minute
        curSec = curTime.time().second

        # if time matches then move further
        if msgToSend[count][0]==curHour and msgToSend[count][1]==curMin and msgToSend[count][2]==curSec:
            # utility variables to tract count of success and fails
            success = 0
            sNo = 1
            failList = []

            # Iterate over selected contacts
            
                print(sNo, ". Target is: " + target)
                sNo+=1
                try:
                    # Select the target
                    x_arg = '//span[contains(@title,' + target + ')]'
                    try:
                        wait5.until(EC.presence_of_element_located((
                            By.XPATH, x_arg
                        )))
                    except:
                        # If contact not found, then search for it
                        searBoxPath = '//*[@id="input-chatlist-search"]'
                        wait5.until(EC.presence_of_element_located((
                            By.ID, "input-chatlist-search"
                        )))
                        inputSearchBox = driver.find_element_by_id("input-chatlist-search")
                        time.sleep(0.5)
                        # click the search button
                        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div/button').click()
                        time.sleep(1)
                        inputSearchBox.clear()
                        inputSearchBox.send_keys(target[1:len(target) - 1])
                        print('Target Searched')
                        # Increase the time if searching a contact is taking a long time
                        time.sleep(4)

            #         # Select the target
            #         driver.find_element_by_xpath(x_arg).click()
            #         print("Target Successfully Selected")
            #         time.sleep(2)

            #         # Select the Input Box
            #         inp_xpath = "//div[@contenteditable='true']"
            #         input_box = wait.until(EC.presence_of_element_located((
            #             By.XPATH, inp_xpath)))
            #         time.sleep(1)

            #         # Send message
            #         # taeget is your target Name and msgToSend is you message
            #         input_box.send_keys("Hello, " + target + "."+ Keys.SHIFT + Keys.ENTER + msgToSend[count][3] + Keys.SPACE) # + Keys.ENTER (Uncomment it if your msg doesnt contain '\n')
            #         # Link Preview Time, Reduce this time, if internet connection is Good
            #         time.sleep(10)
            #         input_box.send_keys(Keys.ENTER)
            #         print("Successfully Send Message to : "+ target + '\n')
            #         success+=1
            #         time.sleep(0.5)

            #     except:
            #         # If target Not found Add it to the failed List
            #         print("Cannot find Target: " + target)
            #         failList.append(target)
            #         pass

            # print("\nSuccessfully Sent to: ", success)
            # print("Failed to Sent to: ", len(failList))
            # print(failList)
            # print('\n\n')
            # count+=1
    driver.quit()
display_menu()