import requests
from bs4 import BeautifulSoup
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader(__name__, ''),
    autoescape=select_autoescape(['html', 'xml'])
)

TEMPLATE = env.get_template('template.html')

def render(carlist):
    """carlist = [ (year, km, price, place, date), ...]
    """
    return TEMPLATE.render(carlist = carlist)


# ------------------------------
# print (soup)
def writeFile(fname, data):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(data)


def get_parsed_page():
    url = 'https://www.olx.in/items/q-wagonr?isSearchCall=true'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    page = requests.get(url, headers=headers)
    return BeautifulSoup(page.content, 'html.parser')


def getDataFromSoup(soup):
    items = soup.find_all(attrs={"data-aut-id": "itemBox"} )
    print ("no of items = ", len(items))
    print ("Ist item = ")
    print (items[0])
    writeFile('temp.html', items[0].prettify())
    my_list = []

    for item in items:
        try:
            my_list.append(item.get_text())
            print(my_list)
            break
        except:
            continue


    price = item.find(attrs={"data-aut-id": "itemPrice"})
    print ("Price of first item = ", price)


    ## Get details from the data.

    return  [("2000", 1000, 100000, "Mumbai", "01-01-2020") for i in range(3)]

if __name__ == "__main__":
    soup = get_parsed_page()
    DATA = getDataFromSoup(soup)
    result_html = render(DATA)
    writeFile('results.html', result_html)

