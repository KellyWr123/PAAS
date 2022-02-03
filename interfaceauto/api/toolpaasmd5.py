import hashlib
import time

class Testmd5Tool:

    def jointAllDic(self,args):
        timestamp = str(int(time.time() * 1000))#转化时间格式
        dic={'accessKeyId':'329c58bb72627411','timestamp':timestamp}
        dictAllContent={**dic,**args}#拼接字符串
        s=''
        for i in sorted(dictAllContent.keys()):#按key值排序
            s=s+i+'='+dictAllContent[i]+'&'
        s=s+'7c5cbe8363244fc047539c27cf2c02011'#获得最终字符串

        content=bytes(s,encoding='utf-8')#转为二进制
        sign=hashlib.md5(content).hexdigest()#MD5加密串

        return timestamp,sign