from selenium.webdriver.common.by import By
import time

def test_valid_login(driver):
    # Entering the username
    print("Entering the username...")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(1)

    # Entering the password
    print("Entering the password...")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)

    # Clicking the Login button
    print("Clicking the Login button...")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Verifying successful login by checking the URL
    assert "inventory" in driver.current_url, "Login failed"
    print("Login test passed successfully!")
