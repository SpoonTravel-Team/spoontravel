from spoons.model.Spoon import Spoon
from BaseHandler import BaseHandler

class TrackSpoon(BaseHandler):
            
    def get(self):
        context = {'error' : "Not done yet!"}
        self.render_response('error.html', **context)
        