import webapp2
from spoons.model.Spoon import Spoon

class FollowSpoon(webapp2.RequestHandler):
    
    def post(self):
        spoonNumber = int(self.request.get('spoonNumber'))
        spoon = Spoon.get_by_id(spoonNumber)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('<h1><center>Following spoon %s</center></h1><br\>' % spoon.spoonNumber())
        self.response.out.write("<div><img src='/spoonImage?img_id=%s'></img></div><br/>" % spoon.key())
        self.response.out.write("<div>Comment: %s</div><br/>" % spoon.comment)
        self.response.out.write("<div>Creation Date: %s</div><br/>" % spoon.creationDate)
        