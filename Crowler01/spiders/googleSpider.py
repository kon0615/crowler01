import scrapy
from urllib import request
from bs4 import BeautifulSoup as bs
from Crowler01.items import Post

class GooglespiderSpider(scrapy.Spider):
    searchWord =r"ペアーズ"
    name = "googleSpider"
    allowed_domains = ["blogmura.com"]
    start_urls = [f"https://blogmura.com/search/posts?q={searchWord}"]

    def parse(self, response):
        soup = bs(response.text,'lxml')
        headerList = soup.find_all('li',attrs={"class","blog-list-item"})
        for post in headerList:
            #ヘッダー
            resUrl = post.find('p',attrs={"class","title"}).find('a').get('href') 
            yield Post(
                url = resUrl,
                custamer = "aaa"#self.GetCustamer(resUrl)
            )
            
        #次のページのURL
        footer = soup .find('ul',{"class","pagination-list"})
        #flist = footer.find("div",{"class","pagination"}).find("ul",{"class","pagination-list"})
        PageNext = footer.find('li',{"class","pagination-list-item next"})
        if PageNext is not None:
            NextUrl = PageNext.find('a').get('href') 
        else:
            NextUrl =None
        if NextUrl is None:
            return #なければ終了
        yield scrapy.Request(NextUrl, callback=self.parse)
    def GetCustamer(url:str) -> str:
        #取得したURLからお問い合わせ先を探す
        req = request.Request(url)
        req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36")
        res = request.urlopen(req)
        soup = bs(res,'html.parser')
        return "aaa"
        

