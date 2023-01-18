# About the project

This project demonstrate the usage of scrapy framework to scrape a demo website whose domain is books.toscrape.com and export the data collected to a csv or json file.

In scrapy there are multiple spider templates. In this project I used two templates "basic" and "crawl".

# prerequisites

1. python installed preferably in a virtual environment.
2. you can install all the requirements using this command `pip install -r requirements.txt`

# usage

1. download the repository or clone it locally.
2. from the terminal `cd` into the project folder.
3. make sure you have installed python and the requirements.
4. you can crawl the website using the following commands.  
- basic template  
`scrapy crawl books_spider_basic -o basic_spider.csv`
- crawl template  
`scrapy crawl books_spider_crawl -o crawl_spider.csv`  

5. you will find the file which has the name you specified after `-o` in the project folder.
6. you may use csv or json format.
