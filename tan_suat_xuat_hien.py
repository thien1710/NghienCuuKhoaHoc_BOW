import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import numpy as np

def removeIsNotAlpha(s):
    words = nltk.word_tokenize(s)
    words=[word.lower() for word in words if word.isalpha()]
    return words

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return content

def thongKeTop (text):
    fdist2 = FreqDist(text) #Thống kê số từ nhiều nhất
    dictOj = dict(fdist2)
    return dictOj

def sapXepDict (dictOj):
    sortedDictOj = sorted(dictOj.items(), key = lambda kv:(kv[1], kv[0]))
    return sortedDictOj


# sentence = 'This is an example sentence, that sentence is not an an an example sentence'
with open('bo_de_1.txt', encoding='utf-8') as f:
    lines = f.read()

sentenceIsAlpha = removeIsNotAlpha(lines)
# print(sentenceIsAlpha)

sent = content_fraction(sentenceIsAlpha)

# Chỉ lấy các danh từ
# Xem tất cả các pos tags: nltk.help.upenn_tagset()
pos_tag_token = nltk.pos_tag(sent)
list_pos_tag_token = []
for pos in pos_tag_token:
    if pos[1] == 'NN' or pos[1] == 'NNS' or pos[1] == 'NNP' or pos[1] == 'NNPS':
        list_pos_tag_token.append(pos[0])
    else:
        pass

dictionary = thongKeTop(list_pos_tag_token)
# print(f'Dictionary: {dictionary}')
dict1_cond = {k:v for (k,v) in dictionary.items() if v>2 if not k in {'a', 'b', 'c', 'd'}}

dict_for_airthmetic = dict1_cond.copy()
for key, value in dict_for_airthmetic.items():
    dict_for_airthmetic[key] = round(value / float(len(dict_for_airthmetic)) * 100, 2)
list_tu_vung = []
list_tan_xuat = []
list_so_lan = []
for key, value in dict_for_airthmetic.items():
    list_tu_vung.append(key)
    list_tan_xuat.append(value)
for key, value in dict1_cond.items():
    list_so_lan.append(value)
dic_for_export_csv = {}
dic_for_export_csv.update({'Tu_vung': list_tu_vung})
dic_for_export_csv.update({'So_lan': list_so_lan})
dic_for_export_csv.update({'Tan_so': list_tan_xuat})

from pandas import DataFrame
df = DataFrame(dic_for_export_csv, columns= ['Tu_vung', 'So_lan', 'Tan_so'])

export_csv = df.to_csv ('export_dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path

print (df)
print(f'\nDictionary: {dict1_cond}')


sortedDict = sapXepDict(dict1_cond)
print(f'\nDict after sorted: {sortedDict}')

listTuVungThongKeTangDan = []
for oj in sortedDict:
    listTuVungThongKeTangDan.append(oj[0])
print(f'\nTu vung thong ke tang dan: {listTuVungThongKeTangDan}')

# Bieu do
# len(sent)
# fdist1 = FreqDist(sent)
# fdist1.plot(3, cumulative=True)
# plt.show()



# import nltk

# s = "I can't do this now, because I'm so tired.  Please give me some time. @ sd  4 232"

# words = nltk.word_tokenize(s)

# words=[word.lower() for word in words if word.isalpha()]

# print(words)

