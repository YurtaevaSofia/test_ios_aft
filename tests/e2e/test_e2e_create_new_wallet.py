from time import sleep

from pages.p3_create_or_import_page import CreateOrImportPage
from pages.p5_generating_wallet_page import GeneratingWalletPage
from pages.p1_get_started_page import GetStartedPage
import allure
from pages.p2_introducing_zerion_wallet_page import IntroducingZerionWalletPage


@allure.feature("tests for wallet creation")
class TestWalletCreation:

    @allure.title("e2e test for wallet creation")
    @allure.description("Test checks happy case of wallet creation by new user")
    def test_e2e_wallet_creation(self, common_steps, screenshot_maker):
        common_steps.click_on_element(GetStartedPage.get_button_get_started())
        common_steps.click_on_element(IntroducingZerionWalletPage.get_button())
        common_steps.click_on_element(CreateOrImportPage.get_button_create_new_wallet())
        common_steps.enter_new_passcode("8 2 5 4 7 6")
        common_steps.enter_new_passcode("8 2 5 4 7 6")
        common_steps.wait_for_element_to_appear(20, GeneratingWalletPage.get_subtitle_owner_of())
        assert common_steps.get_element_text(GeneratingWalletPage.get_button_generating()) == "Finish", \
            screenshot_maker.capture_screenshot("error_in_button_text.png")
        sleep(3)








