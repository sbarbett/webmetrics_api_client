# This client is designed to easily interact with Webmetrics' API.
# Copyright (C) 2014  Shane Barbetta
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
__author__ = 'Shane Barbetta'

import wm_api_client
import sys

if len(sys.argv) != 3:
	raise Exception('Expected use: python sample.py username api_key')
	
username = sys.argv[1]
api_key = sys.argv[2]

c = wm_api_client.ApiClient(username, api_key)

print 'get services %s ' % c.get_services()
print 'set notepad %s' % c.set_notepad('A string of text to test the notepad')
print 'get notepad %s ' % c.get_notepad()
print 'get service type %s ' % c.get_service_type('260726')
print 'add new service %s ' % c.add_new_service('test_mc_test_service', 'PING')
print 'reset service %s ' % c.reset_service('260723')