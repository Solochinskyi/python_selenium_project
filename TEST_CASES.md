# Test Cases for Selenium Project

## 1. test_login.py

### Test Case 1: Successful Login
- **Objective:** Verify that a valid user can log in successfully.
- **Steps:**
  1. Open the SauceDemo website.
  2. Enter valid credentials:
     - Username: `standard_user`
     - Password: `secret_sauce`
  3. Click the "Login" button.
- **Expected Result:**
  - User is redirected to the inventory page.
  - URL contains `/inventory`.

### Test Case 2: Invalid Login
- **Objective:** Verify that login fails with invalid credentials.
- **Steps:**
  1. Open the SauceDemo website.
  2. Enter invalid credentials:
     - Username: `invalid_user`
     - Password: `wrong_password`
  3. Click the "Login" button.
- **Expected Result:**
  - Error message appears: `Epic sadface: Username and password do not match any user in this service.`

---

## 2. test_inventory.py

### Test Case 1: Inventory Display
- **Objective:** Verify that inventory items are displayed on the page.
- **Steps:**
  1. Log in as a valid user.
  2. Verify the presence of elements with the class `inventory_item`.
- **Expected Result:**
  - At least one inventory item is displayed.

### Test Case 2: Inventory Sorting
- **Objective:** Validate sorting functionality (Low to High).
- **Steps:**
  1. Log in as a valid user.
  2. Select the "Low to High" option in the sort dropdown.
  3. Verify that item prices are sorted in ascending order.
- **Expected Result:**
  - Item prices are displayed in ascending order.

---

## 3. test_cart.py

### Test Case 1: Add Item to Cart
- **Objective:** Verify that items can be added to the cart.
- **Steps:**
  1. Log in as a valid user.
  2. Click on the "Add to Cart" button for a specific item.
  3. Go to the cart page.
  4. Verify that the item appears in the cart.
- **Expected Result:**
  - Item is displayed in the cart.

---

## 4. test_checkout.py

### Test Case 1: Complete Checkout Process
- **Objective:** Verify the complete checkout process, from adding an item to completing the order.
- **Steps:**
  1. Log in as a valid user.
  2. Add an item to the cart.
  3. Proceed to the cart page.
  4. Click "Checkout."
  5. Fill in the checkout form:
     - First Name: `John`
     - Last Name: `Doe`
     - Postal Code: `12345`
  6. Click "Continue."
  7. Verify the order summary and click "Finish."
- **Expected Result:**
  - Order confirmation page is displayed with the message: `Thank you for your order!`

---

## 5. test_user_account.py

### Test Case 1: Verify User Account Details
- **Objective:** Verify that user account details are displayed correctly.
- **Steps:**
  1. Log in as a valid user.
  2. Verify that the username is displayed on the page.
- **Expected Result:**
  - Username is displayed.

### Test Case 2: Logout Functionality
- **Objective:** Verify that the user can log out successfully.
- **Steps:**
  1. Log in as a valid user.
  2. Click the logout button.
  3. Verify that the user is redirected to the login page.
- **Expected Result:**
  - User is redirected to the login page.

---

## 6. test_responsiveness.py

### Test Case 1: Validate Responsiveness
- **Objective:** Validate the responsiveness of the website by checking elements on different window sizes.
- **Steps:**
  1. Resize the browser window to various sizes (e.g., mobile, tablet, desktop).
  2. Verify that all critical elements are visible and functional.
- **Expected Result:**
  - Elements adjust appropriately to the screen size.

---

## 7. test_page_navigation.py

### Test Case 1: Verify Page Navigation
- **Objective:** Verify navigation between different pages of the website.
- **Steps:**
  1. Log in as a valid user.
  2. Navigate to the inventory page, cart page, and checkout page.
  3. Verify that each page loads successfully.
- **Expected Result:**
  - Each page loads without errors.

---

## 8. test_remove_from_cart.py

### Test Case 1: Remove Item from Cart
- **Objective:** Verify that items can be removed from the cart.
- **Steps:**
  1. Log in as a valid user.
  2. Add an item to the cart.
  3. Go to the cart page.
  4. Click the "Remove" button for the item.
  5. Verify that the item is no longer in the cart.
- **Expected Result:**
  - Item is removed from the cart.

---

## 9. test_error_handling.py

### Test Case 1: Verify Error Handling
- **Objective:** Ensure proper error messages are displayed for invalid actions.
- **Steps:**
  1. Attempt to log in with invalid credentials.
  2. Attempt to checkout with an empty cart.
- **Expected Result:**
  - Appropriate error messages are displayed.

---

## 10. test_api.py

### Test Case 1: Verify API Interactions
- **Objective:** Simulate API interactions and verify network requests using Selenium Wire.
- **Steps:**
  1. Perform an action that triggers an API request (e.g., login or add to cart).
  2. Intercept and log the API request.
  3. Verify the API response data.
- **Expected Result:**
  - API response matches the expected data.

---

## 11. test_bulk_actions.py

### Test Case 1: Verify Bulk Actions
- **Objective:** Test bulk actions such as adding or removing multiple items.
- **Steps:**
  1. Log in as a valid user.
  2. Add multiple items to the cart.
  3. Verify that all items are displayed in the cart.
  4. Remove all items from the cart.
  5. Verify that the cart is empty.
- **Expected Result:**
  - Bulk actions work as expected.

---

## 12. test_filter.py

### Test Case 1: Verify Inventory Filters
- **Objective:** Verify the functionality of applying filters to the inventory.
- **Steps:**
  1. Log in as a valid user.
  2. Apply a filter (e.g., "Price: Low to High").
  3. Verify that the filter is applied correctly.
- **Expected Result:**
  - Items are displayed according to the selected filter.
