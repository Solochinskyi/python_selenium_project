# Selenium Testing Project for SauceDemo

## 📖 About the Project
This repository contains automated tests for the SauceDemo website. The tests are written in **Python** using the **Selenium** framework and are designed to cover various functionalities of the website, including login, cart operations, inventory management, checkout, and more.

## 🧪 Tests Included
The project includes the following test cases:

- **test_login.py**: Verifies the login functionality using valid credentials.
- **test_inventory.py**:
  - Ensures that inventory items are displayed.
  - Checks if the inventory sorting works as expected (e.g., low-to-high price sorting).
- **test_cart.py**:
  - Validates adding items to the cart.
  - Verifies item details in the cart.
- **test_checkout.py**: Simulates the complete checkout process, from adding an item to the cart to completing the order.
- **test_user_account.py**:
  - Verifies user account details (e.g., username display).
  - Tests the logout functionality.
- **test_responsiveness.py**: Validates the responsiveness of the website by checking elements on different window sizes.
- **test_page_navigation.py**: Tests navigation between different pages of the website (e.g., inventory, cart, checkout).
- **test_remove_from_cart.py**: Verifies the functionality of removing items from the cart.
- **test_error_handling.py**: Ensures that proper error messages are displayed for invalid actions (e.g., logging in with incorrect credentials).
- **test_api.py**: Simulates API interactions (e.g., verifying network requests) using Selenium Wire.
- **test_bulk_actions.py**: Tests bulk actions, such as adding or removing multiple items from the cart.
- **test_filter.py**: Verifies the functionality of applying filters to the inventory.

## 🛠 Technologies Used
- **Python**: Programming language.
- **Selenium**: For browser automation.
- **Selenium Wire**: For intercepting network requests.
- **Pytest**: For test execution.
- **ChromeDriver**: To automate Chrome browser.
- **Virtual Environment**: To isolate dependencies.

## 🚀 How to Run the Tests
### Prerequisites
1. Install Python (version 3.8 or higher).
2. Install Chrome browser.
3. Download and set up ChromeDriver.

