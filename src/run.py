

from scrapy.crawler import CrawlerProcess

from src.main import Spider

hi=Spider()

Spider.user=input("What is your K number ?")
#get K number
Spider.passw=input("and your password?")
#get password





#get crweler to work
process = CrawlerProcess()
process.crawl(hi)
process.start()



print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for i in Spider.getList(Spider):
    print("\b"+"\b"+ i )
    print("|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")

print()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")