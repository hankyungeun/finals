from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def review_english(href, sc_6, sc6_7, sc7_8, sc8_9, sc9_):

    dr = webdriver.Chrome()
    dr.get(href)    
    dr.implicitly_wait(10);    time.sleep(5)

    dr.find_element(By.XPATH,'//*[@id="hotelNavBar"]/div/ul/li[4]/button/span').click() # 이용 후기
    time.sleep(1)

    try:
        dr.find_element(By.XPATH,'//*[@id="dismiss-btn"]/p').click() # 팝업 닫기
    except:
        pass

    time.sleep(1)     
    dr.find_element(By.XPATH,'//*[@id="reviewFilterSection"]/div[1]/div[3]/span').click() # 작성 언어
    time.sleep(1)
    dr.find_element(By.XPATH,'//*[@id="reviewFilterSection"]/div[1]/div[3]/div/ul/li[3]/span/span[2]').click() # english
    
    def get_review(dr : webdriver, lst): # last page 까지 돌면서 title, text를 저장하는 함수

        while True:
            time.sleep(5)
            title = dr.find_elements(By.CLASS_NAME,'Review-comment-bodyTitle') # 제목 cf) id는 0부터 시작
            time.sleep(5)  
            for i in title:
                lst.append(i.text)      
            time.sleep(5)   
            txt = dr.find_elements(By.CLASS_NAME,'Review-comment-bodyText') # 본문
            time.sleep(5) 
            for i in txt:
                lst.append(i.text)
            time.sleep(5)
            
            try:  # 한 page만 존재하는 경우
                dr.find_element(By.CLASS_NAME,'ficon-carrouselarrow-right').click() # ficon ficon-24 ficon-carrouselarrow-right
            except:
                return lst
                        
            dr.implicitly_wait(3)

            try: 
                dr.find_element(By.CLASS_NAME,'Review-paginator--lastPage') # last page class 발견되면 종료
                return lst
            except:
                pass    # 발견되지 않으면 계속 진행
                   
    dr.find_element(By.XPATH,'//*[@id="reviewSection"]/div[3]/div[1]/div/div[3]/div/div[1]/div/div/div[1]/div/span/span').click() # 9점 이상 - 최고 start
    get_review(dr, sc9_)
    time.sleep(2)
    dr.find_element(By.XPATH,'//*[@id="reviewSection"]/div[3]/div[1]/div/div[3]/div/div[1]/div/div/div[1]/div/span/span').click() # 9점 이상 - 최고 end
    time.sleep(2)

    dr.find_element(By.XPATH,'//*[@id="reviewSection"]/div[3]/div[1]/div/div[3]/div/div[1]/div/div/div[2]/div/span/span').click() # 8~9점 - 우수 start
    get_review(dr, sc8_9)    
    time.sleep(2)
    dr.find_element(By.XPATH,'//*[@id="reviewSection"]/div[3]/div[1]/div/div[3]/div/div[1]/div/div/div[2]/div/span/span').click() # 8~9점 - 우수 end
    time.sleep(2)

    dr.find_element(By.XPATH,'//*[@id="reviewSection"]/div[3]/div[1]/div/div[3]/div/div[1]/div/div/div[3]/div/span/span').click() # 7~8점 - 좋음 start
    get_review(dr, sc7_8)    
    time.sleep(2)
    dr.find_element(By.XPATH,'//*[@id="reviewSection"]/div[3]/div[1]/div/div[3]/div/div[1]/div/div/div[3]/div/span/span').click() # 7~8점 - 좋음 end
    time.sleep(2)

    dr.find_element(By.XPATH,'//*[@id="reviewSection"]/div[3]/div[1]/div/div[3]/div/div[1]/div/div/div[4]/div/span/span').click() # 6~7점 - 양호 start
    get_review(dr, sc6_7)
    time.sleep(2)
    dr.find_element(By.XPATH,'//*[@id="reviewSection"]/div[3]/div[1]/div/div[3]/div/div[1]/div/div/div[4]/div/span/span').click() # 6~7점 - 양호  end
    time.sleep(2)

    dr.find_element(By.XPATH,'//*[@id="reviewSection"]/div[3]/div[1]/div/div[3]/div/div[1]/div/div/div[5]/div/span/span').click() # 6점 미만 - 기대 이하 start
    get_review(dr, sc_6)
    time.sleep(2)
    dr.find_element(By.XPATH,'//*[@id="reviewSection"]/div[3]/div[1]/div/div[3]/div/div[1]/div/div/div[5]/div/span/span').click() # 6점 미만 - 기대 이하 end
    time.sleep(2)

    return









