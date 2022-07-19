import requests
from lxml import html
from collections import Counter
import cssselect


# принимает ссылку на страницу, подсчитывает имеющиеся на ней теги и возвращает их
def count_tags(url=''):

    if 'https://' in url or 'http://' in url:

        try:
            page = requests.get(url)
            tree = html.fromstring(page.content)
            all_elms = tree.cssselect('*')
            all_tags = [elm.tag for elm in all_elms]
            count_tags = Counter(all_tags)

            # print('all tags:', dict(count_tegs))
            # print('all count:', len(all_elms), 'head:', count_tegs['head'])

            result = {url: count_tags}
            return result

        except:
            return 'Страница отсутствует'

    else:
        return 'Введите корректный url-адрес'
