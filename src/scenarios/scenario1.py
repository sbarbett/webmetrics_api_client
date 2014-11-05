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

import sys
sys.path.insert(0, '../')
import wm_api_client
import json

if len(sys.argv) != 3:
	raise Exception('Expected use: python sample.py username api_key')
	
username = sys.argv[1]
api_key = sys.argv[2]

c = wm_api_client.ApiClient(username, api_key)

'''The purpose of this scenario is to query and display all alert
contacts in a given account using the following.

-- Use get_services to obtain of service_ids
-- Query each individual service_id using get_all_alerting_contacts
   and parse out the data to make it readable.

'''
account_data = json.loads(c.get_services())

for service in account_data['service']:
	print '------------------------------------------------------------>'
	print 'monitor_name ::: %s' % json.dumps(service['name'])
	print 'service_id ::: %s' % json.dumps(service['id'])
	print 'alert_contacts :::'
	
	service_contacts = json.loads(c.get_all_alerting_contacts(json.dumps(service['id'])[2:-2]))
	
	print '\tlevel1 ::: '
	for contact in service_contacts['level1']['contact']:
		print '\t\t%s' % json.dumps(contact)
		
	print '\tlevel2 ::: '
	for contact in service_contacts['level2']['contact']:
		print '\t\t%s' % json.dumps(contact)
		
	print '\tlevel3 ::: '
	for contact in service_contacts['level3']['contact']:
		print '\t\t%s' % json.dumps(contact)
		
	print '\tdiagnostic ::: '
	for contact in service_contacts['diagnostic']['contact']:
		print '\t\t%s' % json.dumps(contact)