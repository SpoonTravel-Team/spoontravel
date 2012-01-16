from spoons.model.Spoon import Spoon
from google.appengine.ext import db
from BaseHandler import BaseHandler

class AddNewSpoon(BaseHandler):
    
    def get(self):
        context = {}
        self.render_response('addNewSpoon.html', **context)
                
    def post(self):        
        #Creating spoon
        spoon = Spoon()
        spoon.comment = self.request.get('comment')
        picture=self.request.get('img')
        if picture :
            spoon.image_blob = db.Blob(picture)
        spoon.put()
        
        #Responding
        context = {'spoonNumber' : spoon.spoonNumber()}
        self.render_response('newSpoonAdded.html', **context)