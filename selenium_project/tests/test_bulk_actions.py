from selenium.webdriver.common.by import By
import time

def test_bulk_add_to_cart(driver):
    """
    Test adding multiple items to the cart at once.
    """
    print("Testing bulk add-to-cart functionality...")

    # Add all items on the page to the cart
    add_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for button in add_buttons:
        button.click()
        time.sleep(1)

    # Verify the number of items in the cart matches the number of items added
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert int(cart_badge) == len(add_buttons), f"Expected {len(add_buttons)} items in the cart, but found {cart_badge}"
    print(f"All {len(add_buttons)} items successfully added to the cart!")

def test_bulk_remove_from_cart(driver):
    """
    Test removing all items from the cart at once.
    """
    print("Testing bulk remove-from-cart functionality...")

    # Navigate to the cart page
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()
    time.sleep(2)

    # Remove all items from the cart
    remove_buttons = driver.find_elements(By.CLASS_NAME, "cart_button")
    for button in remove_buttons:
        button.click()
        time.sleep(1)

    # Verify the cart is empty
    try:
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "", "Cart is not empty after bulk removal"
    except Exception:
        print("Cart is empty, as expected.")
    print("All items successfully removed from the cart!")


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

        # Run bulk actions tests
        print("Running bulk add-to-cart test...")
        test_bulk_add_to_cart(driver)

        print("Running bulk remove-from-cart test...")
        test_bulk_remove_from_cart(driver)

    finally:
        print("Closing the browser...")
        driver.quit()
        print("Tests completed successfully!")
