#This will not run on online IDE
import requests
from bs4 import BeautifulSoup
import pandas

def Get_ScrapData(URL):
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        return soup
    except:
        return


def UpdateData(soup):
    All_Data = dict()
    if soup:
        data = soup.find('div', attrs={'class':"marketatc_actcont"})

        Table_Heads = data.findAll('thead')[0]

        all_heading = []

        for table_heading in Table_Heads.find('tr'):
            head = table_heading.text.strip()
            if head != str and head != '':
                All_Data[head] = []
                all_heading.append(head)

        data_row = data.findAll('tbody')

        All_tabal_body_row = data_row[0]

        index = 0
        for rows in All_tabal_body_row:
            for row in rows:
                if type(row) != str:
                    datas = str(row.text).strip()
                    if datas != '' and datas != ' ':
                        All_Data[all_heading[index]].append(datas)
                        index += 1
                        index = index % len(all_heading)
    return All_Data

URL = "https://www.moneycontrol.com/stocksmarketsindia/"
soup = Get_ScrapData(URL)
Data = UpdateData(soup)
data_frame = pandas.DataFrame(Data)

print(data_frame)