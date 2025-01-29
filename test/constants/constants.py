# We will define a class that can keep all the constants like(can also keep it in .env file
import allure


class Constants:
    def __init__(self):
        print("Constants loaded from  constant.py file")

    @staticmethod
    def app_url():
        return "https://app.vwo.com/"

    @staticmethod
    def app_dashboard_url(self):
        return "https://app.vwo.com/#/dashboard"
