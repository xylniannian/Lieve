import requests
from lxml import etree
import csv
import time



def top_thirty(n):
    url = 'https://search.jd.com/Search?keyword=%E5%AE%A0%E7%89%A9%E5%90%B8%E6%AF%9B%E5%99%A8&enc=utf-8&suggest=2.his.0.0&wq=&pvid=4248f4265cb1489ab74d7ddb440adaef&page='+str(2*n-1)
    headers = {
        'authority': 'search.jd.com',
        'method': 'GET',
        'path': '/Search?keyword=%E5%AE%A0%E7%89%A9%E5%90%B8%E6%AF%9B%E5%99%A8&enc=utf-8&suggest=1.his.0.0&wq=&pvid=f5c2527f027a41e4ab8b690308ca4888',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'cookie': '__jdu=1598411366644899875444; shshshfpa=a05daf55-8bb5-7286-46c9-4c9b0dc4ae12-1603960121; shshshfpb=bb/gO72dmPK/OOE1sWVyJYA==; pinId=-39f8NFDZJ-QS2CarWk4ebV9-x-f3wj7; __jdv=122270672|direct|-|none|-|1637113912714; areaId=22; ipLoc-djd=22-1930-50947-0; PCSYCityID=CN_510000_510100_510107; rkv=1.0; qrsc=3; user-key=be47a5c1-51d8-423a-99b8-26ca686d3ea1; _pst=jd_66018978b8222; unick=jd_66018978b8222; pin=jd_66018978b8222; _tp=USH4gzP41CNeC1vWRqikzbU0Yv9FGAzMWOeP1PHn6bY=; unpl=V2_ZzNtbUIHREchDRUBf0sIBmJWG15LBxRAJQBFAH8bDgVmVxYNclRCFnUURlRnGlsUZwUZXkpcQRNFCEZkexhdBmEKFVxGUXMlfQAoVDYZMgYJA18QD2dAFUUIR2R7HVQMYgMSX0VQRBBwAU5cch9YAGIGIm1CUXMlRQl2VUsYbE4JAl9dRl9KEHUIRFN8HlkAbgsaVERTRhBwOEdkeA==; __jda=76161171.1598411366644899875444.1598411367.1637836264.1637918984.44; __jdb=76161171.1.1598411366644899875444|44.1637918984; __jdc=76161171; shshshfp=96b0298b06e835f7e87ee3eaefbb4f29; shshshsID=df966c0c8ccb315d277fd7b12d0c1a30_1_1637918985142; 3AB9D23F7A4B3C9B=UHWVIVNFGKLDFAHKAHZRJWGV2SXEO4BU36N3UNMZTWMQI34IZPOBPUWRYCT6BW477GTP6EDOKL5UAUE6GUW7GLHF4I',
        'referer': 'https://search.jd.com/Search?keyword=%E5%AE%A0%E7%89%A9%E5%90%B8%E6%AF%9B%E5%99%A8&enc=utf-8&suggest=1.def.0.base&wq=%E5%AE%A0%E7%89%A9%E5%90%B8&pvid=0a6d43974fab43f39a828dd3655c8cc0',      
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36}'
        }

    response = requests.get(url,headers=headers)
    response.encoding='utf-8'
    html1 = etree.HTML(response.text)      
    datas=html1.xpath('//li[contains(@class,"gl-item")]') 

    with open('goods.csv',mode='a',encoding='utf_8_sig',newline='') as info:
        csv_wirter=csv.writer(info)

        for data in datas:
            goods_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
            goods_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()[1]')
            goods_name_type = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()[2]')
            good_info = goods_name + goods_name_type
            imgs_item = data.xpath('div/div[@class="p-img"]/a/img/@data-lazy-img')
            goods_img = ('https:'+imgs_item[0])       
           
            csv_wirter.writerow([good_info,goods_price,goods_img])


def after_thirty(n):
    
    url = 'https://search.jd.com/Search?keyword=%E5%AE%A0%E7%89%A9%E5%90%B8%E6%AF%9B%E5%99%A8&enc=utf-8&suggest=2.his.0.0&wq=&pvid=4248f4265cb1489ab74d7ddb440adaef&page='+str(2*n)+'&s='+str(30)+'&scrolling=y'
    headers = {
        'authority': 'search.jd.com',
        'method': 'GET',
        'path': '/s_new.php?keyword=%E5%AE%A0%E7%89%A9%E5%90%B8%E6%AF%9B%E5%99%A8&qrst=1&stock=1&pvid=bc053c98bf0e479393876aa52a8bedda&page=2&s=30&scrolling=y&log_id=1638501501914.1839&tpl=1_M&isList=0',       
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',       
        'cookie': '__jdu=1598411366644899875444; shshshfpa=a05daf55-8bb5-7286-46c9-4c9b0dc4ae12-1603960121; shshshfpb=bb/gO72dmPK/OOE1sWVyJYA==; pinId=-39f8NFDZJ-QS2CarWk4ebV9-x-f3wj7; rkv=1.0; qrsc=3; user-key=be47a5c1-51d8-423a-99b8-26ca686d3ea1; _pst=jd_66018978b8222; unick=jd_66018978b8222; pin=jd_66018978b8222; _tp=USH4gzP41CNeC1vWRqikzbU0Yv9FGAzMWOeP1PHn6bY=; unpl=V2_ZzNtbRZQFxMnDEBWKRALUmJWQlsRXhMUJQpEB3sfWAFgAEZZclRCFnUURlRnGlsUZwoZXEJcQBZFCEZkexhdBmEKFVxGUXMlfQAoVDYZMgYJA18QD2dAFUUIR2R7HVQMYgMSX0VQRBBwAU5cch9YAGIGIm1CUXMlRQl2VUsYbE4JAl9dRl9KEHUIRFN8HlkAbgsaVERTRhBwOEdkeA==; __jdc=122270672; areaId=22; ipLoc-djd=22-1930-50947-0; __jdv=122270672|direct|-|none|-|1638439860256; shshshfp=6f07c4ea56031652b42ead9e2b6a32e6; __jda=122270672.1598411366644899875444.1598411367.1638439860.1638501515.47; __jdb=122270672.1.1598411366644899875444|47.1638501515; shshshsID=6009c82e476a4910ecb9e5ff6c6824ee_1_1638501514923; 3AB9D23F7A4B3C9B=J7KVNK5L5FSE5DIJRY7RQUHQ34TUXLB6PZJZFPCSER5KE5KSXDHFFMTBUKBOAUECWV6MXK2FGQANNXIJJB6RQE7LUE',
        'referer': 'https://search.jd.com/Search?keyword=%E5%AE%A0%E7%89%A9%E5%90%B8%E6%AF%9B%E5%99%A8&enc=utf-8&pvid=bc053c98bf0e479393876aa52a8bedda',   
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36}'
        }

    response = requests.get(url,headers=headers)
    response.encoding='utf-8'
    html1 = etree.HTML(response.text)
        
    datas=html1.xpath('//li[contains(@class,"gl-item")]') 

    with open('goods.csv',mode='a',encoding='utf_8_sig',newline='') as info:
        csv_wirter=csv.writer(info)
        
        for data in datas:
            goods_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
            goods_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()[1]')
            goods_name_type = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()[2]')
            good_info = goods_name + goods_name_type
            imgs_item = data.xpath('div/div[@class="p-img"]/a/img/@data-lazy-img')
            goods_img = ('https:'+imgs_item[0])       
           
            csv_wirter.writerow([good_info,goods_price,goods_img])

if __name__ == '__main__':
    
    for n in range(1,11):
              
        print('-----✅✅✅✅-----正在抓取第'+ str(n) +'页前30条数据------✅✅✅✅-----')
        top_thirty(n)
        print('-----✅✅✅✅-----正在抓取第'+ str(n) +'页后30条数据------✅✅✅✅-----')
        after_thirty(n)
        time.sleep(1)

    

    
	

















        
