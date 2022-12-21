# english review
import re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def file_open(f):
    
    lines = f.readlines()
    line = []
    for i in range(len(lines)):
        line.append(lines[i])

    f.close()

    result = analyze_top50(line)
    return result


def analyze_top50(line : list):
    compile = re.compile("\W+") # 대, 소문자 통일
    for i in range(len(line)):
        a = compile.sub(" ", line[i])
        line[i] = a.lower()

    stop_word_eng = set(stopwords.words('english')) # 불용어 제거
    line = [i for i in line if i not in stop_word_eng]

    ps_stemmer = PorterStemmer()
    token = RegexpTokenizer('[\w]+')
    result = [token.tokenize(i) for i in line]
    middle_result= [r for i in result for r in i]
    final_result = [ps_stemmer.stem(i) for i in middle_result if not i in stop_word_eng] # 불용어 제거한 단어만 들어가 있는 리스트

    print("proceed...")

    # series = pd.Series(final_result2).value_counts().head(30) -> shape == (30,)
    top50 = pd.Series(final_result).value_counts(normalize=True).head(50) # top50, 비율로
    return top50


r_6, r6_7, r7_8, r8_9, r9_ = [], [], [], [], []
f = open(".//review//re_6.txt",'rt',encoding='utf-8')
result_6 = file_open(f)
for i in range(0,50):
    r_6.append(result_6.index[i])

f = open(".//review//re6_7.txt",'rt',encoding='utf-8')
result6_7 = file_open(f)
for i in range(0,50):
    r6_7.append(result6_7.index[i])

f = open(".//review//re7_8.txt",'rt',encoding='utf-8')
result7_8 = file_open(f)
for i in range(0,50):
    r7_8.append(result7_8.index[i])

f = open(".//review//re8_9.txt",'rt',encoding='utf-8')
result8_9 = file_open(f)
for i in range(0,50):
    r8_9.append(result8_9.index[i])

f = open(".//review//re9_.txt",'rt',encoding='utf-8')
result9_ = file_open(f)
for i in range(0,50):
    r9_.append(result9_.index[i])

set_word = list(set(r_6)&set(r6_7)&set(r7_8)&set(r8_9)&set(r9_)) # 상위 5개 안의 공통된 단어중 호텔 평점에 따라 등장 빈도가 증가하는 추세를 보이는 단어들
word_score = {} # ['bu', 'hotel', 'bed', 'station', 'walk', 'clean', 'shop', 'great', 'seoul', 'close', 'time', 'servic', 'staff', 'stay', 'shuttl', 'area', 'locat', 'conveni', 'nice', 'good', 'friendli', 'free', 'room', 'comfort', 'help', 'us', 'airport']
print(set_word)

for i in set_word:
    score = []
    if result_6[i] < result6_7[i] and result6_7[i] < result7_8[i] and result7_8[i] < result8_9[i] and result8_9[i] < result9_[i]:
        score.append(result_6[i])
        score.append(result6_7[i])
        score.append(result7_8[i])
        score.append(result8_9[i])
        score.append(result9_[i])
        word_score[i] = score

print(word_score.keys()) # dict_keys(['friendli', 'bed', 'help', 'shuttl', 'great', 'seoul', 'free'])

label = ["~6","6~7","7~8","8~9","9~"]
index = np.arange(len(label))
bar_width = 0.12
alpha = 0.5
p1 = plt.bar(index, word_score['bed'], bar_width, color='b', alpha=alpha, label='bed')
p2 = plt.bar(index + bar_width*1, word_score['seoul'], bar_width, color='r', alpha=alpha, label='seoul')
p3 = plt.bar(index + bar_width*2, word_score['friendli'], bar_width, color='y', alpha=alpha, label='friendli')
p4 = plt.bar(index + bar_width*3, word_score['help'], bar_width, alpha=alpha, label='help')
p5 = plt.bar(index + bar_width*4, word_score['free'], bar_width, alpha=alpha, label='free')
p6 = plt.bar(index + bar_width*5, word_score['shuttl'], bar_width, alpha=alpha, label='shuttl')
p7 = plt.bar(index + bar_width*6, word_score['great'], bar_width, alpha=alpha, label='great')
plt.legend((p1[0],p2[0],p3[0],p4[0],p5[0],p6[0],p7[0]),('bed','seoul','friendli','help','free','shuttl','great'))
plt.xlabel('grade', fontsize = 13)
plt.ylabel('rate', fontsize = 13)
plt.xticks(index, label, fontsize = 9)
plt.show()






