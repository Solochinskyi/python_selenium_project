from selenium.webdriver.common.by import By
import time

def test_page_navigation(driver):
    """
    This test verifies navigation between different pages on the site.
    """
    print("Testing page navigation functionality...")

    # Navigate to the inventory page (assumes login is complete)
    print("Navigating to the inventory page...")
    driver.get("https://www.saucedemo.com/inventory.html")
    time.sleep(2)

    # Click on a product to navigate to its details page
    print("Navigating to the product details page...")
    product_link = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    product_name = product_link.text  # Save product name for validation
    product_link.click()
    time.sleep(2)

    # Verify we are on the product details page
    product_details_title = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
    assert product_name == product_details_title, "Product details page navigation failed"
    print("Product details page navigation verified successfully!")

    # Navigate back to the inventory page
    print("Navigating back to the inventory page...")
    back_button = driver.find_element(By.CLASS_NAME, "inventory_details_back_button")
    back_button.click()
    time.sleep(2)

    # Verify we are back on the inventory page
    assert "inventory" in driver.current_url, "Failed to navigate back to the inventory page"
    print("Navigation back to the inventory page verified successfully!")


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

        # Run the page navigation test
        print("Running the page navigation test...")
        test_page_navigation(driver)

    finally:
        print("Closing the browser...")
        driver.quit()
        print("Test completed successfully!")
