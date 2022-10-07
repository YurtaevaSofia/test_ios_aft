import json
import sys


class ConfigurationLoader:

    def __init__(self, filename):
        try:
            f = open(filename, 'r')
            json_data = f.read()
            print(json_data)
            self.config = json.loads(json_data, strict=False)
            print("Configuration loaded from " + filename)
        except IOError as ex:
            print("Error in loading configuration", ex)
            sys.exit()

    def get_platform_name(self):
        return self.config.get("platformName")

    def get_platform_version(self):
        return self.config.get("platformVersion")

    def get_device_name(self):
        return self.config.get("deviceName")

    def get_app(self):
        return self.config.get("app")

    def get_url(self):
        return self.config.get("url")

    def get_automation_name(self):
        return self.config.get("automationName")

