<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selenium Testing Project for SauceDemo</title>
</head>
<body>
    <h1 style="text-align: center;">Selenium Testing Project for SauceDemo</h1>

    <h2>📖 About the Project</h2>
    <p>
        This repository contains automated tests for the SauceDemo website. The tests are written in 
        <strong>Python</strong> using the <strong>Selenium</strong> framework and are designed to cover various functionalities of the website, 
        including login, cart operations, inventory management, checkout, and more.
    </p>

    <h2>🧪 Tests Included</h2>
    <ul>
        <li><strong>test_login.py</strong>: Verifies the login functionality using valid credentials.</li>
        <li><strong>test_inventory.py</strong>:
            <ul>
                <li>Ensures that inventory items are displayed.</li>
                <li>Checks if the inventory sorting works as expected (e.g., low-to-high price sorting).</li>
            </ul>
        </li>
        <li><strong>test_cart.py</strong>:
            <ul>
                <li>Validates adding items to the cart.</li>
                <li>Verifies item details in the cart.</li>
            </ul>
        </li>
        <li><strong>test_checkout.py</strong>: Simulates the complete checkout process, from adding an item to the cart to completing the order.</li>
        <li><strong>test_user_account.py</strong>:
            <ul>
                <li>Verifies user account details (e.g., username display).</li>
                <li>Tests the logout functionality.</li>
            </ul>
        </li>
        <li><strong>test_responsiveness.py</strong>: Validates the responsiveness of the website by checking elements on different window sizes.</li>
        <li><strong>test_page_navigation.py</strong>: Tests navigation between different pages of the website (e.g., inventory, cart, checkout).</li>
        <li><strong>test_remove_from_cart.py</strong>: Verifies the functionality of removing items from the cart.</li>
        <li><strong>test_error_handling.py</strong>: Ensures that proper error messages are displayed for invalid actions (e.g., logging in with incorrect credentials).</li>
        <li><strong>test_api.py</strong>: Simulates API interactions (e.g., verifying network requests) using Selenium Wire.</li>
        <li><strong>test_bulk_actions.py</strong>: Tests bulk actions, such as adding or removing multiple items from the cart.</li>
        <li><strong>test_filter.py</strong>: Verifies the functionality of applying filters to the inventory.</li>
    </ul>

    <h2>🛠 Technologies Used</h2>
    <ul>
        <li><strong>Python</strong>: Programming language.</li>
        <li><strong>Selenium</strong>: For browser automation.</li>
        <li><strong>Selenium Wire</strong>: For intercepting network requests.</li>
        <li><strong>Pytest</strong>: For test execution.</li>
        <li><strong>ChromeDriver</strong>: To automate Chrome browser.</li>
        <li><strong>Virtual Environment</strong>: To isolate dependencies.</li>
    </ul>

    <h2>🚀 How to Run the Tests</h2>
    <h3>Prerequisites</h3>
    <ul>
        <li>Install Python (version 3.8 or higher).</li>
        <li>Install Chrome browser.</li>
        <li>Download and set up ChromeDriver.</li>
    </ul>
</body>
</html>
