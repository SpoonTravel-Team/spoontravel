import webapp2
from spoons.TrackSpoon import TrackSpoon
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
app = webapp2.WSGIApplication([('/', Welcome),
                              ('/trackSpoon',TrackSpoon),
                              ('/addSpoonStep',CheckInSpoonStep),
                              ('/makeMySpoonTravel',MakeMySpoonTravel),
                              ('/spoonImage',SpoonImage),
                              ('/spoonStepImage',SpoonStepImage),
                              ('/credits',Credits),
                              ('/about',About),
                              ('/sendMail',MailSender)],
                              debug=True)
