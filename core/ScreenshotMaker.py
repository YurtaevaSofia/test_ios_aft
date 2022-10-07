class ScreenshotMaker:
    def __init__(self, driver):
        self.driver = driver

    def capture_screenshot(self, name):
        return self.driver.save_screenshot(
            "/Users/sofia/PycharmProjects/zerion_ios_aft/tests/screenshots/" + name)
