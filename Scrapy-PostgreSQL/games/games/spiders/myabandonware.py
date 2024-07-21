import re
import xml.etree.ElementTree as ET

import scrapy
from scrapy.loader import ItemLoader
from games.items import GamesItem


class GamesSpider(scrapy.Spider):
	name = 'gamescrap'

	def start_requests(self):
		tree = ET.parse('sitemap.xml')
		root = tree.getroot()
		for game in root[1:]:
			link = game.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
			yield scrapy.Request(url = link.text, callback = self.parse)

	def parse(self, response):
		game = ItemLoader(item = GamesItem())

		game.add_value('url', response.url)

		title = response.css('div.box h2::text').get()
		game.add_value('title', title)

		rating = response.css('div#grRaB span::text').get()
		game.add_value('rating', rating)

		tableInfo = response.css('table.gameInfo')[0]
		for tr in tableInfo.css('tr')[:]:
			field = tr.css('th::text').get()
			value = tr.css('td').get()

			if 'Alt names' in field:
				field = 'alt_name'
			elif 'Year' in field:
				field = 'year'
			elif 'Platform' in field:
				field = 'platform'
			elif 'Released' in field:
				field = 'released_in' 
			elif 'Genre' in field:
				field = 'genre'
			elif 'Theme' in field:
				field = 'theme'
			elif 'Publisher' in field:
				field = 'publisher'
			elif 'Developer' in field:
				field = 'developer'
			elif 'Perspectives' in field:
				field = 'perspectives'
			else: 
				continue
			game.add_value(field, value)

		return game.load_item()
