from reqmethod.WebRequest import Webrequests

url = "http://v.juhe.cn/laohuangli/d"
para = {"key":"eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee","date":"2017-3-22"}
headers ={}

q = Webrequests()

q.get(url,para,headers)
q.post(url,para,headers)
q.post_json(url,para,headers)