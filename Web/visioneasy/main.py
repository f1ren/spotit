#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from django.utils import simplejson as json

import webapp2
import logging

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Hello world!")

class SpotsLister(webapp2.RequestHandler):
    def get(self):
        # TODO Get last timestamp from user
        # TODO Delete old clicks (older than 1 minute)
        # TODO Get spots and image for user (by logon information)
        my_response = [(100,100)]
        result = json.dumps(my_response)

        self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
        self.response.out.write(result)

class SpotsAdder(webapp2.RequestHandler):
    def post(self):
        # TODO get spot from request
        #  cords
        #  color
        # TODO add spot to list
        logging.info(self.request.get("x"))
        logging.info(self.request.get("y"))
        logging.info(self.request.get("color"))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/getSpots', SpotsLister),
    ('/addSpot', SpotsAdder),
], debug=True)
