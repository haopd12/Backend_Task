import sqlite3
from JsonScrapper.Novel_Scrapper import read_json

def Insert_to_Novel_Chapter(json_file="",connection=""):
    cursor=connection.cursor()
    json_obj=read_json(json_file)
    columns=['Novel','Page','Page_Link']
    for row in json_obj:
        keys=tuple(row[c] for c in columns)
        cursor.execute("insert into Novel_Chapter values(?,?,?)",keys) 
    
def Insert_to_Novel_Info(json_file="Output/crawl_data_novel_base.json",connection=""):
    cursor=connection.cursor()
    json_obj=read_json(json_file)
    columns=['Novel_Link']
    for row in json_obj:
        key=tuple(row[c] for c in columns)
        cursor.execute("insert into Novel_Info values(?)",key) 

def Insert_to_Belonged_to(json_file="Output/crawl_data_belonged_to_base.json",connection=""):
    cursor=connection.cursor()
    json_obj=read_json(json_file)
    columns=['Novel','Novel_Link']
    for row in json_obj:
        keys=tuple(row[c] for c in columns)
        cursor.execute("insert into Belonged_to values(?,?)",keys) 
        

    