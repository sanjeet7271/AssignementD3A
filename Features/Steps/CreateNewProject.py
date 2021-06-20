from behave import *
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


option_project_xpath = "//*[@id='root']/div/div[1]/nav/div[2]/div[1]/div[2]/div"
button_project_xpath = "//*[@id='root']/div/div[2]/header/div[3]/button[2]"
textbox_projectname_id = "//*[@id='input-field-name']"
textbox_project_description_id = "//*[@id='textarea-field-nameTextArea']"
button_add_project_xpath = "//div[@class='library-name-modal__container']//button"
headline_xpath="//span[@class='saved-project__headline__name__text']"
setting_icon_xpath="//div[@class='saved-project__cog']"
delete_project="//button[@class='context-menu--options-button ']//p[contains(text(),'Delete')]"
confirm_delete_xpath="//div[@class='warning-modal__container']//button[@class='button button--accent']"

@when(u'project "{Project_Name}" is already exits then delete it')
def delete_exiting_Project(context, Project_Name):
    context.driver.find_element_by_xpath(option_project_xpath).click()
    project_name_text = context.driver.find_element_by_xpath(headline_xpath).text
    if project_name_text==Project_Name:
        context.driver.find_element_by_xpath(setting_icon_xpath).click()
        context.driver.find_element_by_xpath(delete_project).click()
        time.sleep(2)
        context.driver.find_element_by_xpath(confirm_delete_xpath).click()
    else:
        pass

@when(u'Click on Projects')
def click_on_project(context):
    try:
        context.driver.find_element_by_xpath(option_project_xpath).click()
    except ElementClickInterceptedException:
        assert False, "other element is on the way"

@then(u'Click on New Project')
def click_on_new_project(context):
    try:
        context.driver.find_element_by_xpath(button_project_xpath).click()
        time.sleep(5)
    except ElementClickInterceptedException:
        assert False, "other element is on the way"

@then(u'Enter Project Name "{Project_Name}" and Project Description "{Project_Description}"')
def enter_name_of_project_and_its_description(context, Project_Name, Project_Description):
    project_name=context.driver.find_element_by_xpath(textbox_projectname_id)
    project_name.send_keys(Project_Name)
    project_description = context.driver.find_element_by_xpath(textbox_project_description_id)
    project_description.send_keys(Project_Description)

@then(u'Add the Project')
def add_project(context):
    try:
        context.driver.find_element_by_xpath(button_add_project_xpath).click()
        time.sleep(5)
    except ElementClickInterceptedException:
        assert False, "other element is on the way"

@then(u'Verify Project "{Project_Name}" added successfully')
def validate_added_project(context, Project_Name):
    project_name_text=context.driver.find_element_by_xpath(headline_xpath).text
    if project_name_text==Project_Name:
        context.driver.close()
        assert True, "Test Passed"
    else:
        context.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
        context.driver.close()
        assert False, "Test failed"
    time.sleep(5)

