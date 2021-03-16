from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from lxml import etree
from nltk.tokenize import word_tokenize

# 生成词云
def create_word_cloud(f):
    print('根据词频，开始生成词云!')
    # f = remove_stop_words(f)
    cut_text = word_tokenize(f)
    #print(cut_text)
    cut_text = " ".join(cut_text)
    wc = WordCloud(
        max_words=100,
        width=2000,
        height=1200,
    )
    wordcloud = wc.generate(cut_text)
    # 写词云图片
    wordcloud.to_file("wordcloud.jpg")
    # 显示词云文件
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def get_transactions(dataset):
    transactions = []
    for i in range(0, dataset.shape[0]):
        temp = []
        for j in range(0, 20):
            if str(dataset.values[i, j]) != 'nan':
               temp.append(str(dataset.values[i, j]))
        #print(temp)
        transactions.extend(temp)
    return transactions

if __name__ == '__main__':
    # 数据加载
    data = pd.read_csv('./MarketBasket/Market_Basket_Optimisation.csv',header = None)
    #print(data)

    transactions =get_transactions(data)
    print(len(transactions))
    all_words = " ".join(transactions)
    create_word_cloud(all_words)
