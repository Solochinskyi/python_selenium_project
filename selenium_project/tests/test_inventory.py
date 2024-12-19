from selenium.webdriver.common.by import By
import time

def test_inventory_display(driver):
    # Checking the display of items
    print("Checking the display of items...")
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0, "No items are displayed"
    print(f"Number of items found: {len(items)}")

def test_sort_inventory(driver):
    # Checking the sorting of items
    print("Checking the sorting of items...")

    # Opening the dropdown menu and selecting "Low to High" sorting
    sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    sort_dropdown.click()
    sort_dropdown.find_element(By.XPATH, "//option[@value='lohi']").click()
    time.sleep(2)

    # Collecting item prices displayed on the page
    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    price_values = [float(price.text.replace("$", "")) for price in prices]

    # Verifying that the prices are sorted in ascending order
    assert price_values == sorted(price_values), "Items are not sorted by price"
    print("Item sorting by price has been verified successfully!")
