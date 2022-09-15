# **CRAWL DATA FROM ALLNOVEL**

## Requirements

        Python 3+
        Python "Beautiful Soup" library
        Crawl Data about Novel
        Insert Data into Database

## How to work
        Crawl_Data has saved in .\Novel_Crawl_2\Output
        list all data in crawl_data.json
        list data following novel i in crawl_data_page_i.json
        list all data has been inserted to .\Novel_Crawl_2\Database\database.db
## About Database 
        Novel_Info(#Novel_Link)
        Novel_Chapter(#Novel, #Page, Page_Link)
        Belonged_to(Novel, Novel_Link)