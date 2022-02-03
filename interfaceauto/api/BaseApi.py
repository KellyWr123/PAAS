import requests
from api import toolpaasmd5


class BaseApi:
    def send(self,**data):
        return requests.request(**data).json()

    def interface_get(self,url,payload):
        timestamp, sign = toolpaasmd5.Testmd5Tool.jointAllDic(self, payload)
        payload['timestamp'] = timestamp
        payload['sign'] = sign
        payload['accessKeyId'] = '329c58bb72627411'
        data={
            'method':'get',
            'url':url,
            'params':payload,
        }
        return self.send(**data)

    def interface_post(self,url,payload):
        timestamp, sign = toolpaasmd5.Testmd5Tool.jointAllDic(self, payload)
        payload['timestamp'] = timestamp
        payload['sign'] = sign
        payload['accessKeyId'] = '329c58bb72627411'
        data={
            'method':'post',
            'url':url,
            'json':payload,
        }
        return self.send(**data)