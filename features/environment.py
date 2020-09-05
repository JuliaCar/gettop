from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import AbstractEventListener
from gettop.app.application import Application
# from features.logger import MyListener, logger

bs_user = 'juliacardenas2'
bs_pw = 'psm5yzFRSPWPDpf3Y6Aq'

def browser_init(context, name):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome()
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(chrome_options = options)

    ### EventFiringWebDriver - log file ###

    ### for drivers ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    # ### for browerstack ###
    # desired_cap = {
    #     'browser': 'Chrome',
    #     'browser_version': '84.0',
    #     'os': 'Windows',
    #     'os_version': '10',
    #     'name': name
    # }
    # url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities = desired_cap)
    # BROWSERSTACK_URL = 'https://juliacardenas2:psm5yzFRSPWPDpf3Y6Aq@hub-cloud.browserstack.com/wd/hub'
    # driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)
    context.driver.wait = WebDriverWait(context.driver, 15)


def before_scenario(context, scenario):
    #logger.info(f'\nStarted scenario: {scenario.name}')
    print(f'\nStarted scenario: ', scenario.name)
    browser_init(context,scenario.name)


def before_step(context, step):
    print(f'\nStarted step: {step}')
    #logger.info(f'\nStarted step: {step}')

def after_step(context, step):
    if step.status == 'failed':
        print(f'\nStep failed: {step}')
        #logger.info(f'\nStep failed: {step}')

def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
