from spoons.model.Spoon import Spoon
from google.appengine.api import images
from google.appengine.ext import db
from BaseHandler import BaseHandler
from google.appengine.api.images import Image

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
            resizedPicture = picture
            if Image(picture).width>620 or Image(picture).height>400:
                resizedPicture = images.resize(picture, 620, 400)
            spoon.image_blob = db.Blob(resizedPicture)
        spoon.put()
        
        #Responding
        context = {'spoonNumber' : spoon.spoonNumber()}
        self.render_response('newSpoonAdded.html', **context)