import re
from konlpy.tag import Okt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

okt = Okt()


def read_review(file):
    f = open(file, 'r')
    lines = f.readlines()
    for line in lines:
        test = analyze_korea_review(line)
    f.close()

    return test


def analyze_korea_review(str):
    compile = re.compile("[^ ㄱ-ㅣ가-힣]+")
    # 특수문자 제거
    review = compile.sub("", str)

    # 형태소 분석
    analyze_noun = okt.nouns(review)

    total_list = []
    for term in analyze_noun:
        total_list.append(term)

    korea_result = pd.Series(total_list).value_counts(normalize=True).head(100)
    return korea_result

list1, list2, list3, list4, list5 = [], [], [], [], []

review6 = read_review("/Users/yeju/Desktop/DataCrawling/review/ke_6.txt")
for term in review6.index:
    list1.append(term)

review7 = read_review("/Users/yeju/Desktop/DataCrawling/review/ke6_7.txt")
for term in review7.index:
    list2.append(term)

review8 = read_review("/Users/yeju/Desktop/DataCrawling/review/ke7_8.txt")
for term in review8.index:
    list3.append(term)

review9 = read_review("/Users/yeju/Desktop/DataCrawling/review/ke8_9.txt")
for term in review9.index:
    list4.append(term)

review10 = read_review("/Users/yeju/Desktop/DataCrawling/review/ke9_.txt")
for term in review10.index:
    list5.append(term)

# 중복 단어 찾기
set_word = (set(list1) & set(list2) & set(list3) & set(list4) & set(list5))
print(set_word)

word_score = {}
for i in set_word:
    score = []

    if review6[i] < review7[i] < review8[i] < review9[i] < review10[i]:
        score.append(review6[i])
        score.append(review7[i])
        score.append(review8[i])
        score.append(review9[i])
        score.append(review10[i])
        word_score[i] = score

    print(word_score.keys())
