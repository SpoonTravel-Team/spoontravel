from spoons.model.Spoon import Spoon
from BaseHandler import BaseHandler

class FollowSpoon(BaseHandler):
    
    def post(self):
        self.get(self)
        
    def get(self):
        try:
            spoonNumber = int(self.request.get('spoonNumber'))
        except ValueError :
            context = {'error' : self.request.get('spoonNumber')+" is not a number !"}
            self.render_response('error.html', **context)
            return 
        
        spoon = Spoon.get_by_id(spoonNumber)
                
        context = {'spoonNumber' : spoon.spoonNumber(),
                   'spoonKey': spoon.key(),
                   'comment': spoon.comment,
                   'creationDate': spoon.creationDate,
                   'spoonSteps' : spoon.spoonSteps,
                   'spoonStepsAvailable' : True}
        self.render_response('followSpoon.html', **context)
        