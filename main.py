import requests
from bs4 import BeautifulSoup
from config import *

session= requests.Session()#создаём экземпляр сессии
response=session.get(url)#переходим на начальную страницу
soup=BeautifulSoup(response.text, 'html.parser')
token=soup.find('input',{'name':'token'})['value']#парсим Токен
data={'pma_username':login, 'pma_password':password,'token':token}
users_url='http://185.244.219.162/phpmyadmin/index.php?route=/sql&db=testDB&table=users&pos=0'
response=session.post(users_url,data=data)#переходим на таблицу с таблицой users
soup=BeautifulSoup(response.text, 'html.parser')
users=soup.find_all('td',{'data-decimals':'0'})#парсим id и имя
for column in users:
    print(column.text)
