import os
import logging
import uuid
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("main_page.html")
class AboutHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("about.html")

# Projects
class ProjectsHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("projects/projects.html")

#CCH
class CCHHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("projects/cch.html")
class AnonymizersHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("projects/cch/anonymizers.html")
class ChatHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("projects/cch/chat.html")
class CurrencyHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("projects/cch/currency.html")
class MobileHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("projects/cch/mobile.html")
class RemailersHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("projects/cch/remailers.html")
class StorageHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("projects/cch/storage.html")

# More
class MoreHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("more/more.html")
class ReadingHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("more/reading.html")
class ResearchHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("more/research.html")

# Interact 
class InteractHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("interact/interact.html")
class MailingListsHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("interact/mailing_lists.html")
class InteractTimeHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("interact/time.html")
class InteractGoodsHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("interact/goods.html")
class InteractMoneyHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("interact/money.html")
		
class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", MainHandler),
			(r"/about/", AboutHandler),
			(r"/projects/", ProjectsHandler),
			
			(r"/projects/cch/", CCHHandler),
			(r"/projects/cch/anonymizers/", AnonymizersHandler),
			(r"/projects/cch/chat/", ChatHandler),
			(r"/projects/cch/currency/", CurrencyHandler),
			(r"/projects/cch/mobile/", MobileHandler),
			(r"/projects/cch/remailers/", RemailersHandler),
			(r"/projects/cch/storage/", StorageHandler),
			
			(r"/more/", MoreHandler),
			(r"/more/reading/", ReadingHandler),
			(r"/more/research/", ResearchHandler),
			
			(r"/interact/", InteractHandler),
			(r"/interact/mailing_lists/", MailingListsHandler),
			(r"/interact/time/", InteractTimeHandler),
			(r"/interact/goods/", InteractGoodsHandler),
			(r"/interact/money/", InteractMoneyHandler),
		]
		settings = dict(
			debug=True,
			template_path=os.path.join(os.path.dirname(__file__), "templates"),
			static_path=os.path.join(os.path.dirname(__file__), "static"),
		)
		tornado.web.Application.__init__(self, handlers, **settings)
if __name__ == "__main__":
	application = Application()
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
