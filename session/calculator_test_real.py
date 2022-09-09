from appium import webdriver

"""
Desired Capabilities
"""

desired_capabilities = {
    "platformName": "Android",
    "deviceName": "Android Device",
    "appPackage": "com.sec.android.app.popupcalculator",
    "appActivity": "com.sec.android.app.popupcalculator.Calculator"
}

# Create the driver instance
webdriver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)


def nine_plus_ten_real() -> str:
    webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_09").click()
    webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_add").click()
    webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_01").click()
    webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_00").click()
    result: str = webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_tv_result").text
    webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal").click()
    return result


def single_digit_calculation_real(a: str, b: str, op: str) -> str:
    webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_0" + a).click()
    webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_" + op).click()
    webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_0" + b).click()
    result: str = webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_tv_result").text
    webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal").click()
    return result


def multi_digit_calculation_real(a: str, b: str, op: str) -> str:
    calculator_input_real(a)
    webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_" + op).click()
    calculator_input_real(b)
    result: str = webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_tv_result").text
    webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal").click()
    return result


def calculator_input_real(value: str):
    for i in range(0, len(value)):
        webdriver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_0"+value[i]).click()
