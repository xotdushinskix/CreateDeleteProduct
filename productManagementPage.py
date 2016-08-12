import productManagementData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from productPage import  ProductPage



productPage = ProductPage()

class ProductManagementHelper():
    def clickableWait(self, driver, xPath):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, xPath)))


productManagementHelper = ProductManagementHelper()

class ProductManagement():
    def searchCreatedProduct(self, driver):
        productManagementHelper.clickableWait(driver, productManagementData.searchManagementButton)
        driver.find_element_by_xpath(productManagementData.searchManagementButton).click()
        driver.find_element_by_xpath(productManagementData.mpnSelect2).click()
        driver.find_element_by_xpath(productManagementData.mpnSelect2Input).send_keys(productPage.getProductMPN_FromFile())
        productManagementHelper.clickableWait(driver, productManagementData.searchSuggestionMPN_Select2)
        driver.find_element_by_xpath(productManagementData.searchSuggestionMPN_Select2).click()
        driver.find_element_by_xpath(productManagementData.searchButtonOnSearchGrid).click()




    def deleteCreatedProduct(self, driver):
        productManagementHelper.clickableWait(driver, productManagementData.deleteButton)
        driver.find_element_by_xpath(productManagementData.deleteButton).click()
        driver.find_element_by_xpath(productManagementData.applyDeleteButton).click()




    def getNotificationAfterDeleteProduct(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, productManagementData.deleteNotification),
                                                    "Product deleted successfully"))
        return driver.find_element_by_xpath(productManagementData.deleteNotification).text




    def checkProdIsAbsentInProductGrid(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.invisibility_of_element_located((By.XPATH, productManagementData.deleteNotification)))
        return driver.find_element_by_xpath(productManagementData.gridAfterDelete).text