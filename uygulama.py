import requests
from bs4 import BeautifulSoup as BS
import html5lib


user_data = {
 'utf8': '✓',
 'login': 'murat896ytk@gmail.com',
 'password' : 'sdfdsfds'
}

isue_data = {
        'utf8': '✓',
        'issue''[title]':'sedat deneme başarılı'
    }

headers ={
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Mobile Safari/537.36'
}

with requests.Session() as ses:

    url ='https://github.com/session'
    r =ses.get(url,headers=headers)

    soup2 =BS(r.content,'html5lib')
    user_data ['authenticity_token']= soup2.find('input',attrs={'name':'authenticity_token'})['value']
    giris_yap = ses.post(url,headers=headers,data=user_data)
    print(giris_yap.text)
    print(soup2.find('input',attrs={'name':'authenticity_token'})['value'])



    url2 = 'https://github.com/Sdtdogru/Spring-boot-Entity-tabel-create/issues/new'
    r2 = ses.get(url2)
    soup = BS(r2.content, 'html5lib')
    isue_data['authenticity_token'] = soup.find(id='new_issue').find(
        'input', attrs={'name': 'authenticity_token'})['value']
    gonder = ses.post('https://github.com/Sdtdogru/Spring-boot-Entity-tabel-create/issues', headers=headers, data=isue_data)








