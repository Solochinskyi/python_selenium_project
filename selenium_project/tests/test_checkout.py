from selenium.webdriver.common.by import By
import time

def test_checkout_process(driver):
    print("Checking the checkout process...")

    # Add a product to the cart
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()
    time.sleep(1)  # Pause for clarity

    # Navigate to the cart
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()
    time.sleep(2)

    # Click the Checkout button
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    time.sleep(2)

    # Fill in the checkout form
    driver.find_element(By.ID, "first-name").send_keys("Ivan")
    driver.find_element(By.ID, "last-name").send_keys("Ivanov")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    time.sleep(1)

    # Click the Continue button
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    # Verify that the user is on the order confirmation page
    assert "checkout-step-two" in driver.current_url, "Failed to navigate to the order confirmation page"
    print("Successfully navigated to the order confirmation page!")

    # Click Finish and check the success message
    driver.find_element(By.ID, "finish").click()
    success_message = driver.find_element(By.CLASS_NAME, "complete-header")
    assert success_message.text == "Thank you for your order!", "The order was not completed successfully"
    print("Order successfully completed!")



if __name__ == "__main__":
    from selenium import webdriver  # Importing the Selenium WebDriver module
    from selenium.webdriver.chrome.service import Service  # To manage the ChromeDriver service
    from selenium.webdriver.common.by import By  # To locate elements on the web page
    import time  # Importing time for adding pauses between actions

    # Path to the ChromeDriver executable
    CHROME_DRIVER_PATH = r"D:\selenium_project\chromedriver-win64\chromedriver.exe"
    service = Service(CHROME_DRIVER_PATH)  # Creating a ChromeDriver service instance
    driver = webdriver.Chrome(service=service)  # Initializing the Chrome WebDriver using the service

    try:
        # Opening the website and logging in
        print("Opening the website...")
        driver.get("https://www.saucedemo.com/")  # Navigating to the specified URL
        time.sleep(2)  # Pause to allow the page to load

        print("Performing login...")
        # Locating the username input field by its ID and entering the username
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # Locating the password input field by its ID and entering the password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # Locating and clicking the login button
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)  # Pause to allow the next page to load

        # Calling the test function for the checkout process
        print("Running the checkout test...")
        test_checkout_process(driver)  # This function should be defined earlier or imported

    finally:
        # Closing the browser after the test completes
        print("Closing the browser...")
        driver.quit()  # Ensures the browser instance is closed
        print("Tests completed successfully!")

