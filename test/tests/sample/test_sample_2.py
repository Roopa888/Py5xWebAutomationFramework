# To check if the framework is properly arranged and can be run #initial commit was not successful.So just added thsi new file as copy of first test_sample
import pytest
import allure
import time
@allure.title("Dry run of the Framework 1")
@allure.description("Verify that the dry run is working")
@allure.feature("TC#0-Sample test run")
@pytest.mark.sample
def test_sample_pass():
    print("Hello Sample")
    assert True==True
@allure.title("Dry run of the Framework 2")
@allure.description("Verify that the dry run is working")
@allure.feature("TC#1-Sample test run")
@pytest.mark.sample
def test_sample_fail():
    print("Hello Sample")
    assert True==False