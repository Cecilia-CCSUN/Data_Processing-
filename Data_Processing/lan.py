# 爬取百度百科方言
import requests
from lxml import etree
if __name__ == '__main__':
    source = open(r'C:\Users\Cecilia\Desktop\区县.txt', 'r', encoding='utf-8')
    for name in source:
        print(name,end = " ")
        url= 'https://baike.baidu.com/item/' + name
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62"
        }
        resp=requests.get(url=url,headers=headers)
        resp.encoding="utf-8"
        page_text=resp.text
        tree=etree.HTML(page_text)
        # print(page_text)
        # 热门城市
        elem_name =tree.xpath("//div[@class='basic-info J-basic-info cmn-clearfix']/dl/dt/text()")
        elem_value=tree.xpath("//div[@class='basic-info J-basic-info cmn-clearfix']/dl/dd/text()")
        # for e in elem_value:
        for e in elem_name:
            if e == "方    言":
                print(e.strip("\n"),elem_value[-6].strip("\n"),elem_value[-5].strip("\n"),elem_value[-4].strip("\n"),elem_value[-3].strip("\n"),elem_value[-2].strip("\n"),elem_value[-1].strip("\n"))


