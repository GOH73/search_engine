import time

import requests
import random
from bs4 import BeautifulSoup

domain_name = 'https://www.qimao.com/'
path = f'{domain_name}shuku/'

# 客户端代理列表
USER_AGENT_LIST = ['zspider/0.9-dev http://feedback.redkolibri.com/',
                   'Xaldon_WebSpider/2.0.b1',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) Speedy Spider ('
                   'http://www.entireweb.com/about/search_tech/speedy_spider/)',
                   'Mozilla/5.0 (compatible; Speedy Spider; http://www.entireweb.com/about/search_tech/speedy_spider/)',
                   'Speedy Spider (Entireweb; Beta/1.3; http://www.entireweb.com/about/search_tech/speedyspider/)',
                   'Speedy Spider (Entireweb; Beta/1.2; http://www.entireweb.com/about/search_tech/speedyspider/)',
                   'Speedy Spider (Entireweb; Beta/1.1; http://www.entireweb.com/about/search_tech/speedyspider/)',
                   'Speedy Spider (Entireweb; Beta/1.0; http://www.entireweb.com/about/search_tech/speedyspider/)',
                   'Speedy Spider (Beta/1.0; www.entireweb.com)',
                   'Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)',
                   'Speedy Spider (http://www.entireweb.com/about/search_tech/speedyspider/)',
                   'Speedy Spider (http://www.entireweb.com)',
                   'Sosospider+(+http://help.soso.com/webspider.htm)',
                   'sogou spider',
                   'Nusearch Spider (www.nusearch.com)',
                   'nuSearch Spider (compatible; MSIE 4.01; Windows NT)',
                   'lmspider (lmspider@scansoft.com)',
                   'lmspider lmspider@scansoft.com',
                   'ldspider (http://code.google.com/p/ldspider/wiki/Robots)',
                   'iaskspider/2.0(+http://iask.com/help/help_index.html)',
                   'iaskspider',
                   'hl_ftien_spider_v1.1',
                   'hl_ftien_spider',
                   'FyberSpider (+http://www.fybersearch.com/fyberspider.php)',
                   'FyberSpider',
                   'everyfeed-spider/2.0 (http://www.everyfeed.com)',
                   'envolk[ITS]spider/1.6 (+http://www.envolk.com/envolkspider.html)',
                   'envolk[ITS]spider/1.6 ( http://www.envolk.com/envolkspider.html)',
                   'Baiduspider+(+http://www.baidu.com/search/spider_jp.html)',
                   'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
                   'BaiDuSpider',
                   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com',
                   ]


def sleep():
    time.sleep(random.randrange(0, 3))


# 处理小说页面
def process_novel_page(page: str):
    soup = BeautifulSoup(page, 'html.parser')
    for num in range(15):
        url_tag = soup.select(
            'body > div.wrapper.padding-top.border-top > div > div:nth-child(2) > div > div.qm-mod-tb > '
            f'div.con-box.books-pic-con.js-list-data > ul > li:nth-child({num + 1}) > div.txt > span.s-tit > a')[
            0]

        cover_tag = soup.select(
            'body > div.wrapper.padding-top.border-top > div > div:nth-child(2) > div > '
            f'div.qm-mod-tb > div.con-box.books-pic-con.js-list-data > ul > li:nth-child({num + 1}) > '
            'div.pic > a > img')[0]

        href = url_tag['href']
        name = url_tag.text
        cover_src = cover_tag['src']
        cover = requests.get(cover_src)
        page_path = domain_name + href

        response = requests.get(page_path)
        response.headers['User-Agent'] = random.choice(USER_AGENT_LIST)
        with open(f'./novel_pages/{name}.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
        with open(f'./covers/{name}.jpg', 'wb') as file:
            file.write(cover.content)
            print(f'{name}.jpg下载完成')
        sleep()


# 处理排行榜页面
def process_rank_page():
    for page_num in range(3):
        # 随机选择代理
        usr_agent = random.choice(USER_AGENT_LIST)

        tail = f'a-a-a-a-a-a-a-click-{page_num + 1}'
        url = path + tail + '/'

        response = requests.get(url)
        response.headers['User-Agent'] = usr_agent
        sleep()
        process_novel_page(response.text)

        with open(f"./web_pages/{tail}.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f'第{page_num + 1}页，done')
        sleep()


process_rank_page()
