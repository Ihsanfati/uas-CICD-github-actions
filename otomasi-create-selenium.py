import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebsiteTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.get("http://localhost/ihsanfati-uas-ppl-BadCRUD/login.php")

    def login(self):
        username_input = self.browser.find_element(By.ID, "inputUsername")
        password_input = self.browser.find_element(By.ID, "inputPassword")
        login_button = self.browser.find_element(By.CSS_SELECTOR, "[type='submit']")

        username_input.send_keys("admin")
        password_input.send_keys("nimda666!")
        login_button.click()

        WebDriverWait(self.browser, 10).until(EC.title_contains("Dashboard"))

        dashboard_heading = self.browser.find_element(By.XPATH, "//h2[contains(text(), 'Halo, admin')]")
        self.assertTrue(dashboard_heading.is_displayed())

    def test_step_1_to_3(self):
        self.login()

    def test_step_4_to_6(self):
        create_contact_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Create Contact')]"))
        )
        create_contact_button.click()

        create_contact_title = WebDriverWait(self.browser, 10).until(
            EC.title_contains("Add new contact")
        )
        self.assertTrue(create_contact_title)

    def test_step_7_to_11(self):
        placeholders = ["Type name", "Email", "Phone number", "Title"]
        for placeholder in placeholders:
            input_field = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"//input[@placeholder='{placeholder}']"))
            )
            self.assertTrue(input_field.is_displayed())

        name_input = self.browser.find_element(By.XPATH, "//input[@placeholder='Type name']")
        email_input = self.browser.find_element(By.XPATH, "//input[@placeholder='Email']")
        phone_input = self.browser.find_element(By.XPATH, "//input[@placeholder='Phone number']")
        title_input = self.browser.find_element(By.XPATH, "//input[@placeholder='Title']")

        name_input.send_keys("Fati")
        email_input.send_keys("ifat.ichan@gmail.com")
        phone_input.send_keys("081229856509")
        title_input.send_keys("Supervisor")

        save_button = self.browser.find_element(By.XPATH, "//input[@type='submit' and @value='Save']")
        save_button.click()

        WebDriverWait(self.browser, 10).until(EC.title_contains("Dashboard"))

        index_title = self.browser.find_element(By.XPATH, "//title[contains(text(), 'Dashboard')]")
        self.assertTrue(index_title.is_displayed())

        fati_in_table = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), 'Fati')]"))
        )
        self.assertTrue(fati_in_table.is_displayed())

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')