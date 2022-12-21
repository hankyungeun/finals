from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def pref_list(): # 2023/07/01 ~ 02 기준 상위 10개 호텔의 href를 return
    p_list = []
    dr = webdriver.Chrome()
    dr.get('https://www.agoda.com/ko-kr/search?city=14690&checkIn=2023-07-01&los=1&rooms=1&adults=1&children=0&cid=1719676&locale=ko-kr&ckuid=0be58580-0455-41a6-93f2-f5981c3c2765&prid=0&currency=KRW&correlationId=bcdaf3aa-6729-47c6-9426-1b90d0fa4a36&pageTypeId=1&realLanguageId=9&languageId=9&origin=KR&userId=0be58580-0455-41a6-93f2-f5981c3c2765&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=26&currencyCode=KRW&htmlLanguage=ko-kr&cultureInfoName=ko-kr&machineName=hk-pc-2f-acm-web-user-7c85744d98-pc7dk&trafficGroupId=1&sessionId=r312jogkij4rhrpobhbzz1pe&trafficSubGroupId=86&aid=130589&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&checkOut=2023-07-02&priceCur=KRW&textToSearch=%EC%84%9C%EC%9A%B8&travellerType=0&familyMode=off&productType=-1')
    time.sleep(10)

    ol_tag = dr.find_element(By.CLASS_NAME, 'hotel-list-container') 
    li_tag = ol_tag.find_elements(By.CLASS_NAME, 'PropertyCardItem')

    for i, li in enumerate(li_tag):
        bf = []
        div_tag = li.find_element(By.CLASS_NAME,'hRUYUu')
        a_tag = div_tag.find_element(By.TAG_NAME,'a')
        href = a_tag.get_attribute('href')
        p_list.append(href)
        if i >= 9:
           break

    return p_list