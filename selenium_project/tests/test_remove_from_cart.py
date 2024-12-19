from selenium.webdriver.common.by import By
import time

def test_remove_from_cart(driver):
    """
    This test verifies that an item can be removed from the cart.
    """
    print("Testing removal of an item from the cart...")

    # Add an item to the cart
    print("Adding item to the cart...")
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()
    time.sleep(1)

    # Navigate to the cart
    print("Navigating to the cart...")
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()
    time.sleep(2)

    # Remove the item from the cart
    print("Removing the item from the cart...")
    remove_button = driver.find_element(By.ID, "remove-sauce-labs-backpack")
    remove_button.click()
    time.sleep(1)

    # Verify the item is removed
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 0, "The item was not removed from the cart"
    print("The item was successfully removed from the cart!")


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

        # Run the remove from cart test
        print("Running the remove from cart test...")
        test_remove_from_cart(driver)

    finally:
        print("Closing the browser...")
        driver.quit()
        print("Test completed successfully!")
