import unittest
import createProductData
from selenium import webdriver
from createProductPage import CreateProductPage
from productPage import ProductPage
import productManagementData
from productManagementPage import ProductManagement
from dbWorker import DB_Worker




createProductPage = CreateProductPage()
productPage = ProductPage()
prodManagementPage = ProductManagement()
dbWorker = DB_Worker()


class CreateAndDeleteProductBase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(createProductData.createProductURL)


    def tearDown(self):
        self.driver.close()




class CreateAndDeleteProductTest(CreateAndDeleteProductBase):

    def test_Create_Product(self):
        driver = self.driver


        createProductPage.login(driver)

        createProductPage.fill_SKU_Id_Field(driver)

        createProductPage.fill_MPN(driver)

        createProductPage.selectProductBrand(driver, "Lenovo")

        createProductPage.selectProductGoodType(driver)

        createProductPage.fillProductTitle(driver)

        createProductPage.selectProductCategory(driver, "notebooks")

        createProductPage.clickOnSwitchArrow(driver)

        createProductPage.fillStockField(driver, 100)

        createProductPage.fillCost(driver, 100)

        createProductPage.selectWarehouseNum1Roberto(driver)

        createProductPage.clickOnActiveCheckBox(driver)

        createProductPage.fillRRPExcludingTax(driver, 100)

        createProductPage.clickOnCreateButton(driver)

        self.assertEqual(createProductPage.getNotificationAfterCreateProduct(driver), "Product successfully added")




    def test_Created_Product_Data_On_Page_With_DB(self):
        driver = self.driver

        driver.get(productPage.getProductSKU())

        createProductPage.login(driver)

        self.assertEqual(productPage.getMPN_FromProductPage(driver), productPage.getProductMPN_FromFile())
        self.assertEqual(productPage.getProductBrandFromPage(driver), "Lenovo")
        self.assertEqual(productPage.getProductTypeFromPage(driver), "Good")
        self.assertEqual(productPage.getProductCategoryFromPage(driver), "notebooks")
        self.assertIn(productPage.getProductMPN_FromFile(), productPage.getMPN_FromVendors(driver))
        self.assertIn(productPage.getProductTitleFromFile(), productPage.getProductName_FromVendors(driver))

        self.assertIn( dbWorker.searchProductTitleInDB_ByMPN(productPage.getProductMPN_FromFile()),
                         productPage.getProductName_FromVendors(driver))

        self.assertEqual(productPage.getProductSKU_FromFile(),
                         dbWorker.searchProductSKU_In_DB_ByMPN(productPage.getProductMPN_FromFile()))

        self.assertEqual(productPage.getProductBrandFromPage(driver),
                         dbWorker.searchProductBrandInDB_ByMPN(productPage.getProductMPN_FromFile()))

        self.assertEqual(productPage.getProductTypeFromPage(driver),
                         dbWorker.searchProductTypeInDB_ByMPN(productPage.getProductMPN_FromFile()))

        self.assertEqual(productPage.getProductCategoryFromPage(driver),
                         dbWorker.searchProductCategoryInDB_ByMPN(productPage.getProductMPN_FromFile()))




    def test_Delete_Created_Product(self):
        driver = self.driver

        driver.get(productManagementData.prodManagementURL)

        createProductPage.login(driver)

        prodManagementPage.searchCreatedProduct(driver)

        prodManagementPage.deleteCreatedProduct(driver)

        self.assertEqual(prodManagementPage.getNotificationAfterDeleteProduct(driver), "Product deleted successfully")

        self.assertEqual(prodManagementPage.checkProdIsAbsentInProductGrid(driver), "No results found.")

        self.assertEqual(dbWorker.searchDeletedProduct(productPage.getProductMPN_FromFile()), 0)



if __name__ == '__main__':
    unittest.main()
