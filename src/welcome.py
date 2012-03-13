import webapp2
from spoons.ShowSpoon import ShowSpoon
from spoons.CheckInSpoonStep import CheckInSpoonStep
from spoons.MakeMySpoonTravel import MakeMySpoonTravel
from spoons.MailSender import MailSender
from spoons.model.Spoon import SpoonImage
from spoons.model.SpoonStep import SpoonStepImage
from credits import Credits
from About import About
from BaseHandler import BaseHandler
import logging

class Welcome(BaseHandler):
    
    def get(self):
        context = {}
        self.render_response('welcome.html', **context)

config = {}
config['webapp2_extras.jinja2'] = {'template_path': 'templates'}

logging.getLogger().setLevel(logging.DEBUG)
app = webapp2.WSGIApplication([
                webapp2.Route('/', handler=Welcome, name='home'),
                webapp2.Route('/home', handler=Welcome, name='namedHome'),
                webapp2.Route('/spoon', handler=ShowSpoon, name='spoon'),
                webapp2.Route('/spoon/<spoonNumber:\d+>', handler=ShowSpoon, name='spoon'),
                webapp2.Route('/addSpoonStep', handler=CheckInSpoonStep, name='CheckInSpoonStepForm'),
                webapp2.Route('/makeMySpoonTravel', handler=MakeMySpoonTravel, name='makeMySpoonTravel'),
                webapp2.Route('/spoonImage', handler=SpoonImage, name='spoonImage'),
                webapp2.Route('/spoonStepImage', handler=SpoonStepImage, name='spoonStepImage'),
                webapp2.Route('/credits', handler=Credits, name='credits'),
                webapp2.Route('/about', handler=About, name='about'),
                webapp2.Route('/sendMail', handler=MailSender, name='sendmail')
                            ], debug=True)
