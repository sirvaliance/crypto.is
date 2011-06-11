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

class MembersHandler(tornado.web.RequestHandler):


	def get(self):
		self.render("members.html")


class ProjectsHandler(tornado.web.RequestHandler):


	def get(self):
		self.render("projects/projects.html")

class DocumentationHandler(tornado.web.RequestHandler):


	def get(self):
		self.render("documentation/documentation.html")


class TutorialsHandler(tornado.web.RequestHandler):


	def get(self):
		self.render("documentation/tutorials.html")

class ResearchHandler(tornado.web.RequestHandler):


	def get(self):
		self.render("documentation/research.html")

class ServerHandler(tornado.web.RequestHandler):


	def get(self):
		self.render("documentation/server.html")




class ServicesHandler(tornado.web.RequestHandler):


	def get(self):
		self.render("services/services.html")


class DonateHandler(tornado.web.RequestHandler):


	def get(self):
		self.render("services/donate.html")


class MailingHandler(tornado.web.RequestHandler):

	def get(self):
		self.render("services/mailing_lists.html")


class NewsHandler(tornado.web.RequestHandler):

	def get(self):
		self.render("services/news.html")


class ServersHandler(tornado.web.RequestHandler):

	def get(self):
		self.render("services/servers.html")


class StatsHandler(tornado.web.RequestHandler):

	def get(self):
		self.render("services/statistics.html")




class Application(tornado.web.Application):


	def __init__(self):
		handlers = [
			(r"/", MainHandler),
			(r"/about/", AboutHandler),
			(r"/members/", MembersHandler),
			(r"/projects/", ProjectsHandler),
			(r"/documentation/", DocumentationHandler),
			(r"/documentation/tutorials/", TutorialsHandler),
			(r"/documentation/research/", ResearchHandler),
			(r"/documentation/server/", ServerHandler),
			(r"/services/", ServicesHandler),
			(r"/services/donate/", DonateHandler),
			(r"/services/mailing_lists/", MailingHandler),
			(r"/services/news/", NewsHandler),
			(r"/services/servers/", ServersHandler),
			(r"/services/statistics/", StatsHandler),
		]

		settings = dict(
			template_path=os.path.join(os.path.dirname(__file__), "templates"),
			static_path=os.path.join(os.path.dirname(__file__), "static"),
		)
		tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
	application = Application()
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
