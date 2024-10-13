import os
import pathlib
import unittest
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

class WebpageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the Chrome driver
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.get(file_uri(r"C:\Users\LiVINGCODES\Desktop\MIOSC\selenium\counter.html"))  # Replace with the correct path to your HTML file

    @classmethod
    def tearDownClass(cls):
        # Close the browser after tests
        cls.driver.quit()

    def test_title(self):
        """Test if the page title is correct."""
        self.assertEqual(self.driver.title, "Count")

    def test_increase(self):
        """Test the increase functionality."""
        # Click the increase button
        increase_button = self.driver.find_element(By.ID, "increase")
        increase_button.click()
        
        # Verify the counter has increased
        counter_value = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(counter_value, "1")  # Expecting counter to be 1 after one click

    def test_decrease(self):
        """Test the decrease functionality."""
        # Click the decrease button
        decrease_button = self.driver.find_element(By.ID, "decrease")
        decrease_button.click()
        
        # Verify the counter has decreased
        counter_value = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(counter_value, "0")  # Expecting counter to be 0 after one increase and one decrease

    def test_multiple_increase(self):
        """Test multiple increase functionality."""
        increase_button = self.driver.find_element(By.ID, "increase")
        
        # Click the increase button multiple times
        for _ in range(5):
            increase_button.click()
            time.sleep(0.1)  # Optional: Small delay to ensure updates are reflected

        # Verify the counter has increased correctly
        counter_value = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(counter_value, "5")  # Expecting counter to be 5 after five clicks

if __name__ == "__main__":
    unittest.main()
