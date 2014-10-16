# This client is designed to easily interact with Webmetrics' API.
# Copyright (C) 2014  Shane Barbetta

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
__author__ = 'Shane Barbetta'

import urllib2
import base64
import hashlib
import time

# store the URL and signature as state

class ApiConnection:
	def __init__(self):
		self.sig = ''
		self.base_url = 'https://api.webmetrics.com/v2/?'
		
	# Authentication
	# The ability to created a signature hash value and retain it for
	# its +/- 10 minute duration, while dynamically refreshing the sig
	# once it becomes stale. If a request fails, it should try again
	# with a new auth token.
	def auth(self, username, api_key):
		timestamp = str(int(time.time()))
		self.sig = base64.b64encode(hashlib.sha1(username + api_key + timestamp).digest())
	
	def _refresh(self):
	
	def _check_sig(self):
	
	# Requests
	# Methods for accessing the API using Python's native urllib2
	# libraries. Use the auth methods to verify the stored signature 
	# and refresh if needed.
	def _do_call():