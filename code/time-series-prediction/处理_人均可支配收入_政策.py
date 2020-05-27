# coding=utf-8
import json

jsontext = {'Notes': [], 'description': [], 'years': [], 'Events': []}

jsontext['Notes'].extend(['人均可支配收入自2013-2019, 单位元；数据中避免出现单引号，含单引号会在上传云端数据库时出现错误的闭合'])
jsontext['description'].extend(['居民可支配收入被认为是消费开支的最重要的决定性因素，因而常被用来衡量一个国家生活水平的变化情况,，可支配收入包含四项，分别为：工资性收入、经营性净收入、财产性净收入和转移性净收入。'])
jsontext['years'].extend([18311, 20167, 21966, 23821, 25974, 28228, 30733])


jsontext['Events'].append(['1997-7', False, "亚洲金融危机", "亚洲大部分主要股市的大幅下跌；冲击亚洲各国外贸企业，造成亚洲许多大型企业的倒闭，工人失业，社会经济萧条。打破了亚洲经济急速发展的景象。中国大陆地区和中国台湾地区则几乎不受影响。"])
jsontext['Events'].append(['1998-5', False, "限制公务招待费用", "1998年行政事业单位为执行公务或开展业务活动需要合理开支的接待费用(招待费)要求不得超过公务费的2%"])
jsontext['Events'].append(['2001-5', False, "从价从量符合征税", "对白酒在征收从价消费税的同时再按实际销售量每斤(500克)征收0.5元的定额消费税，同时停止执行外购或委托加工已税酒和酒精生产的酒抵扣上一生产环节已纳消费税的政策。此政策的出台对白酒业压力巨大，导致对策频出。"])
jsontext['Events'].append(['2006-3', True, "从价税调整", "粮食白酒、薯类白酒的比例税率统一调整为20%。"])
jsontext['Events'].append(['2008-1', False, "经济危机", "从2008年第三季度以来，中国出口大幅下滑，经济增速放缓，就业压力加大。"])
jsontext['Events'].append(['2009-1', True, "4万亿计划", "世界经济金融危机日趋严峻，为抵御国际经济环境对我国的不利影响，必须采取灵活审慎的宏观经济政策，以应对复杂多变的形势。当前要实行积极的财政政策和适度宽松的货币政策，出台更加有力的扩大国内需求措施，加快民生工程、基础设施、生态环境建设和灾后重建，提高城乡居民特别是低收入群体的收入水平，促进经济平稳较快增长。"])
jsontext['Events'].append(['2012-3', False, "三公消费受限", "2012年3月26日，国务院召开第五次廉内政工作会议，要求严格控制“三公”经费，禁止用公款购买香烟、高容档酒和礼品。"])
jsontext['Events'].append(["2016-3", True, "第十三个五年规划", "十三五工业结构升级与布局优化研究, 经济结构调整的主攻方向和战略举措研究"])
jsontext['Events'].append(["2018-6", False, "中美贸易战", "受中美贸易战、金融去杠杆等内外部因素影响，今年下半年经济增速、消费品行业增速有所回落，影响白酒动销。"])
jsondata = json.dumps(jsontext, indent=4, separators=(',', ': '), ensure_ascii=False)
f = open('C:\\Users\\eternal\\Desktop\\origin_data\\人均可支配收入(年)_政策.json', 'w', encoding='utf-8')
f.write(jsondata)
f.close()