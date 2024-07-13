import scrapy
#from urllib import request
import requests
from urllib.parse import urlparse
from urllib.parse import unquote
from bs4 import BeautifulSoup as bs
from Crowler01.items import Post
import random
from time import sleep

class GooglespiderSpider(scrapy.Spider):
    searchWord =r"恋活 アプリ"
    name = "googleSpider"
    allowed_domains = ["blogmura.com"]
    start_urls = [f"https://blogmura.com/search/posts?q={searchWord}"]

    def parse(self, response):
        sleep(random.randrange(2))
        soup = bs(response.text,'lxml')
        headerList = soup.find_all('li',attrs={"class","blog-list-item"})
        for post in headerList:
            #ヘッダー
            resUrl = post.find('p',attrs={"class","title"}).find('a').get('href') 
            urlQuery = unquote(urlparse(resUrl).query)
            blog = remove_before_colon(urlQuery)
            cus = GetCustamer(blog)#カスタマー
            yield Post(
                url = blog,
                custamer = cus#self.GetCustamer(resUrl)
            )
            
        #次のページのURL
        footer = soup .find('ul',{"class","pagination-list"})
        PageNext = footer.find('li',{"class","pagination-list-item next"})
        if PageNext is not None:
            NextUrl = PageNext.find('a').get('href') 
        else:
            NextUrl =None
        
        if NextUrl is None:
            return #なければ終了
        yield scrapy.Request(NextUrl, callback=self.parse)
#自分で実装した関数
def GetCustamer(url:str) -> str:
    #取得したURLからお問い合わせ先を探す
    contactWord = ["contact","support"]
    p = urlparse(url)
    host = f"{p.scheme}://{p.netloc}" #ホストURL
    #リクエストを送って存在するか確認
    print(host)
    for item in contactWord:
        target = f"{host}/{item}/"
        #sleep(random.randrange(3))
        try:
            res = requests.get(target)
        except:
            continue
        if res.status_code == 200:
            return target
        else:
            continue
    return ''

    

    #クエリパラメータからURLを取り出す
def remove_before_colon(text):
    index = text.find('url=') # ':'の位置を取得
    if index == -1:
        index = text.find('url=')
    if index != -1:  # ':'が見つかった場合
        return text[index+4:].strip()  # ':'より後ろの部分を取得して返す（前後の空白を削除）
    else:
        return text  # ':'が見つからない場合はそのままの文字列を返す


