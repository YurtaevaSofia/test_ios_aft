import os
import pytest
from appium import webdriver


from core.ConfigurationLoader import ConfigurationLoader
from core.ScreenshotMaker import ScreenshotMaker
from steps.CommonSteps import CommonSteps


@pytest.fixture(scope="session")
def configuration():
    return ConfigurationLoader("/Users/sofia/PycharmProjects/zerion_ios_aft/resources/configuration.txt")


@pytest.yield_fixture(scope="function")
def driver(configuration):
    desired_caps = {
        "automationName": configuration.get_automation_name(),
        "app": os.path.expanduser(configuration.get_app()),
        "platformName": configuration.get_platform_name(),
        "platformVersion": configuration.get_platform_version(),
        "deviceName": configuration.get_device_name()
    }
    driver = webdriver.Remote(configuration.get_url(), desired_caps)
    driver.implicitly_wait(10)
    print("Driver started!")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def screenshot_maker(driver):
    return ScreenshotMaker(driver)


@pytest.fixture(scope="function")
def common_steps(driver):
    return CommonSteps(driver)