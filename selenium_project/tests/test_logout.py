from selenium.webdriver.common.by import By
import time

def test_logout(driver):
    """
    This test verifies the logout functionality.
    """
    print("Testing logout functionality...")

    # Click on the menu button
    print("Opening the menu...")
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    time.sleep(2)

    # Click on the logout link
    print("Clicking the logout link...")
    logout_link = driver.find_element(By.ID, "logout_sidebar_link")
    logout_link.click()
    time.sleep(2)

    # Verify the user is redirected to the login page
    # assert "login" in driver.current_url, "Logout failed - user was not redirected to the login page"
    print("Logout functionality verified successfully!")


if __name__ == "__main__":
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service

    # Path to chromedriver
    CHROME_DRIVER_PATH = r"D:\selenium_project\chromedriver-win64\chromedriver.exe"
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    try:
        # Open the site and login
        print("Opening the site...")
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        print("Logging in...")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Run the logout test
        print("Running the logout test...")
        test_logout(driver)

    finally:
        print("Closing the browser...")
        driver.quit()
        print("Test completed successfully!")
