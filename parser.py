import requests
from bs4 import BeautifulSoup


HOST = 'https://hh.ru/'
URL = ('https://hh.ru/search/vacancy?text=Python&area=1&salary=&currency_code='
       'RUR&experience=doesNotMatter&schedule=remote&order_by='
       'relevance&search_period=0&items_on_page=50&no_magic='
       'true&L_save_area=true')
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
              'image/avif,image/webp,image/apng,*/*;q=0.8,application/'
              'signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.74 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='vacancy-serp-item-body__main-info')
    vacancies = []
    counter = 0
    for item in items[:5]:
        vacancies.append(
            {
                'employer': item.find(
                    'a', class_='bloko-link bloko-link_kind-tertiary').text,
                'title': item.find(
                    'div', class_='').find('h3').get_text(),
            #     'compensation': item.find(
            #         'span', class_='bloko-header-section-3').text.split(),
            }
        )
        counter += 1
    print(f'processed: {counter}')
    return vacancies


if __name__ == '__main__':
    html = get_html(URL)
    print(*get_content(html.text), sep='\n')
