import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class XSSPageTest(unittest.TestCase):

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
        xss_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'XSS')]"))
        )
        xss_button.click()

        xss_title = WebDriverWait(self.browser, 10).until(
            EC.title_contains("XSS")
        )
        self.assertTrue(WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//title[contains(text(), 'XSS')]"))
        ).is_displayed())

    def test_step_9_to_11(self):
        dashboard_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Dashboard')]"))
        )
        sign_out_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign out')]"))
        )

        self.assertTrue(dashboard_button.is_displayed())
        self.assertTrue(sign_out_button.is_displayed())

        thing_input = self.browser.find_element(By.NAME, "thing")
        submit_button = self.browser.find_element(By.NAME, "submit")

        self.assertTrue(thing_input.is_displayed())
        self.assertTrue(submit_button.is_displayed())

        # Try to write "hacked by ihsanfati" in "thing" input
        thing_input.send_keys("hacked by ihsanfati")
        submit_button.click()

        # Verify that "Your thing is hacked by ihsanfati" is visible successfully
        result_message = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Your thing is hacked by ihsanfati')]"))
        )
        self.assertTrue(result_message.is_displayed())

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
