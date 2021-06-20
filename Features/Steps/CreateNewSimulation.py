from behave import *
from selenium import webdriver
import time

option_project_xpath = "//*[@id='root']/div/div[1]/nav/div[2]/div[1]/div[2]/div"
headline_xpath="//span[@class='saved-project__headline__name__text']"
new_simulation_xpath="//button[@class='button button--accent button-icon saved-project__button--new-simulation']"
button_next_xpath="//button[@class='button button--accent button-icon settings-form__submit']"
simulation_name_xpath="//div[@class='saved-config--pct-width__title__name']"
simulation_setting_icon_xpath="//div[@class='saved-config__cog']"
delete_simulation="//button[@class='context-menu--options-button ']//p[contains(text(),'Delete')]"
confirm_delete_xpath="//div[@class='warning-modal__container']//button[@class='button button--accent']"
simulation_list_xpath="//div[@class='saved-config__list']"

@when(u'verify project "{Project_Name}" is created')
def validate_project_is_already_created(context, Project_Name):
    context.driver.find_element_by_xpath(option_project_xpath).click()
    project_name_title=context.driver.find_element_by_xpath(headline_xpath).text
    if project_name_title==Project_Name:
        assert True, "project exists, proceed with new simulation"
    else:
        context.driver.save_screenshot(".\\Screenshots\\" + "validate_project_is_already_created.png")
        assert False, "Project is not created, please create new project first"

@then(u'Click on expand button to expand created project')
def click_on_expand_button(context):
    try:
        context.driver.find_element_by_xpath(headline_xpath).click()
    except ElementClickInterceptedException:
        assert False, "other element is on the way"

@then(u'verify if simulation is already is created then delete it')
def validate_simulation_if_already_exits(context):
    simulation_list=context.driver.find_element_by_xpath(simulation_list_xpath).text
    if simulation_list=="No simulations to show for this project":
        pass
    else:
        simulation_name = context.driver.find_element_by_xpath(simulation_name_xpath).text
        if simulation_name == "default simulation":
            context.driver.find_element_by_xpath(simulation_setting_icon_xpath).click()
            context.driver.find_element_by_xpath(delete_simulation).click()
            time.sleep(2)
            context.driver.find_element_by_xpath(confirm_delete_xpath).click()
        else:
            pass

@then(u'Click on New Simulation button')
def click_on_new_simulation_icon(context):
    try:
        context.driver.find_element_by_xpath(new_simulation_xpath).click()
    except ElementClickInterceptedException:
        assert False, "other element is on the way"

@then(u'Click on plus icon to add first node')
def click_on_next(context):
    try:
        context.driver.find_element_by_xpath(button_next_xpath).click()
        time.sleep(2)
    except ElementClickInterceptedException:
        assert False, "other element is on the way"


@then(u'Click on Project icon from left panel')
def back_to_projects(context):
    try:
        context.driver.find_element_by_xpath(option_project_xpath).click()
        time.sleep(2)
    except ElementClickInterceptedException:
        assert False, "other element is on the way"

@then(u'Verify default simulation is added into project')
def validate_simulation_created(context):
    simulation_name=context.driver.find_element_by_xpath(simulation_name_xpath).text
    time.sleep(5)
    if simulation_name == "default simulation":
        context.driver.close()
        assert True, "default simulation created"
    else:
        context.driver.save_screenshot(".\\Screenshots\\" + "validate_simulation_created.png")
        context.driver.close()
        assert False, "default simulation is not created"