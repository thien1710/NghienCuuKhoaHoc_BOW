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
#tf_bow:
#[
    # {'the': 0.2222222222222222, 'quick': 0.1111111111111111,
        # 'brown': 0.1111111111111111, 'fox': 0.1111111111111111,
        # 'jumps': 0.1111111111111111, 'over': 0.1111111111111111,
        # 'lazy': 0.1111111111111111, 'dog': 0.1111111111111111,
        # 'and': 0.1111111111111111, 'jump': 0.0, 'never': 0.0,
        # 'quickly': 0.0
    # },
    # {'never': 0.14285714285714285,
        # 'jump': 0.14285714285714285, 'over': 0.14285714285714285,
        # 'the': 0.14285714285714285, 'lazy': 0.14285714285714285,
        # 'dog': 0.14285714285714285, 'quickly': 0.14285714285714285,
        # 'quick': 0.0, 'and': 0.0, 'jumps': 0.0,
        # 'fox': 0.0, 'brown': 0.0
    # }
# ]

def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)

    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))

    return idfDict

idf_bow = computeIDF(count_word)
# idf_bow:
#     {'the': 0.0, 'quick': 0.6931471805599453,
#     'brown': 0.6931471805599453, 'fox': 0.6931471805599453,
#     'jumps': 0.6931471805599453, 'over': 0.0,
#     'lazy': 0.0, 'dog': 0.0,
#     'and': 0.6931471805599453, 'quickly': 0.6931471805599453,
#     'jump': 0.6931471805599453, 'never': 0.6931471805599453
# }

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val * idfs[word]
    return tfidf

# tfidfBowA = computeTFIDF(tfBowA, idfs)
# tfidfBowB = computeTFIDF(tfBowB, idfs)
tf_idf_bow = []
for i in range(len(tf_bow)):
    tf_idf_bow.append(computeTFIDF(tf_bow[i], idf_bow))
print('='*100 + f'\n{tf_idf_bow}')

#Export to Dataframe
import pandas as pd

#From DF
dfTotal=pd.DataFrame()
for tfbow in range (len(tf_bow)):
    df = pd.DataFrame([tf_bow[tfbow]])
    dfTotal = dfTotal.append(df)
print('='*100 + f'\nDF:\n  {dfTotal}\n')
export_csv = dfTotal.to_csv('df_CSV.csv', index=True, header=True)

#From IDF
idfTotal=pd.DataFrame([idf_bow])
print('='*100 + f'\nIDF:\n  {idfTotal}\n')
export_csv = idfTotal.to_csv('idf_CSV.csv', index=True, header=True)

#From TF_IDF
tf_idfTotal=pd.DataFrame()
for t_i_bow in range (len(tf_idf_bow)):
    df = pd.DataFrame([tf_idf_bow[t_i_bow]])
    tf_idfTotal = tf_idfTotal.append(df)
print('='*100 + f'\nTF_IDF:\n  {tf_idfTotal}\n')
export_csv = dfTotal.to_csv('tf_idf_CSV.csv', index=True, header=True)
