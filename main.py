import requests


def get_python_articles(for_last_days):
    resp = requests.get('https://api.stackexchange.com/2.3/search',
                        params={'order': 'desc',
                                'min': for_last_days,
                                'sort': 'activity',
                                'tagged': 'Python',
                                'site': 'stackoverflow'})
    return resp.json()


if __name__ == '__main__':
    result = get_python_articles(2)
    for item in result['items']:
        print(item['title'])
