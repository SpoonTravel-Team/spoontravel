from BaseHandler import BaseHandler
from spoons.model.Spoon import Spoon

class AddSpoonStep(BaseHandler):
    
    def post(self):
        spoonNumber = int(self.request.get('spoonNumber'))
        spoon = Spoon.get_by_id(spoonNumber)
        context = {'spoonNumber' : spoon.spoonNumber()}
        self.render_response('addSpoonStep.html', **context)