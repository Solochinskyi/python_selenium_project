from selenium.webdriver.common.by import By
import time

def test_add_to_cart(driver):
    print("Checking item addition to the cart...")
    
    # Locate and click the button to add the first item (Sauce Labs Backpack) to the cart
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()  # Simulates clicking the button
    time.sleep(1)  # Pause for the action to complete

    # Locate and click the cart icon to navigate to the cart page
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()  # Simulates clicking the cart icon
    time.sleep(2)  # Pause to allow the cart page to load

    # Verify that at least one item is displayed in the cart
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) > 0, "The item was not added to the cart"  # Assert that the cart is not empty
    print("The item has been successfully added to the cart!")

    # Verify that the item name in the cart matches the expected name
    item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_name == "Sauce Labs Backpack", "The item name in the cart is incorrect"
    print("The item name in the cart has been verified successfully!")
