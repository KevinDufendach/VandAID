# Copyright 2013 Google, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#             http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

import webapp2

import model2

# [START urllib-imports]
import urllib
# [END urllib-imports]

# [START urlfetch-imports]
from google.appengine.api import urlfetch
# [END urlfetch-imports]

from config import config

def AsDict(guest):
    return {'id': guest.key.id(), 'first': guest.first, 'last': guest.last}

def AsDict(testfield):
    return {'id': testfield.key.id(), 'field_name': testfield.first, 'last': testfield.last}

# def AsDict(asdfjkl):
#     return {'id': asdfjkl.key.id(), 'field_name': asdfjkl.name, 'field_type': asdfjkl.type}

class RestHandler(webapp2.RequestHandler):

    def dispatch(self):
        # time.sleep(1)
        super(RestHandler, self).dispatch()

    def SendJson(self, r):
        self.response.headers['content-type'] = 'text/plain'
        self.response.write(json.dumps(r))

class RedcapPostHandler(RestHandler):
    
    def get(self):
        url = config['api_url']
        
        form_fields = {
            'token' : config['api_token'],
            'content' : 'metadata',
            'format' : 'json',
            'returnFormat' : 'json'
        }
        
        try:
            form_data = urllib.urlencode(form_fields)
            headers = {'Content-Type': 'application/x-www-form-urlencoded',
                       'Accept' : 'application/json'}
            result = urlfetch.fetch(
                url=url,
                payload=form_data,
                method=urlfetch.POST,
                headers=headers)
            self.response.write(result.content)
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

class QueryHandler(RestHandler):

    def get(self):
        guests = model2.AllGuests()
        r = [AsDict(guest) for guest in guests]
        self.SendJson(r)


class UpdateHandler(RestHandler):

    def post(self):
        r = json.loads(self.request.body)
        guest = model2.UpdateGuest(r['id'], r['first'], r['last'])
        r = AsDict(guest)
        self.SendJson(r)


class InsertHandler(RestHandler):

    def post(self):
        r = json.loads(self.request.body)
        guest = model2.InsertGuest(r['first'], r['last'])
        r = AsDict(guest)
        self.SendJson(r)


class DeleteHandler(RestHandler):

    def post(self):
        r = json.loads(self.request.body)
        model.DeleteGuest(r['id'])


APP = webapp2.WSGIApplication([
    ('/rest/query', QueryHandler),
    ('/rest/insert', InsertHandler),
    ('/rest/delete', DeleteHandler),
    ('/rest/update', UpdateHandler),
    ('/rest/redcap-metadata', RedcapPostHandler),
], debug=True)