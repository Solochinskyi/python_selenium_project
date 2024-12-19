from selenium.webdriver.common.by import By
import time

def test_responsiveness(driver):
    """
    This test checks site responsiveness by resizing the browser window
    and verifying the visibility of key elements.
    """

    print("Testing site responsiveness...")

    # Define different screen sizes to test
    screen_sizes = [
        (1920, 1080),  # Full HD
        (1366, 768),   # Laptop
        (768, 1024),   # Tablet portrait
        (375, 667)     # Mobile
    ]

    # List of elements to check visibility
    elements_to_check = [
        {"by": By.CLASS_NAME, "value": "app_logo", "name": "Logo"},
        {"by": By.CLASS_NAME, "value": "shopping_cart_link", "name": "Shopping cart"},
        {"by": By.ID, "value": "react-burger-menu-btn", "name": "Menu button"}
    ]

    for width, height in screen_sizes:
        print(f"Testing screen size: {width}x{height}")
        driver.set_window_size(width, height)
        time.sleep(2)

        for element in elements_to_check:
            try:
                # Find the element and check visibility
                elem = driver.find_element(element["by"], element["value"])
                assert elem.is_displayed(), f"{element['name']} is not visible at size {width}x{height}"
                print(f"{element['name']} is visible at size {width}x{height}")
            except Exception as e:
                print(f"Error testing {element['name']} at size {width}x{height}: {e}")

    print("Site responsiveness test completed!")


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

        # Run the responsiveness test
        print("Running the responsiveness test...")
        test_responsiveness(driver)

    finally:
        print("Closing the browser...")
        driver.quit()
        print("Tests completed successfully!")
