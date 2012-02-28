from spoons.model.Spoon import Spoon
from BaseHandler import BaseHandler

class TrackSpoon(BaseHandler):
            
    def get(self, spoonNumber=None):
        if(spoonNumber!=None):
            try:
                spoonNumber = int(self.request.get('spoonNumber'))
            except ValueError :
                spoonNumber=None
                
        if(spoonNumber==None):
            context = {'error' : "You need to send a valid SpoonNumber !"}
            self.render_response('error.html', **context)
            return 
        
        spoon = Spoon.get_by_id(spoonNumber)
                
        context = {'spoonNumber' : spoon.spoonNumber(),
                   'spoonKey': spoon.key(),
                   'comment': spoon.comment,
                   'creationDate': spoon.creationDate,
                   'spoonSteps' : spoon.spoonSteps,
                   'spoonStepsAvailable' : True}
        self.render_response('showSpoon.html', **context)
        