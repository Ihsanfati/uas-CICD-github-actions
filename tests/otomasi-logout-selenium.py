import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WebsiteTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        server = 'http://localhost:4444'
        self.browser = webdriver.Remote(command_executor=server, options=options)

    def test_1_login(self):
        try:
            self.url = os.environ['URL']
        except:
            self.url = "http://localhost"
        self.browser.get(self.url +"/logout.php")

        username_input = self.browser.find_element(By.ID, "inputUsername")
        password_input = self.browser.find_element(By.ID, "inputPassword")
        login_button = self.browser.find_element(By.CSS_SELECTOR, "[type='submit']")

        username_input.send_keys("admin")
        password_input.send_keys("nimda666!")
        login_button.click()

        time.sleep(2)  # Allow time for redirection

        dashboard_heading = self.browser.find_element(By.XPATH, "//h2[contains(text(), 'Halo, admin')]")
        self.assertTrue(dashboard_heading.is_displayed())

    def test_2_verify_signout_button(self):

        signout_button = self.browser.find_element(By.XPATH, "//a[contains(text(), 'Sign out')]")
        self.assertTrue(signout_button.is_displayed())

    def test_3_signout(self):
    
        signout_button = self.browser.find_element(By.XPATH, "//a[contains(text(), 'Sign out')]")
        signout_button.click()

        time.sleep(2)  # Allow time for redirection

        login_heading = self.browser.find_element(By.XPATH, "//h1[contains(text(), 'Please sign in')]")
        self.assertTrue(login_heading.is_displayed())

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        #cls.browser.quit()

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')