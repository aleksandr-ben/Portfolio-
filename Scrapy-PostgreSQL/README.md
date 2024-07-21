# Scrapy (python) & PostgreSQL database


The task is to scrap data from old games online database: https://myabandonware.com/ and store it in PosgreSQL db.

Scrapy techniques used:
1. Import list of pages with games from sitemap.xml.
2. For each page scrap data and store it in Scrapy Item.
3. Connect to PostgerSQL with Scrapy Pipelines and store our items in table.


The data format on page:

![Alt text](task.png?raw=true "Data format")

Table with collected data:

![Alt text](table.png?raw=true "Solution")
