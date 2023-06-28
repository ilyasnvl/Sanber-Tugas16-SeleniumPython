from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest
import time
import login
from pom.loginElem import loginElm
from pom.employeElem import employee
from pom.data import addEmployee

class TestEmployeModul(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://opensource-demo.orangehrmlive.com/"

    # TC001 - As an admin, i can successfully add new employee with valid data
    def test_a_success_add_new_employee(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(1)

        # Memanggil test case login
        login.test_login(self, driver)

        # Masuk Menu PIM
        driver.find_element(By.XPATH, employee.menuPim).click()
        time.sleep(2)
        driver.find_element(By.XPATH, employee.btnAddEmp).click() #button add
        time.sleep(1)

        # Add Employee
        driver.find_element(By.XPATH, employee.inputAddFirstName).send_keys(addEmployee.addFirstName)
        driver.find_element(By.XPATH, employee.inputAddMiddleName).send_keys(addEmployee.addMiddleName)
        driver.find_element(By.XPATH, employee.inputAddLastName).send_keys(addEmployee.addLastName)
        emp_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, employee.inputEmpId)))
        emp_id.send_keys(Keys.SHIFT, Keys.ARROW_UP, Keys.DELETE)
        emp_id.send_keys(addEmployee.addEmpIdValid)
        time.sleep(2)
        driver.find_element(By.XPATH, employee.btnSaveAdd).click() #button save
        time.sleep(5)

        # Validasi
        resp_add_emp = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, employee.expAddEmp))).text
        self.assertIn("Personal Details", resp_add_emp)
        time.sleep(5)
    
    # TC002 - As an admin, i can cancel add new employee
    def test_b_cancel_add_new_employee(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(1)

        # Memanggil test case login
        login.test_login(self, driver)

        # Masuk Menu PIM
        driver.find_element(By.XPATH, employee.menuPim).click()
        time.sleep(2)
        driver.find_element(By.XPATH, employee.btnAddEmp).click() #button add
        time.sleep(1)

        # Add Employee
        driver.find_element(By.XPATH, employee.inputAddFirstName).send_keys(addEmployee.addFirstName)
        driver.find_element(By.XPATH, employee.inputAddMiddleName).send_keys(addEmployee.addMiddleName)
        driver.find_element(By.XPATH, employee.inputAddLastName).send_keys(addEmployee.addLastName)
        driver.find_element(By.XPATH, employee.btnCancelAdd).click() #button cancel

        #validasi
        resp_cancel_add_emp = driver.current_url
        self.assertIn("web/index.php/pim/viewEmployeeList", resp_cancel_add_emp)        
    
    # TC003 - As an admin, i can't add new employee without input field
    def test_c_add_new_employee_without_input_field(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(1)

        # Memanggil test case login
        login.test_login(self, driver)

        # Masuk Menu PIM
        driver.find_element(By.XPATH, employee.menuPim).click()
        time.sleep(2)
        driver.find_element(By.XPATH, employee.btnAddEmp).click() #button add
        time.sleep(1)

        # Add Employee
        driver.find_element(By.XPATH, employee.btnSaveAdd).click() #button save

        # Validasi
        err_msg_firstname = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, employee.errMsgFirstName))).text
        err_msg_lastname = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, employee.errMsgLastName))).text
        self.assertIn("Required", err_msg_firstname)
        self.assertIn("Required", err_msg_lastname)

    # TC004 - Failed input employe id with more than 10 character
    def test_d_failed_add_new_employee_with_invalid_data(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(1)

        # Memanggil test case login
        login.test_login(self, driver)

        # Masuk Menu PIM
        driver.find_element(By.XPATH, employee.menuPim).click()
        time.sleep(2)
        driver.find_element(By.XPATH, employee.btnAddEmp).click() #button add
        time.sleep(1)

        # Add Employee
        driver.find_element(By.XPATH, employee.inputAddFirstName).send_keys(addEmployee.addFirstName)
        driver.find_element(By.XPATH, employee.inputAddMiddleName).send_keys(addEmployee.addMiddleName)
        driver.find_element(By.XPATH, employee.inputAddLastName).send_keys(addEmployee.addLastName)
        time.sleep(2)
        emp_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, employee.inputEmpId))) 
        emp_id.send_keys(Keys.SHIFT, Keys.ARROW_UP, Keys.DELETE)
        emp_id.send_keys(addEmployee.addEmpId)
        time.sleep(2)
        driver.find_element(By.XPATH, employee.btnSaveAdd).click() #button save
        time.sleep(5)

        # Validasi
        err_msg_empid_exist = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, employee.errMsgEmpId))).text
        self.assertIn("Should not exceed 10 characters", err_msg_empid_exist)
        

    # TC005 - As an admin, i can success edit employee
    def test_e_success_edit_employee(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(1)

        # Memanggil test case login
        login.test_login(self, driver)

        # Masuk Menu PIM
        driver.find_element(By.XPATH, employee.menuPim).click()
        time.sleep(2)
        driver.find_element(By.XPATH, employee.btnEdit).click()
        time.sleep(2)

        # Change Name
        first_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, employee.inputAddFirstName)))
        first_name.send_keys(Keys.SHIFT, Keys.ARROW_UP, Keys.DELETE) # mengahapus text sebelumnya
        first_name.send_keys(addEmployee.editFirstName) # masukkan nama depan yang diinginkan
        time.sleep(1)
        middel_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, employee.inputAddMiddleName)))
        middel_name.send_keys(Keys.SHIFT, Keys.ARROW_UP, Keys.DELETE) # mengahapus text sebelumnya
        middel_name.send_keys(addEmployee.editMiddleName) # masukkan nama tengah yang diinginkan
        time.sleep(1)
        last_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, employee.inputAddLastName)))
        last_name.send_keys(Keys.SHIFT, Keys.ARROW_UP, Keys.DELETE) # mengahapus text sebelumnya
        last_name.send_keys(addEmployee.editLastName) # masukkan nama akhir yang diinginkan
        time.sleep(2)
        driver.find_element(By.XPATH, employee.btnSaveEdit).click()
        time.sleep(3)

        # Validasi
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, employee.toasterSuccess))).is_displayed() # Cek Toaster Successfully Update Muncul

    # TC006 - As an admin, i can successfully delete employee
    def test_f_success_delete_employee(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(1)

        # Memanggil test case login
        login.test_login(self, driver)

        # Masuk Menu PIM
        driver.find_element(By.XPATH, employee.menuPim).click()
        time.sleep(2)
        driver.find_element(By.XPATH, employee.btnDelete).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, employee.modalDelYes))).click()
        time.sleep(2)

        # Validasi
        driver.find_element(By.CSS_SELECTOR, employee.toasterSuccess).is_displayed() # Verify Toaster yang muncul setelah delete
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()