import random

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import createProductData
from randomHelper import RandomHelper


randomHelper = RandomHelper()


class CreateProductPageHelper():
    def selectFunction(self, driver, selectPath, visibleText):
        select = Select(driver.find_element_by_xpath(selectPath))
        select.select_by_visible_text(visibleText)




    def select2function(self, driver, select2Path, inputField, value,suggestion):
        driver.find_element_by_xpath(select2Path).click()
        driver.find_element_by_xpath(inputField).send_keys(value)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, suggestion), value))
        driver.find_element_by_xpath(suggestion).click()




    def fileWriter(self, driver, fileNameTxt, info):
        with open(fileNameTxt, "w") as myfile:
            myfile.write(info)
        myfile.close()


createProductHelper = CreateProductPageHelper()




class CreateProductPage():

    def login(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, createProductData.loginButton)))
        driver.find_element_by_xpath(createProductData.emailField).send_keys(createProductData.email)
        driver.find_element_by_xpath(createProductData.passwordField).send_keys(createProductData.password)
        driver.find_element_by_xpath(createProductData.loginButton).click()




    def fill_SKU_Id_Field(self, driver):
        intPiece = randomHelper.random_int_generator()
        intPiece = intPiece[5:]
        stringPiece = randomHelper.random_string_generator()
        stringPiece = stringPiece[5:]
        skuID = intPiece + stringPiece
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, createProductData.createButton)))
        driver.find_element_by_xpath(createProductData.skuIdField).send_keys(skuID)
        createProductHelper.fileWriter(driver, "skuId.txt", skuID)




    def fill_MPN(self, driver):
        intPiece = randomHelper.random_int_generator()
        intPiece = intPiece[5:]
        stringPiece = randomHelper.random_string_generator()
        stringPiece = stringPiece[5:]
        MPN = intPiece + "-" + stringPiece
        driver.find_element_by_xpath(createProductData.mpnField).send_keys(MPN)
        createProductHelper.fileWriter(driver, "mpn.txt", MPN)




    def selectProductBrand(self, driver, requiredValue):
        createProductHelper.select2function(driver, createProductData.brandSelect2, createProductData.inputFieldBrand,
                                            requiredValue, createProductData.brandSuggestion)




    def selectProductGoodType(self, driver):
         createProductHelper.selectFunction(driver, createProductData.typeSelect, "Good")




    def fillProductTitle(self, driver):
        productTitleHelp = randomHelper.random_string_generator()
        productTitleHelp = productTitleHelp[5:]
        productTitle = "Test_product_" + productTitleHelp
        createProductHelper.fileWriter(driver, "productName.txt", productTitle)
        driver.find_element_by_xpath(createProductData.productTitleField).send_keys(productTitle)




    def selectProductCategory(self, driver, requiredValue):
        createProductHelper.select2function(driver, createProductData.productCategory,
                                            createProductData.prodCategoryInputField, requiredValue,
                                            createProductData.suggestionAfterSearch)




    def clickOnSwitchArrow(self, driver):
        driver.find_element_by_xpath(createProductData.vendorSwitchArrow).click()




    def fillCost(self, driver, value):
        driver.find_element_by_xpath(createProductData.costField).send_keys(value)




    def fillRRPExcludingTax(self, driver, exclTaxValue):
        driver.find_element_by_xpath(createProductData.rrpExcludingTaxField).send_keys(exclTaxValue)




    def fillStockField(self, driver, value):
        driver.find_element_by_xpath(createProductData.stockField).send_keys(value)




    def selectWarehouseNum1Roberto(self, driver):
        createProductHelper.selectFunction(driver, createProductData.warehouseSelect,
                                           createProductData.warehouseNameHash)




    def clickOnActiveCheckBox(self, driver):
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(createProductData.activeCheckBox).click()




    def clickOnCreateButton(self, driver):
        driver.find_element_by_xpath(createProductData.createButton).click()




    def getNotificationAfterCreateProduct(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, createProductData.notificationAfterCreateProduct),
                                                    "Product successfully added"))
        return driver.find_element_by_xpath(createProductData.notificationAfterCreateProduct).text
