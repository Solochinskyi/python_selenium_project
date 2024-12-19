# Test Cases for Selenium Project

## 📋 Test Cases

### **1. test_login.py**
#### **Test Case 1: Successful Login**
- **Objective:** Verify that a valid user can log in successfully.
- **Steps:**
  1. Open the SauceDemo website.
  2. Enter valid credentials:
     - Username: `standard_user`
     - Password: `secret_sauce`.
  3. Click the "Login" button.
- **Expected Result:** 
  - User is redirected to the inventory page.
  - URL contains `/inventory`.

#### **Test Case 2: Invalid Login**
- **Objective:** Verify that login fails with invalid credentials.
- **Steps:**
  1. Open the SauceDemo website.
  2. Enter invalid credentials:
     - Username: `invalid_user`
     - Password: `wrong_password`.
  3. Click the "Login" button.
- **Expected Result:** 
  - Error message appears: `Epic sadface: Username and password do not match any user in this service.`

---

### **2. test_inventory.py**
#### **Test Case 1: Inventory Display**
- **Objective:** Verify that inventory items are displayed on the page.
- **Steps:**
  1. Log in as a valid user.
  2. Verify the presence of elements with the class `inventory_item`.
- **Expected Result:** At least one inventory item is displayed.

#### **Test Case 2: Inventory Sorting**
- **Objective:** Validate sorting functionality (Low to High).
- **Steps:**
  1. Log in as a valid user.
  2. Select the "Low to High" option in the sort dropdown.
  3. Verify that item prices are sorted in ascending order.
- **Expected Result:** Item prices are displayed in ascending order.

---

### **3. test_cart.py**
#### **Test Case 1: Add Item to Cart**
- **Objective:** Verify that items can be added to the cart.
- **Steps:**
  1. Log in as a valid user.
  2. Click on the "Add to Cart" button for a specific item.
  3. Go to the cart page.
  4. Verify that the item appears in the cart.
- **Expected Result:** Item is displayed in the cart.

---

### **4. test_checkout.py**
#### **Test Case 1: Checkout Process**
- **Objective:** Simulate the complete checkout process.
- **Steps:**
  1. Log in as a valid user.
  2. Add an item to the cart.
  3. Proceed to checkout.
  4. Fill in the checkout form with:
     - First Name: `John`
     - Last Name: `Doe`
     - Postal Code: `12345`.
  5. Complete the checkout.
- **Expected Result:** 
  - A success message appears: `Thank you for your order!`.

---

### **5. test_user_account.py**
#### **Test Case 1: Display Username**
- **Objective:** Verify that the correct username is displayed after login.
- **Steps:**
  1. Log in as a valid user.
  2. Check the displayed username.
- **Expected Result:** Username matches the logged-in user.

#### **Test Case 2: Logout Functionality**
- **Objective:** Verify that the user can log out successfully.
- **Steps:**
  1. Log in as a valid user.
  2. Click the logout button.
  3. Verify that the user is redirected to the login page.
- **Expected Result:** User is logged out, and the login page is displayed.

---

### **6. test_responsiveness.py**
#### **Test Case: Website Responsiveness**
- **Objective:** Verify that the website adjusts correctly to different window sizes.
- **Steps:**
  1. Log in as a valid user.
  2. Resize the browser window to small, medium, and large dimensions.
  3. Verify that all elements remain functional and correctly positioned.
- **Expected Result:** Website layout adapts without breaking functionality.

---

### **7. test_page_navigation.py**
#### **Test Case: Page Navigation**
- **Objective:** Verify navigation between pages.
- **Steps:**
  1. Log in as a valid user.
  2. Navigate between the inventory, cart, and checkout pages.
  3. Verify that the correct page is displayed after each action.
- **Expected Result:** Navigation works without errors, and the correct page is displayed.

---

### **8. test_remove_from_cart.py**
#### **Test Case: Remove Item from Cart**
- **Objective:** Verify that items can be removed from the cart.
- **Steps:**
  1. Add an item to the cart.
  2. Go to the cart page.
  3. Click the "Remove" button for the item.
- **Expected Result:** The item is removed from the cart.

---

### **9. test_filter.py**
#### **Test Case: Apply Filter**
- **Objective:** Verify that filters can be applied to the inventory.
- **Steps:**
  1. Log in as a valid user.
  2. Apply a filter (e.g., "Price: Low to High").
  3. Verify that the displayed items match the filter criteria.
- **Expected Result:** Filter is applied successfully.

---

### **10. test_search.py**
#### **Test Case: Search Functionality**
- **Objective:** Verify that the search bar works correctly.
- **Steps:**
  1. Log in as a valid user.
  2. Enter a product name in the search bar.
  3. Verify that the search results match the query.
- **Expected Result:** Relevant items are displayed based on the search query.

---

### **11. test_bulk_actions.py**
#### **Test Case: Bulk Add/Remove Items**
- **Objective:** Verify that bulk actions work.
- **Steps:**
  1. Log in as a valid user.
  2. Add multiple items to the cart.
  3. Remove multiple items from the cart.
- **Expected Result:** Bulk actions are performed successfully.

---

### **12. test_api.py**
#### **Test Case: API Verification**
- **Objective:** Verify API requests using Selenium Wire.
- **Steps:**
  1. Intercept API requests during login or inventory loading.
  2. Verify the response status code is 200.
- **Expected Result:** API requests are successful with valid responses.
