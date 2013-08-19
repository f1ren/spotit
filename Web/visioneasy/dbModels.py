#!/usr/bin/env python

from google.appengine.ext import db

class Spot(db.Model):
  x = db.FloatProperty()
  y = db.FloatProperty()
  color = db.FloatProperty()
  timestamp = db.IntegerProperty()
