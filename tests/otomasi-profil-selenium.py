import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

class WebsiteTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        server = 'http://localhost:4444'
        self.browser = webdriver.Remote(command_executor=server, options=options)

    def login(self, username, password):
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
        
    def test_3_profile_button_visible(self):
        # Verify "Profile" button visibility
        profile_button = self.browser.find_element(By.XPATH, "//a[contains(text(), 'Profile')]")
        self.assertTrue(profile_button.is_displayed())

    def test_4_profile_redirect(self):
        # Click "Profile" button and verify redirection to profil.php
        profile_button = self.browser.find_element(By.XPATH, "//a[contains(text(), 'Profile')]")
        profile_button.click()
        time.sleep(2)  # Allow time for redirection

        # Verify Profile page visibility
        profile_heading = self.browser.find_element(By.XPATH, "//h2[contains(text(), 'Profil')]")
        self.assertTrue(profile_heading.is_displayed())

    def test_5_dashboard_signout_visible(self):
        # Verify "Dashboard" and "Sign out" buttons visibility
        dashboard_button = self.browser.find_element(By.XPATH, "//a[contains(text(), 'Dashboard')]")
        signout_button = self.browser.find_element(By.XPATH, "//a[contains(text(), 'Sign out')]")
        self.assertTrue(dashboard_button.is_displayed())
        self.assertTrue(signout_button.is_displayed())

    def test_6_username_password_form_visible(self):
        # Verify Username and Password form visibility
        username_input = self.browser.find_element(By.ID, "username")
        password_input = self.browser.find_element(By.ID, "address")
        self.assertTrue(username_input.is_displayed())
        self.assertTrue(password_input.is_displayed())

    def test_7_formfile_and_button_ganti_visible(self):
        # Verify formFile and "Ganti" button visibility
        formfile_input = self.browser.find_element(By.ID, "formFile")
        ganti_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Ganti')]")

        self.assertTrue(formfile_input.is_displayed())
        self.assertTrue(ganti_button.is_displayed())

    def test_8_upload_invalid_image(self):
        # Upload invalid image (tom.png) and verify error message
        formfile_input = self.browser.find_element(By.ID, "formFile")
        formfile_input.send_keys("tom.png")

        ganti_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Ganti')]")
        ganti_button.click()

        error_message = self.browser.find_element(By.XPATH, "//div[contains(text(), 'Ekstensi tidak diijinkan. Hanya menerima file JPG/JPEG')]")
        self.assertTrue(error_message.is_displayed())

    def test_9_upload_valid_image(self):
        # Upload valid image (tom.jpg) and verify file moved to image directory with new name (profile.jpg)
        formfile_input = self.browser.find_element(By.ID, "formFile")
        formfile_input.send_keys("tom.jpg")

        ganti_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Ganti')]")
        ganti_button.click()

        time.sleep(2)  # Allow time for the file to be moved

        # Verify the file has moved to image directory with new name (profile.jpg)
        profile_image_path = "image/profile.jpg"
        self.assertTrue(os.path.exists(profile_image_path))

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
