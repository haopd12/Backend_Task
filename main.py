
try:
    import os
    import argparse
    from JsonScrapper.Novel_Scrapper import NovelScrapper
    from JsonScrapper.config import Config
    import sqlite3
    from Import_to_Db import Insert_to_Belonged_to, Insert_to_Novel_Chapter, Insert_to_Novel_Info
    from JsonScrapper.Novel_Scrapper import write_json
except Exception as e:
    print("Caught exception while importing: {}".format(e))
    
    

if __name__ == '__main__':
    parser= argparse.ArgumentParser(description="")
    parser.add_argument('--dir', help='output dir', default='Output', type=str)
    parser.add_argument('--file', help='output file', default='crawl_data', type=str)
    args = parser.parse_args()
    print("Start crawling...")
    print(args)
    
    current_path = os.getcwd()
    save_dir = current_path + '/' + args.dir
    
    configs = Config(save_dir= save_dir, save_file= args.file)
    crawler = NovelScrapper(configs)
    crawler.novel_crawler()
#Insert to Novel_Chapter Table
    json_file="Output/crawl_data_{}.json"
    connection=sqlite3.connect("Database/database.db")
    for i in range (0,23):
        Insert_to_Novel_Chapter(json_file=json_file.format(i),connection=connection)
#Insert to Novel_Info
    datas=crawler.data_extract
    data1=[]
    for data in datas:
        ele_data={
            "Novel_Link": data
        }
        data1.append(ele_data)
    write_json(save_dir+'/'+args.file+'_novel_base.json',data1)
    Insert_to_Novel_Info(connection=connection)   
#Insert to Belonged_to
    data2=crawler.get_Belonged_to_data()
    data3=[]
    for i in range(len(datas)):
        ele_data={
            "Novel": data2[i],
            "Novel_Link": datas[i]
        }
        data3.append(ele_data)
    write_json(save_dir+'/'+args.file+'_belonged_to_base.json',data3)
    Insert_to_Belonged_to(connection=connection)
    connection.commit()
    connection.close()

    
    