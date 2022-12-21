from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from review_english import review_english
from review_korean import review_korean
from review_txt import write_english_txt, write_korean_txt
from hotel_list import pref_list
import time

if __name__ == "__main__":
     
    p_list = pref_list() # 2023/07/01 ~ 02 기준 상위 10개 호텔에 대한 list
    print(len(p_list)) # double check
    print(p_list)

    for href in p_list: # 상위 10개 호텔에 대해 각각

        sc_6, sc6_7, sc7_8, sc8_9, sc9_ = [], [], [], [], []
        review_english(href, sc_6, sc6_7, sc7_8, sc8_9, sc9_) # 평점에 따른 영어 리뷰 가져오기
        write_english_txt(sc_6, sc6_7, sc7_8, sc8_9, sc9_) # 해당 리뷰 txt 파일에 저장하기

        sc_6, sc6_7, sc7_8, sc8_9, sc9_ = [], [], [], [], []
        review_korean(href, sc_6, sc6_7, sc7_8, sc8_9, sc9_) # 평점에 따른 한글 리뷰 가져오기
        write_korean_txt(sc_6, sc6_7, sc7_8, sc8_9, sc9_) # 해당 리뷰 txt 파일에 저장하기

    
