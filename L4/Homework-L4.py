import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from efficient_apriori import apriori

def get_transactions(dataset):
    transactions = []
    for i in range(0, dataset.shape[0]):
        temp = []
        for j in range(0, 20):
            if str(dataset.values[i, j]) != 'nan':
               temp.append(str(dataset.values[i, j]))
        transactions.append(temp)
    return transactions

if __name__=='__main__':
    dataset = pd.read_csv('./MarketBasket/Market_Basket_Optimisation.csv', header=None)
    transactions=get_transactions(dataset)
    itemsets, rules = apriori(transactions, min_support=0.02, min_confidence=0.4)
    print("频繁项集：", itemsets)
    print("关联规则：", rules)