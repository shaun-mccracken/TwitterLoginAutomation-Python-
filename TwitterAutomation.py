from selenium import webdriver

username = 'Enter Username'
passowrd = 'Enter Password'

url = 'https://www.twitter.com/login'

#Enter filepath of chromedriver.exe
driver = webdriver.Chrome("")

#Send url to the webdriver
driver.get(url)

#Locate username and password text fields by class name and input corresponding Strings
driver.find_element_by_class_name('js-username-field').send_keys(username)
driver.find_element_by_class_name('js-password-field').send_keys(passowrd)

#Locate login submition field 
driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium').submit()