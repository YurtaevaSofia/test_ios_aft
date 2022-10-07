import os
from time import sleep

import numpy as np
from PIL import Image
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException

from pages.p4_set_passcode_page import SetPasscodePage
from pages.p6_summary_page import SummaryPage

words = []


def get_element_search_parameter(element):
    if element[0] == 'id':
        return AppiumBy.ID
    elif element[0] == 'accessibility_id':
        return AppiumBy.ACCESSIBILITY_ID
    elif element[0] == 'xpath':
        return AppiumBy.XPATH
    else:
        return AppiumBy.CUSTOM


def assert_images_equal(image_1: str, image_2: str):
    img1 = Image.open(image_1)
    img2 = Image.open(image_2)

    # Convert to same mode and size for comparison
    img2 = img2.convert(img1.mode)
    img2 = img2.resize(img1.size)

    sum_sq_diff = np.sum((np.asarray(img1).astype('float') - np.asarray(img2).astype('float')) ** 2)

    if sum_sq_diff == 0:
        # Images are exactly the same
        pass
    else:
        normalized_sum_sq_diff = np.sqrt(sum_sq_diff / np.asarray(img1).size)
        assert normalized_sum_sq_diff < 5


class CommonSteps:

    def __init__(self, driver):
        self.driver = driver

    def check_elements_presence(self, element):
        return self.driver.find_element(by=get_element_search_parameter(element), value=element[1]).is_displayed()

    def click_on_element(self, element):
        self.driver.find_element(by=get_element_search_parameter(element), value=element[1]).click()

    def get_element_text(self, element):
        return self.driver.find_element(by=get_element_search_parameter(element), value=element[1]).get_attribute(
            "label")

    def enter_new_passcode(self, passcode):
        passcode_numerals = passcode.split()
        for numeral in passcode_numerals:
            self.click_on_element(SetPasscodePage.get_button_numeral(numeral))

    def wait_for_element_to_appear(self, seconds, element):
        self.driver.implicitly_wait(seconds)
        self.check_elements_presence(element)

    def tap_on_element(self, element):
        actions = TouchAction(self.driver)
        actions.tap(self.driver.find_element(by=get_element_search_parameter(element), value=element[1]))
        actions.perform()

    def check_image_similarity(self, baseline_filename, screenshot_filename):

        generated_file = os.path.join(str("/Users/sofia/PycharmProjects/zerion_ios_aft/tests/screenshots"),
                                      "{}".format(screenshot_filename))

        assert_images_equal(
            "/Users/sofia/PycharmProjects/zerion_ios_aft/resources/baseline_images/{}".format(baseline_filename),
            generated_file)

    def remember_the_seed_phrase(self):
        sleep(3)
        elements = self.driver.find_elements(by='xpath', value='/XCUIElementTypeApplication[@name="Zerion"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]//XCUIElementTypeStaticText')
        for element in elements:
            words.append(element.get_attribute('name'))
        print(words)

    def answer_the_question(self):
        sleep(0.5)
        for i in range(0, 13):
            try:
                self.driver.find_element(by='id', value=str(i))
            except NoSuchElementException:
                continue
            number = i
            break
        secret_word = words[number - 1]
        element = self.driver.find_element(by='id', value=secret_word)
        element.click()

    def answer_the_question_wrong(self):
        sleep(0.5)
        for i in range(0, 13):
            try:
                self.driver.find_element(by='id', value=str(i))
            except NoSuchElementException:
                continue
            number = i
            break
        words.remove(words[number-1])
        print(words)
        for word in words:
            try:
                element = self.driver.find_element(by='id', value=word)
            except NoSuchElementException:
                continue
            element.click()
            break

