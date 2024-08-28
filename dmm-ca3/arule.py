import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

data = pd.read_csv('dataset.csv')
head = data.head()
data = data.drop(['month', 'block', 'flat_model','street_name','storey_range','floor_area_sqm', 'lease_commence_date', 'remaining_lease', 'resale_price'], axis=1)
print(data)

records = []
for i in range(0, 103834):
    records.append([str(data.values[i,j]) for j in range(0, 2)])

# [["ang mo kio", "3 room"], ["bukit batok", '2 room']]
association_rules = apriori(records, min_support=0.01, min_confidence=0.4, min_lift=1.8, min_length=2)
association_results = list(association_rules)

print (association_results)
# print(association_rules[0])

# association_results.sort(key=confidence)

for item in association_results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    print("pair", pair)
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")


# from mlxtend.preprocessing import TransactionEncoder
# from mlxtend.frequent_patterns import association_rules
# from mlxtend.frequent_patterns import apriori


# te = TransactionEncoder()
# te_array = te.fit(records).transform(records)
# df = pd.DataFrame(te_array, columns=te.columns_)

# frequent_itemsets_ap = apriori(df, min_support=0.01, use_colnames=True)

# print(frequent_itemsets_ap)

# rules_ap = association_rules(frequent_itemsets_ap, metric="confidence", min_threshold=0.08)

# print(rules_ap)