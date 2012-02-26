from spoons.model.Spoon import Spoon
from BaseHandler import BaseHandler

class TrackSpoon(BaseHandler):
            
    def get(self):
        try:
            spoonNumber = int(self.request.get('spoonNumber'))
        except ValueError :
            context = {'error' : self.request.get('spoonNumber')+" is not a valid SpoonNumber !"}
            self.render_response('error.html', **context)
            return 
        
        spoon = Spoon.get_by_id(spoonNumber)
                
        context = {'spoonNumber' : spoon.spoonNumber(),
                   'spoonKey': spoon.key(),
                   'comment': spoon.comment,
                   'creationDate': spoon.creationDate,
                   'spoonSteps' : spoon.spoonSteps,
                   'spoonStepsAvailable' : True}
        self.render_response('trackSpoon.html', **context)
        