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

class ProjectsHandler(tornado.web.RequestHandler):


	def get(self):
		self.render("projects.html")




class Application(tornado.web.Application):


	def __init__(self):
		handlers = [
			(r"/", MainHandler),
			(r"/about/", AboutHandler),
			(r"/projects/", ProjectsHandler),
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
