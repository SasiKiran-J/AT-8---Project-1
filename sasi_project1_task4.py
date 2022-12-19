from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import Keys
import time

class Sasi_project4():

    def login(self):

        driver = webdriver.Firefox()
        url1 = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url1)
        driver.maximize_window()
        time.sleep(3)
        username = driver.find_element(By.XPATH, "//input[@name='username']")
        username.send_keys("Admin")
        time.sleep(3)
        password = driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys("admin123")
        time.sleep(3)
        login = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        pim = driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,
                            "//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']").send_keys(
            "Sasi")
        Selecting_employee_name = "//span[text()='Sasi Kiran J']"
        wait = WebDriverWait(driver, 5)
        wait.until(expected_conditions.element_to_be_clickable(By.XPATH, Selecting_employee_name))
        driver.find_element(By.XPATH, "//span[text()='Sasi Kiran J']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        nickname = driver.find_element(By.XPATH, "//div/label[text()='Nickname']/following::div[1]/input")
        nickname.send_keys("Goodman")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)


obj=Sasi_project4()
obj.login()

