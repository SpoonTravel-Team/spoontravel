import webapp2
import logging
from spoons.model.Spoon import Spoon
from google.appengine.api import mail
from spoons.model.SpoonStep import SpoonStep

class MailSender(webapp2.RequestHandler):
    '''
    Sends mails
    '''

    def post(self):
        try:
            spoonNumber = int(self.request.get('spoonNumber'))
        except ValueError :
            logging.error("MailSender : %s is not a valid SpoonNumber (not a number)" % self.request.get('spoonNumber'))
            self.error("500")
            return
               
        spoon = Spoon.get_by_id(spoonNumber)
        users_address = []
        
        for spoonStep in spoon.spoonSteps:
            if spoonStep.email is not None :
                users_address.append(str(spoonStep.email))
                 
        #@todo:  Gérer le host
        followTheSpoonUrl = "thespoontravel.appspot.com/followSpoon?spoonNumber=%s" % spoonNumber
        email = mail.EmailMessage()
        email.sender = "maxime.werlen@gmail.com"
        logging.info("sender : %s" % email.sender)
        email.to = ", ".join(users_address)
        logging.info("to : %s" % email.to)
        email.subject = "A small step for spoon a giant leap for SpoonTravel"
        email.body = """"Hi dude,
        One of your former spoon has reached a new step. Look out at <a href="%s">The Spoon travel</a> to get news about it :
        
        See you soon
        
        TheSpoonTravel team
        """ % followTheSpoonUrl
        
        email.Send()
        