from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import productPageData


class ProductPageHelper():
    def fileReader(self,fileName):
        nameFile = open(fileName)
        textFromFile = nameFile.read()
        return textFromFile



productPageHelper = ProductPageHelper()

class ProductPage():
    def getMPN_FromProductPage(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, './/a[@class="btn btn-gepard-wide btn-default pull-right"]')))
        return driver.find_element_by_xpath(productPageData.mpnPath).text



    def getProductSKU_FromFile(self):
        return productPageHelper.fileReader("skuId.txt")




    def getProductMPN_FromFile(self):
        return productPageHelper.fileReader("mpn.txt")




    def getProductBrandFromPage(self, driver):
        return driver.find_element_by_xpath(productPageData.brandPath).text




    def getProductTypeFromPage(self, driver):
        return driver.find_element_by_xpath(productPageData.typePath).text




    def getProductCategoryFromPage(self, driver):
        return driver.find_element_by_xpath(productPageData.categoryPath).text




    def getProductTitleFromFile(self):
        return productPageHelper.fileReader("productName.txt")




    def getProductSKU(self):
        sku = ProductPage.getProductSKU_FromFile(self)
        return productPageData.productPageURL + sku




    def getMPN_FromVendors(self, driver):
        all_MPNs = driver.find_elements_by_xpath(productPageData.MPNsFromVendor)
        all_MPNs_Text = []
        for i in all_MPNs:
            textMPN = i.text
            all_MPNs_Text.append(textMPN)
        return all_MPNs_Text




    def getProductName_FromVendors(self, driver):
        all_Prod_Names = driver.find_elements_by_xpath(productPageData.productNamesFromVendor)
        all_Prod_Names_Text = []
        for i in all_Prod_Names:
            textProdName = i.text
            all_Prod_Names_Text.append(textProdName)
        return all_Prod_Names_Text








