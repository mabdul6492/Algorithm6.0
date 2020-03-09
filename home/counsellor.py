from requests_html import HTMLSession
from bs4 import BeautifulSoup
import urllib


def counsellors():
    urls = []
    all_counsellors = []
    count = 1

    for i in range(1, 3):
        urls.append(
            f'https://www.careerguide.com/career-experts-in-india/p-{i}')

    for url in urls:
        session = HTMLSession()
        response = session.get(url).html
        source = response.html

        soup = BeautifulSoup(source, 'lxml')
        counsellors = soup.find_all(
            'div', class_='m-content c-bg-white c-border')

        for counsellor in counsellors:
            title = counsellor.find('h4').text.strip()
            status = counsellor.find('p').text.strip()
            info = counsellor.find('span', class_='m-more').text.strip()
            profile = counsellor.find('div', class_='col-md-6 col-xs-6')
            profile = counsellor.find('a').attrs['href']
            profile = 'https://www.careerguide.com'+profile
            image = counsellor.find('img')['src']
            image = 'https://www.careerguide.com'+image
            try:
                urllib.request.urlretrieve(image, f"images/{title}.jpg")
            except:
                pass
            linkedin = ''
            try:
                session = HTMLSession()
                response = session.get(profile).html
                source = response.html

                soup = BeautifulSoup(source, 'lxml')
                linkedin = soup.find('p', class_='c-font-thin')
                linkedin = linkedin.find('a').attrs['href']
            except:
                pass
            all_counsellors.append((title, status, info, linkedin))
            print(count, end=" ")
            count = count + 1
    return all_counsellors


if __name__ == "__main__":
    counsellors()
