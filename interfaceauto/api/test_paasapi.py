import allure
import pytest
import yaml
from api.paasapi import PaasApi

@allure.feature("paas接口")
class TestPaasApi:
    def setup(self):
        self.paasapi=PaasApi()

    @allure.story("查询产品品类")
    def test_procategory_query(self):
        #查询产品品类

        r=self.paasapi.procategory_query()
        print(r)
        assert r['code']==200

    @allure.story("创建产品")
    @pytest.mark.parametrize("productName",yaml.safe_load(open("../data/productName.yaml")))
    def test_createproduct_post(self,productName):
        #创建产品

        r=self.paasapi.createproduct_post(productName)
        print(r)
        assert r['code']==200

    @allure.story("查询产品列表")
    def test_productlist_query(self):
        #查询产品列表

        r=self.paasapi.productlist_query()
        print(r)
        assert r['code']==200

    @allure.story("查询产品")
    @pytest.mark.parametrize("productKey",yaml.safe_load(open("../data/productKey.yaml")))
    def test_product_query(self,productKey):
        #查询产品

        r=self.paasapi.product_query(productKey)
        print(r)
        assert r['code']==200

    @allure.story('更新产品')
    def test_productmodify_post(self,productKey='a1hJRin4n3S',productName="洗衣机234",description="test20201222"):
        #更新产品

        r=self.paasapi.productmodify_post(productKey, productName, description)
        print(r)
        assert r['code']==200

    @allure.story('删除产品')
    def test_productdelete_post(self,productKey='b2hJRin4n3S'):
        #删除产品

        r=self.paasapi.productdelete_post(productKey)
        print(r)
        assert r['code']==200

    @allure.story('创建产品Topic')
    def test_productcreateTopic_post(self):
        #创建产品Topic

        r=self.paasapi.productcreateTopic_post()
        print(r)
        assert r['code']==200

    @allure.story('查询产品Topic')
    def test_productqueryTopic_post(self):
        #查询产品Topic

        r=self.paasapi.productqueryTopic_post()
        print(r)
        assert r['code']==200

    @allure.story('更新产品Topic')
    def test_productmodifyTopic_post(self):
        #更新产品Topic

        r=self.paasapi.productmodifyTopic_post()
        print(r)
        assert r['code']==200

    @allure.story('注册设备')
    #@pytest.mark.parametrize("productKey",yaml.safe_load(open("../data/productKey.yaml")))
    def test_deviceRegist_post(self,productKey='a1wzw7p3MSO'):
        #注册设备

        r=self.paasapi.deviceRegist_post(productKey)
        print(r)
        assert r['code']==200

    @allure.story('批量注册设备')
    def test_deviceregistbatch_post(self,productKey='a1wzw7p3MSO'):
        # 批量注册设备

        r=self.paasapi.deviceregistbatch_post(productKey)
        print(r)
        assert r['code']==200

    @allure.story('批量注册设备状态查询')
    def test_deviceRegistBatchStatus_query(self,productKey='a1wzw7p3MSO',applyId='2780529'):
        #批量注册设备状态查询
        r=self.paasapi.deviceRegistBatchStatus_query(productKey, applyId)
        print(r)
        assert r['code']==200

    @allure.story('分页查询指定批次的设备信息')
    def test_deviceRegistBatchPage_query(self,applyId='2780529'):
        #分页查询指定批次的设备信息
        r=self.paasapi.deviceRegistBatchPage_query(applyId)
        print(r)
        assert r['code']==200

    @allure.story('查询指定设备信息')
    def test_device_query(self,productKey='a1wzw7p3MSO',deviceName='K9PxWPgpWJ1MFG74zYwU'):
        #查询指定设备信息
        r=self.paasapi.device_query(productKey, deviceName)
        print(r)
        assert r['code']==200

    @allure.story('删除指定设备')
    def test_deviceDelete_post(self,productKey='a1UYMzsyWY6',deviceName='1050'):
        #删除指定设备
        r=self.paasapi.deviceDelete_post(productKey, deviceName)
        print(r)
        assert r['code']==200

    @allure.story('查询设备属性状态信息')
    def test_devicePropertyStatus_get(self,productKey='a1wzw7p3MSO',deviceName='a1wzw7p3MSO'):
        #查询设备属性状态信息
        r=self.paasapi.devicePropertyStatus_get(productKey, deviceName)
        print(r)
        assert r['code']==200

    @allure.story('发送RRPC指令')
    def test_deviceRrpc_post(self):
        #发送RRPC指令
        r=self.paasapi.deviceRrpc_post()
        print(r)
        assert r['code']==200

    @allure.story('发送pub指令')
    def test_devicePub_post(self):
        #发送pub指令
        r=self.paasapi.devicePub_post()
        print(r)
        assert r['code']==200

    @allure.story('设备日志分页列表')
    def test_deviceLogList_get(self):
        #设备日志分页列表
        r=self.paasapi.deviceLogList_get()
        print(r)
        assert r['code']==200


    @allure.story('添加云智易产品')
    def test_xlinkProductAdd_post(self):
        #添加云智易产品
        r=self.paasapi.xlinkProductAdd_post()
        print(r)
        assert r['code']==200

    @allure.story('添加云智易设备')
    def test_xlinkDeviceAdd_post(self):
        #添加云智易设备
        r=self.paasapi.xlinkDeviceAdd_post()
        print(r)
        assert r['code']==200

    @allure.story('云智易产品是否存在')
    def test_xlinkProductExist_post(self):
        #云智易产品是否存在
        r=self.paasapi.xlinkProductExist_post()
        print(r)
        assert r['code']==200

    @allure.story('云智易设备是否存在')
    def test_xlinkDeviceExist_post(self):
        #云智易设备是否存在
        r=self.paasapi.xlinkDeviceExist_post()
        print(r)
        assert r['code']==200

    @allure.story('创建OTA')
    def test_otaCreate_post(self):
        #创建OTA
        r=self.paasapi.otaCreate_post()
        print(r)
        assert r['code']==200

    @allure.story('设备OTA升级')
    def test_otaDeviceUpgrade_get(self):
        #设备OTA升级
        r=self.paasapi.otaDeviceUpgrade_get()
        print(r)
        assert r['code']==200

    @allure.story("产品增删改查")
    def test_cq_fuction(self):
        with allure.step("创建产品并查询是否创建成功"):
            productName="洗衣机369"
            r=self.paasapi.createproduct_post(productName)
            productKey=r['data']
            r=self.paasapi.product_query(productKey)
            #创建后查询
            assert r['data']['productName']==productName
        with allure.step("修改产品并查询是否修改成功"):
            description='thisisanewdesc'
            self.paasapi.productmodify_post(productKey,productName,description)
            r = self.paasapi.product_query(productKey)
            #修改后查询
            assert r['data']['description']==description
        with allure.step("删除产品并查询是否已删除成功"):
            self.paasapi.productdelete_post(productKey)
            r=self.paasapi.product_query(productKey)
            #删除成功
            assert r['message']=='产品不存在'







