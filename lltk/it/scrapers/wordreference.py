#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from lxml import html
from collections import Counter

from ...scraping import Scraper

class WordreferenceIt(Scraper):

	def __init__(self, word):
		super(WordreferenceIt, self).__init__( word)
		self.name = 'Wordreference.com'
		self.url = 'http://www.wordreference.com/iten/%s' % self.word
		self.baseurl = 'http://wordreference.com'
		self.language = 'it'

	def download(self):
		super(WordreferenceIt, self).download()
#		if len(self.tree.xpath('//span[@class="noThreads"]')) or len(self.tree.xpath('//p[@id="noEntryFound"]')):
#			# There are no result. This is most likely not a proper word

	@Scraper.needs_download
	def gender(self):
		''' Try to scrape the correct gender for a given word from wordreference.com '''

		elements = self.tree.xpath('//table[@class="WRD"]')
		if len(elements):
			elements = self.tree.xpath('//table[@class="WRD"]')[0]
			if len(elements):
				if '/iten/' in self.page.url:
					elements = elements.xpath('//td[@class="FrWrd"]/em[@class="POS2"]/text()')
				elif '/enit/' in self.page.url:
					elements = elements.xpath('//td[@class="ToWrd"]/em[@class="POS2"]/text()')
				else:
					return [None]
				element = [element[1:] for element in elements if element in ['nm', 'nf']]
				counter = Counter(element)
				if len(counter.most_common(1)):
					result = counter.most_common(1)[0][0]
					return [result]
		return [None]