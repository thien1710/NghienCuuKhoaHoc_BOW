#List các document
documents = []
documents.append("the quick brown fox jumps over the lazy dog and")
documents.append("never jump over the lazy dog quickly")
#['the quick brown fox jumps over the lazy dog and',
# 'never jump over the lazy dog quickly']

#List các từ trong mỗi document sau khi split
bow = []
for doc in documents:
    bow.append(set(doc.split(" ")))
# [{'jumps', 'quick', 'and', 'brown', 'dog', 'fox', 'over', 'lazy', 'the'},
#  {'quickly', 'jump', 'never', 'dog', 'over', 'lazy', 'the'}]

#List các tất cả từ đã split
word_dict = set()
for word in bow:
    word_dict = word_dict.union(word)
#{'lazy', 'fox', 'brown', 'and', 'over', 'dog', 'jump',
# 'never', 'quick', 'jumps', 'the', 'quickly'}

count_word=[] #Số lần xuất hiện mỗi từ, chứa mỗi document với các từ đã split
#Đếm số lần xuất hiện mỗi từ trong 1 document
for doc in documents:
    senc=doc.split(" ")
    # print(senc)
    list_word={}
    for w in senc:
        try:
            list_word[w] += 1
        except:
            list_word[w] = 1
    count_word.append(list_word)
#[{'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1,
# 'over': 1,'lazy': 1, 'dog': 1, 'and': 1},
# {'never': 1, 'jump': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog': 1, 'quickly': 1}]

# Tìm những từ không xuất hiện trong 1 document và gán = 0
for word in word_dict:
    for sentence in count_word:
        try:
            if sentence[word]!=0:
                pass
        except:
            sentence[word]=0
#count_word:
#[
    # {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1,
    # 'dog': 1, 'and': 1, 'never': 0, 'quickly': 0, 'jump': 0
    # },

    # {'never': 1, 'jump': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog': 1, 'quickly': 1,
    # 'and': 0, 'brown': 0, 'fox': 0, 'jumps': 0, 'quick': 0
    # }
# ]

# word_dictX = []
# for word in word_dict:
#     word_dictX.append(dict.fromkeys(word_dict, 0))
# # print(word_dictX)


def compute_TF(word_dict, bow):
    tf_dict = {}
    bow_count = len(bow)
    for word, count in word_dict.items():
        tf_dict[word] = count/float(bow_count)
    return tf_dict
tf_bow = []
for i in range(len(count_word)):
    tf_bow.append(compute_TF(count_word[i], bow[i]))
print(tf_bow)

# for dict_document in tf_bow:
#     print(dict_document)

import pandas as pd

# (pd.DataFrame.from_dict(data=tf_bow[1], orient='index').to_csv('tester4.csv', header=False))
# with open('tester42.csv', 'w') as f:
#     [f.write('{0}: {1}\n'.format(key, value)) for key, value in tf_bow[0].items()]
