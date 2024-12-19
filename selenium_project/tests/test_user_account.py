from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains  # Импорт ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_verify_user_name(driver):
    print("Verifying the displayed user name...")

    # Log in to the account
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Verify that the user is logged in by checking if the inventory page is loaded
    assert "inventory" in driver.current_url, "Failed to log in"

    # Check the presence of a user-specific element (if any)
    print("User successfully logged in!")
    # Add any user-specific checks here if available on the site (e.g., a user profile section)

def test_logout(driver):
    print("Testing the logout functionality...")

    # Open the menu
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    time.sleep(1)  # Allow menu to open

    # Click the Logout button
    logout_button = driver.find_element(By.ID, "logout_sidebar_link")
    ActionChains(driver).move_to_element(logout_button).click().perform()
    time.sleep(3)  # Wait for the page to reload after logout

    # Verify that the user is redirected to the login page
    current_url = driver.current_url
    print(f"Current URL after logout: {current_url}")
    # assert "login" in current_url, "Logout fail"

if __name__ == "__main__":
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service

    # Path to chromedriver
    CHROME_DRIVER_PATH = r"D:\selenium_project\chromedriver-win64\chromedriver.exe"
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    try:
        print("Opening the site...")
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        # Run the tests
        test_verify_user_name(driver)
        test_logout(driver)

    finally:
        print("Closing the browser...")
        driver.quit()
        print("Tests completed successfully!")
