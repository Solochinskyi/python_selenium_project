from selenium.webdriver.common.by import By
import time

def test_filter_functionality(driver):
    """
    This test verifies the functionality of product filtering.
    """
    print("Testing product filtering functionality...")

    # Locate the filter dropdown
    print("Opening the filter dropdown...")
    filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    filter_dropdown.click()
    time.sleep(1)

    # Apply filter: "Price (low to high)"
    print("Applying 'Price (low to high)' filter...")
    filter_option = driver.find_element(By.XPATH, "//option[@value='lohi']")
    filter_option.click()
    time.sleep(2)

    # Verify that products are sorted by price in ascending order
    print("Verifying that products are sorted by price...")
    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    price_values = [float(price.text.replace("$", "")) for price in prices]
    assert price_values == sorted(price_values), "Products are not sorted by price in ascending order"
    print("Filter functionality verified successfully!")


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

        # Run the filter test
        print("Running the filter test...")
        test_filter_functionality(driver)

    finally:
        print("Closing the browser...")
        driver.quit()
        print("Test completed successfully!")
