# coding=utf-8
import json

jsontext = {'Notes': [], 'description': [], 'province': [], 'country': {'year': [], 'month': {}}}
jsontext['Notes'].extend(['为了消除春节假期不固定因素带来的影响，增强数据的可比性，按照国家统计制度，从2012年起，不单独对1月份统计数据进行调查，1-2月份数据一起调查，一起发布。'])
jsontext['description'].extend(["省最大误差0.18千万升，全国最大误差0.38  无上海、海南、香港、澳门、台湾。单位统一为：千万升。省份数据类型为：‘省份名称': [某年商品量 * 5], '全国': ['年度': 【按1994-2019年份排列数据】, '月度'：{按月度排列数据}]"])
jsontext['province'].append({'四川': [370.90, 402.6731, 372.3886, 358.3, 366.7]})
jsontext['province'].append({'山东': [113.13, 112.6360, 106.2709, 40.6, 30.8466]})
jsontext['province'].append({'河南': [110.49, 117.5017, 114.9164, 42.9, 40.9366]})
jsontext['province'].append({'江苏': [99.13, 106.8935, 92.3548, 69.2, 20.7566]})
jsontext['province'].append({'湖北': [87.96, 90.3237, 61.9877, 56.0, 54.1978]})
jsontext['province'].append({'吉林': [67.71, 78.1675, 77.7787, 19.4, 4.3243]})
jsontext['province'].append({'黑龙江': [57.44, 60.9371, 57.7883, 15.3, 10.09]})
jsontext['province'].append({'贵州': [42.801, 49.0072, 45.2067, 30.9, 27.3872]})
jsontext['province'].append({'安徽': [46.45, 44.8889, 43.9334, 43.1, 34.5943]})
jsontext['province'].append({'北京': [27.6239, 31.0216, 33.8154, 46.4, 51.3149]})
jsontext['province'].append({'湖南': [23.6838, 30.5758, 28.6739, 14.8, 11.2432]})
jsontext['province'].append({'云南': [9.5798, 10.1738, 11.3227, 9.6, 6.6306]})
jsontext['province'].append({'河北': [24.4, 22.3992, 23.5963, 16.1, 12.9729]})
jsontext['province'].append({'广东': [19.281, 18.8757, 20.6458, 15.6, 11.8197]})
jsontext['province'].append({'辽宁': [46.36, 8.2796, 2.6959, 1, 0.3709]})
jsontext['province'].append({'江西': [18.2395,16.0143, 16.6860, 11.2, 14.4143]})
jsontext['province'].append({'山西': [8.3594, 10.3239, 13.9907, 16.7, 20.4683]})
jsontext['province'].append({'福建': [5.4412, 5.2616, 5.9893, 6.3, 6.3423]})
jsontext['province'].append({'陕西': [13.6245, 14.2512, 20.1849, 15.7, 16.144]})
jsontext['province'].append({'甘肃': [4.2786, 4.6294, 3.3186, 3.0513, 2.2357]})
jsontext['province'].append({'青海': [1.8466, 2.6259, 1.8262, 1.6726, 1.4157]})
jsontext['province'].append({'浙江': [1.4641, 1.1493, 1.3394, 1.594, 1.897]})
jsontext['province'].append({'内蒙古': [69.00, 75.1397, 6.9827, 5.3159, 4.0497]})
jsontext['province'].append({'广西': [11.7735, 12.0207, 13.0438, 11.2, 9.6169]})
jsontext['province'].append({'西藏': [0.0565, 0.0529, 0.0492, 0.0458, 0.0426]})
jsontext['province'].append({'宁夏': [0.9367, 0.8318, 0.3036, 0.1108, 0.0404]})
jsontext['province'].append({'新疆': [6.8227, 6.8091, 6.1690, 5.589, 5.0636]})
jsontext['province'].append({'天津': [2.4049, 2.7103, 3.1157, 3.5817, 4.1174]})
jsontext['province'].append({'重庆': [20.3889, 22.1831, 11.6860, 11.2, 9.8017]})


jsontext['country']['year'].extend([583.1,  657.4, 691, 708.7, 492.8, 502.3, 476.1, 420.2, 378.5, 331.4, 311.7,349.3, 397.1, 493.9, 569.3, 706.9, 890.6, 1025.8, 1153.1, 1226.7, 1256.9,  1312.80, 1358.3574, 1198.0603, 871.2, 785.9])
jsontext['country']['month'] = {'2015': [199.9, 110.5, 97.2, 100.6, 115.4, 93.8, 91.5, 130, 106.9, 129.9, 137.1],
									'2016': [216.4, 116.2, 100.9, 105.8, 116, 96.2, 97.7, 125.4, 109.3, 132, 142.5],
									'2017': [221.1, 116.6, 106.7, 110.4, 128.7, 99.3, 99.7, 113.4, 52.7, 66.4, 83.1],
									'2018': [194.1, 83.8, 74.5, 70.4, 70.1, 47.8, 53.7, 88.6, 44.9, 74.3, 69],
									'2019': [140, 65.9, 62.1, 57.8, 71.8, 58.5, 52.2, 66.5, 60.3, 62.9, 87.9]}

'''检查数据'''
print("省份数量：", len(jsontext['province']))
for cum in jsontext['province']:
	for name in cum:
		if len(cum[name]) != 5:
			print("%s处数据有缺漏" % name)
		else:pass
		

jsondata = json.dumps(jsontext, indent=4, separators=(',', ': '), ensure_ascii=False)
f = open('C:\\Users\\eternal\\Desktop\\origin_data\\各省白酒商用量.json', 'w', encoding='utf-8')
f.write(jsondata)
f.close()