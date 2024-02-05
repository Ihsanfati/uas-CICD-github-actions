import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class EditButtonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.get("http://localhost/ihsanfati-uas-ppl-BadCRUD/login.php")

    def login(self):
        time.sleep(5)  # Tunggu lebih lama sebelum mencari elemen
        username_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#inputUsername"))
        )
        password_input = self.browser.find_element(By.ID, "inputPassword")
        login_button = self.browser.find_element(By.CSS_SELECTOR, "[type='submit']")

        username_input.send_keys("admin")
        password_input.send_keys("nimda666!")
        login_button.click()

        time.sleep(2)  # Allow time for redirection

        # Check if redirected to the dashboard
        dashboard_heading = self.browser.find_element(By.XPATH, "//h2[contains(text(), 'Halo, admin')]")
        self.assertTrue(dashboard_heading.is_displayed(), "Failed to log in. Dashboard heading not found.")

    def test_edit_button_visibility(self):
        self.login()

        # Continue with your test logic for edit button visibility

    def test_edit_button_clickable(self):
        self.login()

        # Tunggu hingga halaman index.php selesai dimuat
        WebDriverWait(self.browser, 10).until(EC.title_contains("Dashboard"))

        # Ambil semua tombol "Edit"
        edit_buttons = self.browser.find_elements(By.CSS_SELECTOR, ".btn-outline-success")

        # Uji setiap tombol "Edit"
        for edit_button in edit_buttons:
            self.assertTrue(edit_button.is_displayed(), "Edit button is not visible")
            edit_button.click()

            # Tunggu hingga halaman update.php selesai dimuat
            WebDriverWait(self.browser, 10).until(EC.title_contains("Update"))

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')