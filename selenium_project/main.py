from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tests.test_login import test_valid_login
from tests.test_inventory import test_inventory_display, test_sort_inventory
import time

# Путь к chromedriver
CHROME_DRIVER_PATH = r"D:\selenium_project\chromedriver-win64\chromedriver.exe"

# Запуск тестов
if __name__ == "__main__":
    print("=== Запуск тестов ===")
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    try:
        # Открытие сайта
        print("\nОткрываем сайт...")
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        # Тест логина
        print("\n=== Тест логина ===")
        test_valid_login(driver)
        time.sleep(2)

        # Тест инвентаря: проверка отображения товаров
        print("\n=== Тесты инвентаря: отображение товаров ===")
        test_inventory_display(driver)
        time.sleep(2)

        # Тест инвентаря: сортировка товаров
        print("\n=== Тесты инвентаря: сортировка товаров ===")
        test_sort_inventory(driver)
        time.sleep(2)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        print("\nЗакрываем браузер...")
        driver.quit()
        print("Тесты выполнены успешно!")
