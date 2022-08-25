import fiftyone as fo
import fiftyone.zoo as foz
import os
import requests

r = requests.get('http://httpbin.org/ip')
print(r.text)
os.environ["http_proxy"] = "http://220.191.0.203:1231"
os.environ["https_proxy"] = "http://220.191.0.203:1231"
dataset = foz.load_zoo_dataset("quickstart")

session = fo.launch_app(dataset)
 
session.wait()


