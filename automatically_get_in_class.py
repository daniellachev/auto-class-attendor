from selenium import webdriver
# You need to import selenium and chromedrivers

driver = webdriver.Chrome()
driver.get('https://elearn.uni-sofia.bg/login/index.php')

username = driver.find_element_by_xpath('//*[@id="username"]')
password = driver.find_element_by_xpath('//*[@id="password"]')
login_button = driver.find_element_by_xpath('//*[@id="loginbtn"]')


username.send_keys("enter username")
password.send_keys("enter your password")
login_button.click()

driver.implicitly_wait(0.5)

driver.get('https://elearn.uni-sofia.bg/course/view.php?id=43549')

driver.implicitly_wait(1)

get_in_course = driver.find_element_by_partial_link_text('Упражнение 11 - БАЕ 1 група') #change for each course
get_in_course.click()

driver.implicitly_wait(1)

presentation = driver.find_element_by_partial_link_text('Presentation')
presentation.click()
