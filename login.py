'''
Author: Jiahoo
Date: 2021-05-21 18:22:13
LastEditTime: 2021-05-22 18:21:14
LastEditors: Do not edit
Description: 
'''
import requests
import re
import json
import time

from requests.api import get
def main():
    charge_url = "http://192.168.111.171/shop/wifi/charge?name=156100XXXXX"
    charge_headers = {
        "Host": "192.168.111.171",
        "Connection": "Keep-Alive",
        "Cache-Control": "max-age=0",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
        "Cookie": "PHPSESSID=qcefn7dre6u6e8mv96se2l3vp3"
    }

    charge_response = response = requests.get(url = charge_url, headers =charge_headers)
    text = charge_response.text
    res_hash = r'<input.*_hash_.*?/>'
    all_str = re.findall(pattern = res_hash, string = text)
    res_value = r'value=".*?"'
    value = re.findall(pattern = res_value, string = all_str[0])[0]
    # print(value)
    value =  value.replace(r'value="',"").replace(r'"','')
    # print(value)

    headers = {
        "Host": "192.168.111.171",
        "Connection": "keep-alive",
        "Content-Length": "100",
        "Cache-Control": "max-age=0",
        "Origin": "http://192.168.111.171",
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": "http://192.168.111.171/shop/wifi/charge?name=156100XXXXX",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
        "Cookie": "PHPSESSID=qcefn7dre6u6e8mv96se2l3vp3"
    }
    # body = {
    #     "showtip": "0",
    #     "service_plan": "1652",
    #     "app_logout": "0",
    #     "phone": "156100XXXXX",
    #     "__hash__": value
    # }
    url = "http://192.168.111.171/shop/wifi/showDetail"
    body ="showtip=0&service_plan=1652&app_logout=0&phone=156100XXXXX&__hash__={}".format(value)
    # print(body)
    # print(json.dumps(body))
    response = requests.post(url = url, headers = headers, data = body)
    hash_all = re.findall(r'<input type="hidden" name="__hash__" value=".*?/>', response.text)
    value = [re.findall(pattern = res_value, string = s)[0].replace(r'value="',"").replace(r'"','')  for s in hash_all]
    # print(value)
    url = "http://192.168.111.171/shop/wifi/do_charge"
    headers = {
        "Host": "192.168.111.171",
        "Connection": "keep-alive",
        "Content-Length": "142",
        "Cache-Control": "max-age=0",
        "Origin": "http://192.168.111.171",
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": "http://192.168.111.171/shop/wifi/showDetail",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
        "Cookie": "PHPSESSID=qcefn7dre6u6e8mv96se2l3vp3"
    }
    body = "showtip=0&service_plan=1652&app_logout=0&phone=156100XXXXX&__hash__={}&__hash__={}".format(value[0],value[1])
    # body ={
    #     "showtip" : "0",
    #     "service_plan": "1652",
    #     "app_logout": "0",
    #     "phone": "156100XXXXX",
    #     "__hash__": value[0],
    #     "__hash__": value[1]
    # }
    response = requests.post(url = url, headers = headers, data = body)

    url = "http://192.168.111.171/shop/shop/js/icheck/js/custom.min.js"
    headers = {
        "Host": "192.168.111.171",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "DNT": "1",
        "Accept": r'*/*',
        "Referer": "http://192.168.111.171/shop/wifi/do_charge",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
        "Cookie": "PHPSESSID=qcefn7dre6u6e8mv96se2l3vp3"
    }
    r = requests.get(url = url, headers = headers)

    timee = int(round(time.time()*1000))
    url = "http://as.gwifi.com.cn/gportal/web/sendPassby?_={}".format(timee)
    headers = {
        "Host": "as.gwifi.com.cn",
        "Connection": "Keep-Alive",
        "Accept": r'*/*',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "DNT": "1",
        "Origin": "http://192.168.111.171",
        "Referer": "http://192.168.111.171/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8"
    }
    r = requests.get(url = url, headers = headers)
    print("Get : " + str(r.status_code))
if __name__ == "__main__":
    while True:
        time.sleep(10)
        try:
            print("baidu" + str(requests.get("https://baidu.com").status_code))
            assert 200 == requests.get("https://baidu.com").status_code
        except: main()