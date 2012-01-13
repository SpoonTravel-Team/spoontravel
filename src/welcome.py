import webapp2
from spoons.followSpoon import FollowSpoon
from spoons.addSpoonStep import AddSpoonStep
from spoons.addNewSpoon import AddNewSpoon
from spoons.model.Spoon import SpoonImage
from spoons.model.SpoonStep import SpoonStepImage
from BaseHandler import BaseHandler

class Welcome(BaseHandler):
    
    def get(self):
        context = {'message': 'toto'}
        self.render_response('welcome.html', **context)

config = {}
config['webapp2_extras.jinja2'] = {'template_path': 'templates'}

app = webapp2.WSGIApplication([('/', Welcome),
                              ('/followSpoon',FollowSpoon),
                              ('/addSpoonStep',AddSpoonStep),
                              ('/addNewSpoon',AddNewSpoon),
                              ('/spoonImage',SpoonImage),
                              ('/spoonStepImage',SpoonStepImage)],
                              debug=True)
