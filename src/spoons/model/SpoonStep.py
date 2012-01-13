from google.appengine.ext import db
from spoons.model.Spoon import Spoon
import webapp2


class SpoonStep(db.Model):
    spoon = db.ReferenceProperty(Spoon, collection_name="spoonSteps")
    date = db.DateTimeProperty(auto_now_add=True)
    comment = db.StringProperty(multiline=True)
    place = db.PostalAddressProperty()
    email = db.EmailProperty()
    image_blob = db.BlobProperty()
    
class SpoonStepImage(webapp2.RequestHandler):
    def get(self):
        spoonStep = db.get(self.request.get("img_id"))
        if spoonStep.image_blob:
            self.response.headers['Content-Type'] = "image/png"
            self.response.out.write(spoonStep.image_blob)
        else:
            self.response.out.write("No image")