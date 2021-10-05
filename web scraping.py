import requests as re
import pandas as pd
from bs4 import BeautifulSoup as bs

product = str(input('Enter Product : '))
page = int(input('Enter a Page : '))
pages = page + 1
URL = 'https://www.flipkart.com/search?q='+product+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
print(URL)
list_lp = []

for page in range(1,pages):
    #a=URL + '&page' + '=' + str(page)
    response = re.get(URL + '&page' + '=' + str(page))
    #print(a)
    soup = bs(response.content, 'html5lib')
    #print(soup.prettify())
    if soup.find_all('div', attrs={'class':'_4ddWXP'}):
        flips1 = soup.find_all('div', attrs={'class':'_4ddWXP'})
        #print('hi')
        #print(flips1)
        
        for flip in flips1:
            dataframe = {}
            dataframe['Product'] = flip.find('a', attrs={'class':'s1Q9rs'}).text.replace('\n', '')
            try:
                dataframe['Feature'] = flip.find('div', attrs={'class':'_3Djpdu'}).text.replace('\n', '')
            except:
                dataframe['Feature'] = '--'
            try:
                dataframe['Price'] = flip.find('div', attrs={'class':'_30jeq3'}).text.replace('\n', '')
            except:
                dataframe['Price'] = '--'
            try:
                dataframe['Rating'] = flip.find('div', attrs={'class':'_3LWZlK'}).text.replace('\n','') + '*'
            except:
                dataframe['Rating'] = '--'
            list_lp.append(dataframe)
    elif soup.find_all('div', attrs={'class':'_2kHMtA'}):
        flips1 = soup.find_all('div', attrs={'class':'_2kHMtA'})
        #print(flips2)
            
        for flip in flips1:
            dataframe = {}
            dataframe['Product'] = flip.find('div', attrs={'class':'_4rR01T'}).text.replace('\n', '')
            try:
                features = flip.find('div', attrs={'class':'fMghEO'})
                list_f = []
                for li in features.find_all('li'):
                    a = {}
                    a = li.text
                    list_f.append(a)
                dataframe['Feature'] = list_f
                #print(dataframe['Feature'])
            except:
                dataframe['Feature'] = '--'
            try:
                dataframe['Price'] = flip.find('div', attrs={'class':'_30jeq3 _1_WHN1'}).text.replace('\n', '')
            except:
                dataframe['Price'] = '--'
            try:
                dataframe['Rating'] = flip.find('div', attrs={'class':'_3LWZlK'}).text.replace('\n','') + '*'
            except:
                dataframe['Rating'] = '--'
            list_lp.append(dataframe)
    elif soup.find_all('div', attrs={'class':'_1xHGtK _373qXS'}):
        flips1 = soup.find_all('div', attrs={'class':'_1xHGtK _373qXS'})
        #print(flips2)
            
        for flip in flips1:
            dataframe = {}
            dataframe['Product'] = flip.find('div', attrs={'class':'_2WkVRV'}).text.replace('\n', '')
            try:
                dataframe['Feature'] = flip.find('a', attrs={'class':'IRpwTa'}).text.replace('\n', '')
            except:
                dataframe['Feature'] = '--'
            try:
                dataframe['Price'] = flip.find('div', attrs={'class':'_30jeq3'}).text.replace('\n', '')
            except:
                dataframe['Price'] = '--'
            try:
                dataframe['Rating'] = flip.find('div', attrs={'class':'_3LWZlK'}).text.replace('\n','') + '*'
            except:
                dataframe['Rating'] = '--'
            list_lp.append(dataframe)
    else:
        print('Data Not Found!!')
        
#print(list_lp)
df = pd.DataFrame(list_lp)
df.columns=['Products','Features','Price','Ratings']
df.dtypes
pd.set_option('display.max_rows' ,None)
print(df)
try:
    df.to_excel(product+ '.xlsx')
    print('Excel file is Ready(' + product + '.xlsx).')
except:
    print('Excel file is not created...')