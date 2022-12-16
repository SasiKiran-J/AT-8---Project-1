from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import Keys
import time

class Sasi_project1():

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
        add = driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
        time.sleep(3)
        firstname = driver.find_element(By.XPATH, "//input[@name='firstName']")
        firstname.send_keys("Sasi")
        time.sleep(3)
        middlename = driver.find_element(By.XPATH, "//input[@name='middleName']")
        middlename.send_keys("Kiran")
        time.sleep(3)
        lastname = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastname.send_keys("Jaganathan")
        time.sleep(3)
        details = driver.find_element(By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
        time.sleep(3)
        user_xpath = "//label[text()='Username']/following::div[1]/input"
        user_name = driver.find_element(By.XPATH, user_xpath)
        user_name.send_keys("example_sasi_12")
        time.sleep(3)
        first_xpath = "//div/label[text()='Password']/following::div[1]/input"
        first_password = driver.find_element(By.XPATH, first_xpath)
        first_password.send_keys("Sasikiran@12")
        time.sleep(3)
        confirm_xpath = "//div/label[text()='Confirm Password']/following::div[1]/input"
        confirm_password = driver.find_element(By.XPATH, confirm_xpath)
        confirm_password.send_keys("Sasikiran@12")
        time.sleep(3)
        save = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        #pim = driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        #time.sleep(3)
        #employee_name = driver.find_element(By.XPATH, "//input[@name='']")
        #username.send_keys("Admin")


obj=Sasi_project1()
obj.login()

