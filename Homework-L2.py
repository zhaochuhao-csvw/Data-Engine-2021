import numpy as np
import pandas as pd
import selenium
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import requests
from bs4 import BeautifulSoup

# 请求URL
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

def fetch_content(soup):
    # 得到页面的内容
    print(soup.title)

    # 找到完整的投诉信息框
    temp = soup.find('div', class_="tslb_b")
    # 创建DataFrame
    df = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        # ToDo：提取汽车投诉信息
        print(tr)

        td_list = tr.find_all('td')
        if len(td_list) > 0:
            # 建立临时数据字典
            tmp = {}

            # 投诉编号
            tmp['id'] = td_list[0].text
            # 投诉品牌
            tmp['brand'] = td_list[1].text
            # 投诉车系
            tmp['car_model'] = td_list[2].text
            # 投诉车型
            tmp['type'] = td_list[3].text
            # 问题简述
            tmp['desc'] = td_list[4].text
            # 典型问题
            tmp['problem'] = td_list[5].text
            # 投诉时间
            tmp['datetime'] = td_list[6].text
            # 投诉状态
            tmp['status'] = td_list[7].text

            # 添加到DataFrame里
            df = df.append(temp, ignore_index=True)

    return df

if __name__=='__main__':
    result = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])

    page_num = 16
    for i in range(page_num):
        url = base_url+str(i+1)+'.shtml'
        html = requests.get(url, headers=headers, timeout=10)
        content = html.text
        # 通过content创建BeautifulSoup对象
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        result.append(fetch_content(soup))

    result.to_csv('car_complain_result_page'+str(page_num)+'csv')