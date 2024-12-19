from selenium.webdriver.common.by import By
import time

def test_search_functionality(driver):
    """
    This test checks if items related to a specific keyword are displayed correctly.
    """

    print("Testing search functionality...")

    # Open the menu and verify visibility of the inventory items
    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    search_keyword = "Sauce"

    # Simulate search by checking the names of the inventory items
    matching_items = [item for item in items if search_keyword.lower() in item.text.lower()]

    # Assert that at least one item matches the search keyword
    assert len(matching_items) > 0, f"No items found for search keyword '{search_keyword}'"
    print(f"Search keyword '{search_keyword}' found {len(matching_items)} matching items!")

    # Print matching item names
    for item in matching_items:
        print(f"Matching item: {item.text}")


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

        # Run the search test
        print("Running the search test...")
        test_search_functionality(driver)

    finally:
        print("Closing the browser...")
        driver.quit()
        print("Tests completed successfully!")
