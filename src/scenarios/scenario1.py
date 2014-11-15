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

import sys, json, csv
sys.path.insert(0, '../')
import wm_api_client

if len(sys.argv) != 3 and len(sys.argv) != 4:
    raise Exception('Expected use: python scenario1.py username api_key [filename.csv]')

"""The purpose of this scenario is to query and display all alert
contacts in a given account using the following.

Arguments:
username -- The username of the Webmetrics account for which alert
            contacts are to be queried.
api_key -- The Webmetrics API key for the account.
filename -- Optional: The name of the file to which the data is to
            saved.

"""
	
username = sys.argv[1]
api_key = sys.argv[2]
save_file = False

if len(sys.argv) == 4:
    if sys.argv[3][-4:] == '.csv':
        save_file = True
        file = csv.writer(open(sys.argv[3], "wb"))
        file.writerow(['Monitor Name', 'Service ID', 'Level 1 Escalation', 'Level 2 Escalation', 'Level 3 Escalation', 'Diagnostic Contact'])
    else:
        raise Exception('File name must end in .csv')

c = wm_api_client.ApiClient(username, api_key)

account_data = c.get_services()

for service in account_data['service']:
    name = json.dumps(service['name'])[2:-2]
    id = json.dumps(service['id'])[2:-2]
    if save_file == True:
        level1 = ''
        level2 = ''
        level3 = ''
        diagnostic = ''

    print '------------------------------------------------------------>'
    print 'monitor_name ::: %s' % name
    print 'service_id ::: %s' % id
    print 'alert_contacts :::'

    service_contacts = c.get_all_alerting_contacts(id)

    print '\tlevel1 ::: '
    i = 1
    length = len(service_contacts['level1']['contact'])
    for contact in service_contacts['level1']['contact']:
        if contact is not None:
            contact = contact.rstrip()
        else:
            continue
        if contact:
            print '\t\t%s' % contact
            if save_file == True:
                if i == length:
                    level1 += contact
                else:
                    level1 += contact + '\n'
        i = i + 1
        
    print '\tlevel2 ::: '
    i = 1
    length = len(service_contacts['level2']['contact'])
    for contact in service_contacts['level2']['contact']:
        if contact is not None:
            contact = contact.rstrip()
        else:
            continue
        if contact:
            print '\t\t%s' % contact
            if save_file == True:
                if i == length:
                    level2 += contact
                else:
                    level2 += contact + '\n'
        i = i + 1
        
    print '\tlevel3 ::: '
    i = 1
    length = len(service_contacts['level3']['contact'])
    for contact in service_contacts['level3']['contact']:
        if contact is not None:
            contact = contact.rstrip()
        else:
            continue
        if contact:
            print '\t\t%s' % contact
            if save_file == True:
                if i == length:
                    level3 += contact
                else:
                    level3 += contact + '\n'
        i = i + 1
        
    print '\tdiagnostic ::: '
    i = 1
    length = len(service_contacts['diagnostic']['contact'])
    for contact in service_contacts['diagnostic']['contact']:
        if contact is not None:
            contact = contact.rstrip()
        else:
            continue
        if contact:
            print '\t\t%s' % contact
            if save_file == True:
                if i == length:
                    diagnostic += contact
                else:
                    diagnostic += contact + '\n'
        i = i + 1

    if save_file == True:
        file.writerow([name, id, level1, level2, level3, diagnostic])