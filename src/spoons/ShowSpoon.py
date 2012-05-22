from spoons.model.Spoon import Spoon
from BaseHandler import BaseHandler

class ShowSpoon(BaseHandler):
            
    def get(self, spoonNumber=None):
        if(spoonNumber==None):
            try:
                spoonNumber = int(self.request.get('spoonNumber'))
            except ValueError :
                context = {'error' : "You need to send a valid SpoonNumber !"}
                self.render_response('error.html', **context)
                return 
        
        spoon = Spoon.get_by_id(int(spoonNumber))
        
        if(spoon is None):
            context = {'error' : " This spoon does not exists!"}
            self.render_response('error.html', **context)
            return
            
        context = {'spoonNumber' : spoon.spoonNumber(),
                   'spoonKey': spoon.key(),
                   'comment': spoon.comment,
                   'creationDate': spoon.creationDate,
                   'spoonSteps' : spoon.spoonSteps,
                   'stepsCount': spoon.spoonSteps.count()}
        self.render_response('showSpoon.html', **context)
        