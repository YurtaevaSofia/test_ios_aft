from time import sleep
from pages.p1_get_started_page import GetStartedPage
import allure


@allure.feature("tests of element presence on pages")
class TestPages:

    @allure.title("get_started_page_check")
    @allure.description("Test checks all elements presented on start_page")
    def test_get_started_page_check(self, common_steps, screenshot_maker):
        common_steps.wait_for_element_to_appear(3, GetStartedPage.get_icon())
        assert (common_steps.check_elements_presence(GetStartedPage.get_icon()))
        assert (common_steps.check_elements_presence(GetStartedPage.get_title1()))
        assert (common_steps.check_elements_presence(GetStartedPage.get_button_get_started()))
        assert (common_steps.get_element_text(GetStartedPage.get_title1()) == "One Wallet To Do It All")
        assert (common_steps.get_element_text(GetStartedPage.get_subtitle1()) == "Turn your phone into Web3 Mission Control with a wallet built for humans, not degens.")
        screenshot_maker.capture_screenshot("screenshot1.png")
        common_steps.check_image_similarity("bi1_one_wallet_to_do_it_all.png", "screenshot1.png")
        sleep(3)
        common_steps.wait_for_element_to_appear(5, GetStartedPage.get_title2())
        screenshot_maker.capture_screenshot("screenshot2.png")
        common_steps.check_image_similarity("bi2_build_a_truly_multichain_portfolio.png", "screenshot2.png")
        assert (common_steps.get_element_text(GetStartedPage.get_title2()) == "Build a Truly Multichain Portfolio")
        assert (common_steps.get_element_text(GetStartedPage.get_subtitle2()) == "Track your complete portfolio across and manage all your private keys in one app.")
        sleep(5)
        common_steps.wait_for_element_to_appear(5, GetStartedPage.get_title3())
        screenshot_maker.capture_screenshot("screenshot3.png")
        common_steps.check_image_similarity("bi3_explore_web3_with_people_you_trust.png", "screenshot3.png")
        assert (common_steps.get_element_text(GetStartedPage.get_title3()) == "Explore Web3 With People You Trust")
        assert (common_steps.get_element_text(GetStartedPage.get_subtitle3()) == "Follow any wallet and NFT collection. Build your own Web3 community and identity.")


