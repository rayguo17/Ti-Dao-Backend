import requests
import json
import hashlib
import time

# input = {
#     #"input": "现在的日期是2023年，9月15日。一年，有365天，一个月有30天。知乎，是一个中文互联网高质量问答社区和创作者聚集的原创内容平台，于2011年1月正式上线，以“让人们更好地分享知识、经验和见解，找到自己的解答”为品牌使命。知乎凭借认真、专业、友善的社区氛围、独特的产品机制以及结构化和易获得的优质内容，聚集了中文互联网科技、商业、影视、时尚、文化领域最具创造力的人群，已成为综合性、全品类、在诸多领域具有关键影响力的知识分享社区和创作者聚集的原创内容平台，建立起了以社区驱动的内容变现商业模式。 [1]知乎，2017年11月8日入选时代影响力·中国商业案例TOP30。 [2] 2019年10月21日，胡润研究院发布《2019胡润全球独角兽榜》，知乎排名第138位。 [3] 6月6日原有的“知识市场”业务升级为“知乎大学”。 [4] 7月，知乎完成新一轮融资，融资额接近3亿美元。 [5] 2019年8月12日，知乎宣布完成F轮融资，总额4.34亿美元。 [6]截至2020年12月，知乎上的总问题数超过4400万条，总回答数超过2.4亿条。在付费内容领域，知乎月活跃付费用户数已超过250万，总内容数超过300万，年访问人次超过30亿。 [7]知乎以问答业务为基础，经过近十年的发展，已经承载为综合性内容平台，覆盖“问答”社区、全新会员服务体系“盐选会员”、机构号、热榜等一系列产品和服务，并建立了包括图文、音频、视频在内的多元媒介形式。 [8]2022年4月22日，知乎在港交所实现双重上市 [45] 。",
#     # "prompt": "问答",
#     "input":"今天的日期是<mask_0>年，<mask_1>月<mask_2>日。",
#     "prompt": "填空",
#     #"question": "",
#     "<ans>":{
#         "mask_0":"",
#         "mask_1":"",
#         "mask_2":""
#         },
# }
input = {
    "input": "心理学领域的研究人员发现，做出重要决定的最好方法之一，比如选择一所大学或<mask_0>，都涉及到使用决策工作表。研究优化的心理学家将<mask_1>与理论理想决策进行比较，看看它们有多相似。工作表程序的支持者认为它会产生最优的，也就是说，最好的决策。虽然有<mask_2>可以接受，但它们在本质上都是相似的。",
    "<ans>":{
      "<mask_0>":"",
      "<mask_1>":"",
      "<mask_2>":""
    }

}

endpoint_name = "cpm-bee-230913084052OZPY"
ak = "eb79fd4f4bc811ee9f4c0242ac120004"
sk = "QWg=pBZeBhkN7U6UP4tqAGqscTnPI+#K"
host = "saas-user-1237853131.us-west-2.elb.amazonaws.com"

timestemp = str(int(time.time()))
hl = hashlib.md5()
hl.update(f"{timestemp}{sk}".encode(encoding='utf-8'))
sign = hl.hexdigest()

url = f"http://{host}/inference"

payload = {
   "endpoint_name": endpoint_name,
   "input": json.dumps(input),
   "ak": ak,
   "timestamp": timestemp,
   "sign": sign
}

response = requests.post(url=url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
if response.status_code != 200:
    print(response.reason, response.text)
else:
    obj_json = response.json()
    if obj_json['code'] != 0:
        print(obj_json)
    else:
        data_str = obj_json['data']['data']
        print(data_str)
        data_obj = json.loads(data_str)
        print(data_obj)