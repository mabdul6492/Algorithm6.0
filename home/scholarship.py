from requests_html import HTMLSession
from bs4 import BeautifulSoup
import urllib

def trusts():
    session = HTMLSession()
    response = session.get("http://bestofhealthindia.com/finance/list-of-charitable-trusts-in-mumbai").html
    source = response.html

    soup = BeautifulSoup(source, 'lxml')

    trusts = soup.find_all('p')[1:-10]

    trusts_name = []

    for trust in trusts:
        # print(trust.text)
        try:
            one = trust.text.split(',')
            two = one[2].split('–')
            three = two[1].split(" ")
            trusts_name.append([one[:1],(one[1],two[0]),three[1:]])
        except:
            pass

    return trusts_name

if __name__ == "__main__":
    print(trusts())
