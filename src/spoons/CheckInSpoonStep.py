from BaseHandler import BaseHandler
from spoons.model.Spoon import Spoon
from spoons.model.SpoonStep import SpoonStep
from google.appengine.api.images import Image
from google.appengine.api import images, taskqueue
from google.appengine.ext import db

class CheckInSpoonStep(BaseHandler):
    
    def get(self,spoonNumber=None):
        if(spoonNumber==None):
            try:
                spoonNumber = int(self.request.get('spoonNumber'))
            except ValueError :
                context = {'error' : self.request.get('spoonNumber') + " is not a valid SpoonNumber !"}
                self.render_response('error.html', **context)
                return 
            
        spoon = Spoon.get_by_id(int(spoonNumber))
        
        context = {'spoonNumber' : spoon.spoonNumber()}
        self.render_response('CheckInSpoonStep.html', **context)
        
    def post(self):
        try:
            spoonNumber = int(self.request.get('spoonNumber'))
        except ValueError :
            context = {'error' : self.request.get('spoonNumber') + " is not a valid SpoonNumber !"}
            self.render_response('error.html', **context)
            return
        
        spoon = Spoon.get_by_id(spoonNumber)
        
        #Creating spoonStep
        spoonStep = SpoonStep()
        spoonStep.comment = self.request.get('comment')
        spoonStep.place = self.request.get('place')
        spoonStep.currentOwner = self.request.get('currentOwner')
        if self.request.get('email') :
            spoonStep.email = self.request.get('email')
        spoonStep.spoon = spoon
        picture = self.request.get('img')
        if picture :
            resizedPicture = picture
            if Image(picture).width > 620 or Image(picture).height > 400:
                resizedPicture = images.resize(picture, 620, 400)
            spoonStep.image_blob = db.Blob(resizedPicture)
        spoonStep.put()
        
        # Add the task to the default queue.
        taskqueue.add(url='/sendMail', params={'spoonNumber': spoonNumber})
        
        self.redirect("/spoon/%s" % spoonNumber)
