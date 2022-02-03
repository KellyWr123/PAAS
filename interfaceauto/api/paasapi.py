# -*- coding: UTF-8 -*-
import pytest
from api.BaseApi import BaseApi


class PaasApi(BaseApi):
    testurl=''#sit02url



    #查询产品品类
    def procategory_query(self):
        payload={}
        url = '%s/api/v1/product/category/list' % self.testurl
        r=self.interface_get(url,payload)
        return r

    # 创建产品
    def createproduct_post(self,productName):
        payload={'productName':productName}
        url='%s/api/v1/product/create' % self.testurl
        r=self.interface_post(url,payload)
        return r

    #查询产品列表
    def productlist_query(self):
        payload={
            'currentPage':'1',
            'pageSize':'3',
        }
        url='%s/api/v1/product/list' % self.testurl
        r=self.interface_get(url,payload)
        return r

    # 查询产品
    #@pytest.mark.skip
    def product_query(self,productKey='123456'):
        payload = {
            'productKey': productKey,
        }
        url='%s/api/v1/product/query' % self.testurl
        r=self.interface_get(url,payload)
        return r


    #更新产品
    def productmodify_post(self,productKey='a1hJRin4n3S',productName="洗衣机234",description="test20201222"):
        payload = {
            'productKey':productKey ,
            'productName':productName ,
            'description':description
        }
        url='%s/api/v1/product/modify' % self.testurl

        r=self.interface_post(url,payload)
        return r



    # 删除产品
    @pytest.mark.skip
    def productdelete_post(self,productKey='a1bU2OdH8NU'):
        payload = {
            'productKey': productKey,
        }
        url = '%s/api/v1/product/delete' % self.testurl
        #print(self.interface_post(url,payload))
        r=self.interface_post(url,payload)
        return r


    #创建产品Topic
    @pytest.mark.skip
    def productcreateTopic_post(self):
        payload = {
            'productKey': 'a1UYMzsyWY6',
            'topicShortName': "testtest",
            'operation':"test20201222123455"
        }
        url = '%s/api/v1/topic/create' % self.testurl
        r=self.interface_post(url,payload)
        return r
        #返回报错

    #查询指定产品Topic
    @pytest.mark.skip
    def productqueryTopic_post(self):
        payload = {
            'productKey': 'a1UYMzsyWY6',
        }
        url = '%s/api/v1/topic/query' % self.testurl
        r=self.interface_get(url,payload)
        return r
        #返回报错


    #删除指定产品Topic
    @pytest.mark.skip
    def productdeleteTopic_post(self):
        payload = {
            'topicId': '1000',
        }
        url = '%s/api/v1/topic/delete' % self.testurl
        r=self.interface_post(url,payload)
        return r
        #返回报错

    # 更新指定产品Topic
    @pytest.mark.skip
    def productmodifyTopic_post(self):
        payload = {
            'productKey': 'a1UYMzsyWY6',
            'topicShortName': "testtest",
            'operation': "test20201222123455"
        }
        url = '%s/api/v1/topic/modify' % self.testurl
        r=self.interface_post(url,payload)
        return r

    # 注册设备
    @pytest.mark.skip
    def deviceRegist_post(self,productKey):
        payload = {
            'productKey': productKey,
        }
        url = '%s/api/v1/device/register' % self.testurl
        r=self.interface_post(url,payload)
        return r

    #批量注册设备
    @pytest.mark.skip
    def deviceregistbatch_post(self,productKey):
        payload = {
            'productKey': productKey,
            'count': '1',
        }
        url = '%s/api/v1/device/register/batch' % self.testurl
        r=self.interface_post(url,payload)
        return r

    #批量注册设备状态查询———————接口说明有误
    @pytest.mark.skip
    def deviceRegistBatchStatus_query(self,productKey,applyId):
        payload = {
            'productKey': productKey,
            'applyId': applyId,
        }
        url = '%s/api/v1/device/register/batch/status/query' % self.testurl
        r=self.interface_get(url,payload)
        return r



    #分页查询指定批次的设备信息
    @pytest.mark.skip
    def deviceRegistBatchPage_query(self,applyId):
        payload = {
            'pageSize': '1',
            'applyId': applyId,
            "currentPage":'2'
        }
        url= '%s/api/v1/device/register/batch/page' % self.testurl
        r=self.interface_get(url,payload)
        return r


    #查询指定设备信息
    @pytest.mark.skip
    def device_query(self,productKey,deviceName):
        payload = {
            'productKey': productKey,
            'deviceName': deviceName
        }
        url= '%s/api/v1/device/query' % self.testurl
        r=self.interface_get(url,payload)
        return r


    #删除指定设备
    @pytest.mark.skip
    def deviceDelete_post(self,productKey,deviceName):
        payload = {
            'productKey': productKey,
            'deviceName': deviceName,
        }
        url= '%s/api/v1/device/delete' % self.testurl
        r=self.interface_post(url,payload)
        return r


    #查询设备属性状态信息
    @pytest.mark.skip
    def devicePropertyStatus_get(self,productKey,deviceName):
        payload = {
            'productKey': productKey,
            'deviceName': deviceName,
            'identifiers':'powerStat'
        }
        url= '%s/api/v1/device/property/status' % self.testurl
        r=self.interface_get(url,payload)
        return r


    #发送RRPC指令
    @pytest.mark.skip
    def deviceRrpc_post(self):
        payload = {
            'productKey': 'a1UYMzsyWY6',
            'deviceName': '1050',
            'messageContent':'测试中测试中',

        }
        url= '%s/api/v1/device/rrpc' % self.testurl
        r=self.interface_post(url,payload)
        return r

    # 发送pub指令
    @pytest.mark.skip
    def devicePub_post(self):
        payload = {
            'productKey': 'a1UYMzsyWY6',
            'deviceName': '1050',
            'messageContent': '测试中测试中',
            'topic':'123456'

        }
        url = '%s/api/v1/device/pub' % self.testurl
        r=self.interface_post(url, payload)
        return r

    #设备日志分页列表
    @pytest.mark.skip
    def deviceLogList_get(self):
        payload = {
            'productKey': 'a1UYMzsyWY6',
            'deviceName': '1050',
        }
        url= '%s/api/v1/device/log/list' % self.testurl
        r=self.interface_get(url,payload)
        return r


    #添加云智易产品
    @pytest.mark.skip
    def xlinkProductAdd_post(self):
        payload = {
            'productKey': 'a1UYMzsyWY6',
            'productName': '1050',
            'productSecret':'1234567',
            'description':'testtest'
        }
        url= '%s/api/v1/xlink/product/add' % self.testurl
        r=self.interface_post(url,payload)
        return r

    # 添加云智易设备
    @pytest.mark.skip
    def xlinkDeviceAdd_post(self):
        payload = {
            'productKey': 'a1UYMzsyWY6',
            'deviceName': '1050',
            'deviceSecret': '1234567',
            'iotId': 'testtest'
        }
        url = '%s/api/v1/xlink/device/add' % self.testurl
        r=self.interface_post(url, payload)
        return r

    # 云智易产品是否存在
    @pytest.mark.skip
    def xlinkProductExist_post(self):
        payload = {
            'productId': 'testtest'
        }#productId对应的是productKey
        url = '%s/api/v1/xlink/product/exist' % self.testurl
        r=self.interface_post(url, payload)
        return r

    # 云智易设备是否存在
    @pytest.mark.skip
    def xlinkDeviceExist_post(self):
        payload = {
            'deviceName': 'testtest'
        }
        url = '%s/api/v1/xlink/device/exist' % self.testurl
        r=self.interface_post(url, payload)
        return r

    # 创建OTA
    @pytest.mark.skip
    def otaCreate_post(self):
        payload = {
            'type': '0',
            'name':'热水器',
            'productKey':'123',
            'algorithm':'MD5',
            'signature':'',
            'path':'',
        }
        url = '%s/api/v1/ota/create' % self.testurl
        r=self.interface_post(url, payload)
        return r

    #获得OTA列表
    @pytest.mark.skip
    def test_otaList_get(self):
        payload = {
            'productKey': '0',
        }
        url = '%s/api/v1/ota/list' % self.testurl
        r=self.interface_get(url, payload)
        return r


    #设备OTA升级
    @pytest.mark.skip
    def otaDeviceUpgrade_get(self):
        payload = {
            'firmwareId': '0',
            'deviceNameList':''
        }
        url = '%s/api/v1/ota/device/upgrade' % self.testurl
        r=self.interface_post(url, payload)
        return r



