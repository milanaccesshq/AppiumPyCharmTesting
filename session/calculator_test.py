from appium import webdriver
from time import sleep

"""
Desired Capabilities
"""

desired_capabilities = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "appPackage": "com.android.calculator2",
    "appActivity": "com.android.calculator2.Calculator"
}

# Create the driver instance
webdriver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)


def nine_plus_ten() -> str:
    # Calculate 9 + 10
    webdriver.find_element("id", "com.android.calculator2:id/digit_9").click()
    webdriver.find_element("id", "com.android.calculator2:id/op_add").click()
    webdriver.find_element("id", "com.android.calculator2:id/digit_1").click()
    webdriver.find_element("id", "com.android.calculator2:id/digit_0").click()

    # Assign the result to an element and return it
    result: str = webdriver.find_element("id", "com.android.calculator2:id/result").text
    sleep(1)
    calculation_clear(4)
    return result


def single_digit_calculation(a: str, b: str, op: str) -> str:
    # Calculate (valid operators are "add", "sub", "mul" and "div")
    webdriver.find_element("id", "com.android.calculator2:id/digit_"+a).click()
    webdriver.find_element("id", "com.android.calculator2:id/op_"+op).click()
    webdriver.find_element("id", "com.android.calculator2:id/digit_"+b).click()

    # Assign the result to an element and return it
    result: str = webdriver.find_element("id", "com.android.calculator2:id/result").text
    sleep(1)
    calculation_clear(3)
    return result


def multi_digit_calculation(a: str, b: str, op: str) -> str:
    # Calculate
    calculator_input(a)
    webdriver.find_element("id", "com.android.calculator2:id/op_"+op).click()
    calculator_input(b)

    # Assign the result to an element and return it
    result: str = webdriver.find_element("id", "com.android.calculator2:id/result").text
    sleep(1)
    input_length: int = len(a)+len(b)+1
    calculation_clear(input_length)
    return result


def calculator_input(value: str):
    for i in range(0, len(value)):
        webdriver.find_element("id", "com.android.calculator2:id/digit_"+value[i]).click()


def calculation_clear(length: int):
    for i in range(0, length):
        webdriver.find_element("id", "com.android.calculator2:id/del").click()

