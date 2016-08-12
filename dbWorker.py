from elasticsearch import Elasticsearch

class DB_Helper():
    def elasticIndex(self, requiredBody):
        es = Elasticsearch(hosts='.com:9200')
        productName = es.search(index='dev_erp_product_delete_fifo', body=requiredBody)
        return productName




dbHelper = DB_Helper()


class DB_Worker():

    def searchProductTitleInDB_ByMPN(self, requiredMPN):
        body = {"_source": ["content_providers.erp.multilingual.1.title"], "query": {"match": {"mpn": requiredMPN}}}
        fullBody = dbHelper.elasticIndex(body)
        return fullBody['hits']['hits'][0]['_source']['content_providers']['erp']['multilingual']['1']['title']




    def searchProductSKU_In_DB_ByMPN(self, requiredMPN):
        body = {"_source": ["*.sku"], "query": {"match": {"mpn": requiredMPN}}}
        fullBody = dbHelper.elasticIndex(body)
        return fullBody['hits']['hits'][0]['_source']['vendors']['distriread']['sku']




    def searchProductBrandInDB_ByMPN(self, requiredMPN):
        body = {"_source": ["brand.brand_name"],"query": {"match": {"mpn": requiredMPN}}}
        fullBody = dbHelper.elasticIndex(body)
        return fullBody['hits']['hits'][0]['_source']['brand']['brand_name']




    def searchProductTypeInDB_ByMPN(self, requiredMPN):
        body = {"_source": ["type"], "query": {"match": {"mpn": requiredMPN}}}
        fullBody = dbHelper.elasticIndex(body)
        type = fullBody['hits']['hits'][0]['_source']['type']
        type = int(type)
        textType = None
        if type == 1:
            textType = "Good"
        elif type == 2:
            textType = "Service"
        elif type == 3:
            textType = "Food"
        return textType




    def searchProductCategoryInDB_ByMPN(self, requiredMPN):
        body = {"_source": ["multilingual.1.category_name"], "query": {"match": {"mpn": requiredMPN}}}
        fullBody = dbHelper.elasticIndex(body)
        return fullBody['hits']['hits'][0]['_source']['multilingual']['1']['category_name']




    def searchDeletedProduct(self, requiredMPN):
        body = {"query": {"term": {"mpn": {"value": requiredMPN}}}}
        fullBody = dbHelper.elasticIndex(body)
        return fullBody['hits']['total']
