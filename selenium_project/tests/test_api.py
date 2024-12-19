from seleniumwire import webdriver  # Selenium Wire is needed to intercept network requests
from selenium.webdriver.common.by import By
import json
import time


def test_api_request(driver):
    """
    Test to validate API request during login and verify response.
    """
    print("Testing API request interception...")

    # Perform login to trigger API request
    print("Performing login...")
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Intercept network requests
    for request in driver.requests:
        if request.response and "login" in request.url:  # Check if it's a login-related request
            print(f"Intercepted API request to: {request.url}")
            print(f"Request method: {request.method}")
            print(f"Response status code: {request.response.status_code}")
            print(f"Response body: {request.response.body.decode('utf-8')}")
            # Validate the response
            assert request.response.status_code == 200, "Login API did not return a success status!"
            break
    else:
        raise AssertionError("No login API request intercepted!")
    print("API request test passed successfully!")


if __name__ == "__main__":
    from selenium.webdriver.chrome.service import Service

    # Path to chromedriver
    CHROME_DRIVER_PATH = r"D:\selenium_project\chromedriver-win64\chromedriver.exe"
    service = Service(CHROME_DRIVER_PATH)

    # Set up Selenium Wire driver to intercept requests
    driver = webdriver.Chrome(service=service)

    try:
        # Run the API test
        test_api_request(driver)
    finally:
        print("Closing the browser...")
        driver.quit()
        print("API test completed successfully!")
