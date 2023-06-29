from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

import base64
from urllib import parse
from xml.etree import ElementTree
from django.contrib.sessions.models import Session

def save_saml_user_data(saml_response_data):
    decoded_uri = parse.unquote(saml_response_data)
    response_xml = base64.b64decode(decoded_uri)
    root = ElementTree.fromstring(response_xml)
    name_id_element = root.find('.//{urn:oasis:names:tc:SAML:2.0:assertion}NameID')
    email = name_id_element.text
    
    # Check if user already exists based on email
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        # Create a new user
        user = CustomUser.objects.create(email=email)
    
    return user

class SamlBackend(ModelBackend):
    def authenticate(self, request, session_id=None):
        if session_id is not None:
            try:
                session = Session.objects.get(session_key=session_id)
                print(session.get_decoded())
                user_id = session.get_decoded().get('_auth_user_id')
                #session_index = session.get_decoded().get('samlSessionIndex')
                user = CustomUser.objects.get(id=user_id)
                return user
            except:
                pass

        return None

    def get_user(self, id):
        try:
            return CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return None

        # Example: Retrieve the session key from a custom session variable
        # session_key = custom_get_session_key(user_id)
        # if session_key:
        #     return self.CustomUser.objects.get(**{self.user_model.USERNAME_FIELD: user_id, self.user_model.SESSION_KEY_FIELD: session_key})
        # return None