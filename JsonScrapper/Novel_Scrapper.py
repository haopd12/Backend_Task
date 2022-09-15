try:
    from bs4 import BeautifulSoup
    import requests
    import bs4
    import os
    import json
    import traceback
except Exception as e:
    print('Caught exception while importing: {}'.format(e))
    
def make_dir(output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
def write_json(filename,data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4,ensure_ascii=False)

def read_json(filename):    
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print('Error loading {}'.format(filename), e)
        traceback.print_exc()
        return []
def request_url(url):
    session= requests.Session()
    header ={"User-Agent" : 
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                "Accept" : "text/html,application/xhtml+xml,application/xml;\
                q=0.9,image/webp,image/apng,*/*;q=0.8"}
    response = session.get(url, headers=header)
    soup=BeautifulSoup(response.text,"html.parser")
    return soup
class NovelScrapper:
    def __init__(self, config):
        self.config = config
    @property
    def data_extract(self):
        url1=self.config.SEARCH_URL
        soup=request_url(url1)
        elements=soup.select('div.list-novel')
        ele1=elements[0].select('div')
        data1=[]
        i=0
        for ele in ele1:
            try:   
                link=ele.select("a")
                if len(link)>0:
                    i+=1
                    novel_link=link[0]["href"]
                    if i%2==0:
                        data1.append(novel_link)
            except Exception as e:
                print("Error: ", e)
                traceback.print_exc()
        return data1
    
    def crawl_info(self, url="https://allnovel.net/p-s-i-still-love-you-to-all-the-boys-i-ve-loved-before-2.html"):
        soup=request_url(url)
        elements=soup.select("section.content")
        ele1=elements[0].select("div")[0].select("div")[0].select("div")[0].select("div")
        ele0=elements[0].select("div.detail-novel")[0].select("div.col-sm-12")
        text=(ele0[0].select("h1"))[0].getText()
        text=text.replace("#","")
        text=text.replace("'","")
        ele3=ele1[0].select("div.list-page-novel")
        ele4=ele3[0].select("table")[0].select("tbody")[0].select("tr")
        data=[]
        for ele in ele4:
            novel_page=ele.select("td")[1].select("a")[0]
            page_link=novel_page["href"]
            page=novel_page["title"]
            page=page.replace("Read ","")
            ele_data={
                "Novel":text,
                "Page":page,
                "Page_Link":page_link
            }
            data.append(ele_data)
        return data
    def novel_crawler(self):
        datas=self.data_extract
        # print(data)
        save_dir=self.config.save_dir
        save_file=self.config.save_file
        make_dir(save_dir)
        for i in range(len(datas)):
            filename=save_file+'_{}.json'.format(i)
            write_json(save_dir+'/'+filename,self.crawl_info(url="https://allnovel.net{}".format(datas[i])))
            
    def get_Belonged_to_data(self):
        url1=self.config.SEARCH_URL
        soup=request_url(url1)
        elements=soup.select('div.list-novel')
        ele1=elements[0].select('div')
        data1=[]
        i=0
        for ele in ele1:
            try:   
                link=ele.select("div.title-home-novel")
                if len(link)>0:
                    i+=1
                    novel_name=link[0].getText()
                    
                    if i%2==0:
                        novel_name=novel_name.replace("'","")
                        novel_name=novel_name.replace("#","")
                        # print(novel_name)
                        data1.append(novel_name)
            except Exception as e:
                print("Error: ", e)
                traceback.print_exc()
        return data1
            