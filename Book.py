from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

#start
driver = webdriver.Chrome("") #path for your chromedriver.exe file
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(3)
#login
login = driver.find_element_by_id("nav-link-accountList")
login.click()
user_name = driver.find_element_by_id("ap_email")
user_name.send_keys("Your Login details") #enter your details first before run
con = driver.find_element_by_class_name("a-button-input")
con.click()
password = driver.find_element_by_id("ap_password")
password.send_keys("Password")#enter your password
submit = driver.find_element_by_class_name("a-button-input")
submit.click()




#switch from all to books
action = ActionChains(driver)
All_tab = driver.find_element_by_id("searchDropdownBox")
action.move_to_element(All_tab).click().perform()
time.sleep(2)
book_tab = driver.execute_script('return document.querySelector("#searchDropdownBox > option:nth-child(11)");').click()

#Now time to search Paulo Coehlo book
search = driver.find_element_by_id('twotabsearchtextbox')
search.click()
search.send_keys("paulo coelho books")
Enter = driver.find_element_by_id("nav-search-submit-button")
Enter.click()
driver.implicitly_wait(2)

#scroll down to the books Eleven Minutes
scrollToBook = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[5]/div/span/div/div/div[1]')
driver.execute_script("arguments[0].scrollIntoView();",scrollToBook)
driver.execute_script("window.scrollBy(0 , -100);")
time.sleep(2)

#click on book
book_link = driver.find_element_by_link_text("Eleven Minutes")
book_link.click()
time.sleep(2)
# current window handle
parent_Tab = driver.current_window_handle

# all open window handles
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
time.sleep(2)
#add to card
card = driver.find_element_by_id("add-to-cart-button")
card.click()
time.sleep(2)

# Now open card to check that the product is added or not
driver.find_element_by_id('hlb-view-cart-announce').click()
