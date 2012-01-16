from spoons.model.Spoon import Spoon
from BaseHandler import BaseHandler

class FollowSpoon(BaseHandler):
    
    def post(self):
        spoonNumber = int(self.request.get('spoonNumber'))
        spoon = Spoon.get_by_id(spoonNumber)
        
        context = {'spoonNumber' : spoon.spoonNumber(),
                   'spoonKey': spoon.key(),
                   'comment': spoon.comment,
                   'creationDate': spoon.creationDate}
        self.render_response('followSpoon.html', **context)
        