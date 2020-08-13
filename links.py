import requests
import bs4 
import pandas as pd
import csv


url = 'http://ramognee.com'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.content,'lxml')
links=[]
for link in soup.find_all('a',href=True):
    if link['href'] == '#':
        link['href'] = url+'/'
    x = link['href'].replace('#',url+'/')
    links.append(x)
# print(links)
df = pd.DataFrame({'LINKS':links}) 
df.to_csv('links.csv', index=False, encoding='utf-8')

# # Import CSV
# data = pd.read_csv (r'C:\Users\Ron\Desktop\Test\People.csv')   
# df = pd.DataFrame(data, columns= ['Name','Country','Age'])

# # Connect to SQL Server
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=RON\SQLEXPRESS;'
#                       'Database=TestDB;'
#                       'Trusted_Connection=yes;')
# cursor = conn.cursor()

# # Create Table
# cursor.execute('CREATE TABLE people_info (Name nvarchar(50), Country nvarchar(50), Age int)')

# # Insert DataFrame to Table
# for row in df.itertuples():
#     cursor.execute('''
#                 INSERT INTO TestDB.dbo.people_info (Name, Country, Age)
#                 VALUES (?,?,?)
#                 ''',
#                 row.Name, 
#                 row.Country,
#                 row.Age
#                 )
# conn.commit()