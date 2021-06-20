from behave import *
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from Utilities.ReadProperty import ReadConfig

button_Login_xpath = "//button[@class='button button--accent button-icon']"
textbox_username_id = "email"
textbox_password_id = "password"
button_login_xpath = "//button[@class='button button--accent']"
header_class_name = "header__page-title"
button_logout_xpath = ""

baseUrl = ReadConfig.getApplicationURL()
Browser = ReadConfig.getBrowserName()


@given(u'Launch the browser')
def open_browser(context):
    if Browser == 'Chrome':
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('start-maximized')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('--disable-extensions')
        context.driver = webdriver.Chrome(executable_path="./Drivers/chromedriver.exe", chrome_options=chrome_options)
        context.driver.implicitly_wait(10)
    elif Browser == 'Firefox':
        context.driver = webdriver.Firefox(executable_path="./Drivers/geckodriver.exe")
        context.driver.implicitly_wait(10)


@when(u'Open D3A homepage')
def open_home_page(context):
    context.driver.get(baseUrl)


@when(u'Click on Login button from D3A homepage')
def click_on_login_button(context):
    try:
        context.driver.find_element_by_xpath(button_Login_xpath).click()
    except ElementClickInterceptedException:
        assert False, "other element is on the way"

@when(u'Enter username "{username}" and password "{password}"')
def enter_credentails(context, username, password):
    context.driver.find_element_by_id(textbox_username_id).clear()
    context.driver.find_element_by_id(textbox_username_id).send_keys(username)
    context.driver.find_element_by_id(textbox_password_id).clear()
    context.driver.find_element_by_id(textbox_password_id).send_keys(password)


@when(u'Click on login button')
def click_on_login_button(context):
    try:
        context.driver.find_element_by_xpath(button_login_xpath).click()
        time.sleep(2)
    except ElementClickInterceptedException:
        assert False, "other element is on the way"


@then(u'verify that the logged in successfully')
def login_success(context):
    try:
        header = context.driver.find_element_by_class_name(header_class_name).text
    except StaleElementReferenceException:
        context.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
        context.driver.close()
        assert False, "Test failed"
    if header == "Home":
        context.driver.close()
        assert True, "Test Passed"
    else:
        context.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
        context.driver.close()
        assert False, "Test failed"
