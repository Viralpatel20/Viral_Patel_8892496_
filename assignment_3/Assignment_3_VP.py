# Importing required libraries

# gitpip install selenium

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the apple homepage
driver.get("https://www.apple.com/ca/")
driver.maximize_window()  # Maximizing the browser window
time.sleep(5)

# select apple brand
ipad_button = driver.find_element("xpath", "/html/body/div[1]/nav/div/ul/li[2]/div/div/div[3]/ul/li[1]/a/span[1]")
ipad_button.click()

# Waiting for the page to load
time.sleep(5)

# select I pad version like pro

ipad_pro_buuton = driver.find_element("xpath", "/html/body/nav/div/ul/li[1]/a/figure")
ipad_pro_buuton.click()

time.sleep(5)

# Select ipad buy

ipad_screen_length = driver.find_element("xpath", "/html/body/nav/div/div[2]/div[2]/div[2]/div[2]/a")
ipad_screen_length.click()

time.sleep(5)
# Clicking on "watch altra" link
ipad_size = driver.find_element("xpath",
                                "/html/body/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[1]/fieldset/div/div[2]/label/span/span[1]")
ipad_size.click()

# Waiting for the page to load
time.sleep(5)

# # Selecting a product from the  results I_pad
# # Product_link = driver.find_element_by_css_selector("span[data-component-type='s-product-image'] a")
ipad_colour = driver.find_element("xpath",
                                   "/html/body/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[2]/fieldset/div/div[1]/label")
ipad_colour.click()
# # Product_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
# #
time.sleep(5)

# Clicking on this we can select I_pad size
size_button = driver.find_element("xpath",
                                  "/html/body/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[3]/fieldset/div/div[2]/label")
size_button.click()

# Waiting for the size selection to take effect
time.sleep(5)

# Waiting for the select the storage
ipad_Storage_button = driver.find_element("xpath",
                                          "/html/body/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[4]/fieldset/div/div[2]/label/span/span[1]/span")
ipad_Storage_button.click()

time.sleep(5)


# Waiting for the Wi-Fi only or choose another one
with_sim_button = driver.find_element( "xpath",
                                       "/html/body/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[5]/div/div/div/fieldset/div/div[2]/label")
with_sim_button.click()

time.sleep(5)

# adding Engraving on IPad
name_on_ipad_button = driver.find_element("xpath",
                                          "/html/body/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[6]/fieldset/button[2]")
name_on_ipad_button.click()

time.sleep(5)

# Buying Ipad without pencil
buy_pencil_button = driver.find_element("xpath",
                                        "/html/body/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[8]/fieldset/button[3]")
buy_pencil_button.click()


time.sleep(5)

# add Keyboard
buy_keyboard_button = driver.find_element("xpath",
                                          "/html/body/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[8]/fieldset/button[3]")
buy_keyboard_button.click()

time.sleep(2)

# with trade-in or without trede-in
notrede_button = driver.find_element("xpath",
                                     "/html/body/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[9]/div[2]/div[1]/div/section/div[1]/div/fieldset/div/div[2]/label/span/span")
notrede_button.click()

time.sleep(5)

# Protection plan
apple_care_plan = driver.find_element("xpath",
                                      "/html/body/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[11]/fieldset/div[2]/div/label")
apple_care_plan.click()

time.sleep(5)

# # Adding the ipad Product to buy in bag
add_to_bag_button = driver.find_element("xpath",
                                        "/html/body/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div[12]/div/div[5]/div/div/span/form/div/span/button")
add_to_bag_button.click()

time.sleep(5)

# # Clicking on the titanium case with green alpoine loop
Login_button = driver.find_element("xpath", "")
actions = ActionChains(driver)
actions.move_to_element(Login_button).click().perform()
time.sleep(5)

# Closing the webdriver
driver.quit()

