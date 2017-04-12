import scrapy


class TitlesSpider(scrapy.Spider):

	name = "titles"

	start_urls = ["http://www.wykop.pl/strona/" + str(i) for i in range(1, 100)]

	
	

	def parse(self, response):
		titles = response.xpath("//div[contains(@class, 'lcontrast')]/h2/a/@title").extract()
		# print("here's what i crawled: " + str(titles))
		file = open("results.txt", "a")
		for title in titles:
			file.write(title + "\n")
		file.close()

