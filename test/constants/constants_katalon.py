# We will define a class that can keep all the constants like(can also keep it in .env file
import allure


class ConstantsKatalon:
    def __init__(self):
        print("Constants loaded from  constant_katalon.py file")

    @staticmethod
    def katalon_app_url():
        return "https://katalon-demo-cura.herokuapp.com/"

    @staticmethod
    def app_dashboard_url():
        return "https://app.vwo.com/#/dashboard"
