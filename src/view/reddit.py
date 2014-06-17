'''
Created on Jun 15, 2014

@author: kkantor
'''
from model import agent

import os

import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)

DEFAULT_SUB = '/cscareerequestions'
DEFAULT_SECTION = 'hot'

class MainPage(webapp2.RequestHandler):
    '''
    classdocs
    '''
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())
    
class GetReddit(webapp2.RequestHandler):
    def post(self):
        sub = self.request.get('subreddit', default_value=DEFAULT_SUB)
        section = self.request.get('section', default_value=DEFAULT_SECTION)
        
        
        template = JINJA_ENVIRONMENT.get_template('index.html')
        
        runner = agent.Agent(subreddit=sub)
        resp = runner.retrieve(section)
        
        template_values = {
                'content': resp,
                'section': section
                }
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sub', GetReddit),
], debug=True)