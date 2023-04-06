import requests
from bs4 import BeautifulSoup

headers= {'User-Agent': 'user agent id'}

url = 'https://www.vetcompendium.be/fr/diergeneesmiddelen'
req = requests.get(url,headers=headers)
soup = BeautifulSoup(req.content,'html.parser')

titles = soup.find_all('h2',class_='field-content uk-h3 uk-margin-remove')
links_list=[]
index = 1

for title in titles:
    click_links = 'https://www.vetcompendium.be'+title.find('a')['href'] #Finding links of titles for getting more details.
    links_list.append(click_links)

for click_link in links_list:
    req = requests.get(click_link, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    tables= soup.find_all('div',class_='region-content')
    info = soup.find_all('div',class_='field_label')

    for table in tables:
        names = table.find('span').get_text()
   
    fields = soup.find_all('div',id='starterkit-content')
    info_list=[]
    
    for field in fields:
        new_field = field.text.strip()
        info_list.append(new_field)
        with open('info.txt', 'a', encoding='utf-8') as f:
            for k in info_list:
                f.write(f"{index}."+ k.replace('\n\n','\n') +f"\n\n{'*'*100}\n\n")
                index +=1
