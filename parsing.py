import requests
from bs4 import BeautifulSoup


def params(server,name):
    print(name)
    url = "https://www.leagueofgraphs.com/summoner/"+server+"/" + name
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61"
    }
    return(parsing(url,headers))

#преобразование переменной в нормальный формат
def transformation(text):
    edited_variable = text.text.strip()
    return(edited_variable)

#парсинг данных о ранге
def parsing(url, headers):
    rere = requests.get(url, headers=headers)
    src = rere.text
    soup = BeautifulSoup(src, 'lxml')
    rangCod = soup.find_all("div", class_="tag requireTooltip brown")
    return(rangCod)

#вывод ранга
def elo(rangCod):
    edited_variable = [0]*len(rangCod)
    i = 0
    for rangText in rangCod:
        edited_variable[i]=transformation(rangText)
        i+=1
    return edited_variable
