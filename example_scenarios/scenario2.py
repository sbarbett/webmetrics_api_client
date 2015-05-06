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

import csv, webmetrics_api_client, json, sys, time

if len(sys.argv) == 2 and sys.argv[1].lower() == "help":
    sys.exit("Expected use: python list_services.py username api_key\n\nArgument 1:\n\tlist_services.py -- The name of your python file\nArgument 2:\n\tusername -- Username of the Webmetrics account\nArgument 3:\n\tapi_key -- Webmetrics account API key\n")
    
if len(sys.argv) != 3:
    raise Exception("Expected use: python list_services.py username api_key\n\nType 'python list_services.py help' for more information.\n")

"""This script will query all services in an account and list
monitored url for each. Only works for site monitors. Output
is saved to a timestamped CSV file within the directory the
script is ran.

Arguments:
username -- The username of the Webmetrics account.
api_key -- The account's api_key.

"""

username = sys.argv[1]
api_key = sys.argv[2]
  
# Establish an API connection
c = webmetrics_api_client.ApiClient(username, api_key)
        
output_file = "results_" + str(int(time.time())) + ".csv"
with open(output_file, "wb") as csv_output:
    # Set output CSV headers
    writer = csv.DictWriter(csv_output, fieldnames=['Service name', 'Service ID', 'Monitored url'])
    writer.writeheader()

    # Get all services in account
    get_services_response = c.get_services()
    print json.dumps(get_services_response)
    if get_services_response['stat'] is "fail":
        raise Exception(get_service_response['errror'][0]['msg'])
        
    # Iterate through services
    for service in get_services_response['service']:
        # Set variables
        service_id = service['id'][0]
        service_name = service['name'][0]
        service_monitoring_url = None
        
        # Get the monitoring url
        get_monitoring_url_response = c.get_monitoring_url(service_id)
        print json.dumps(get_monitoring_url_response)
        if get_monitoring_url_response['stat'] == "fail":
            service_monitoring_url = get_monitoring_url_response['error'][0]['msg']
        else:
            service_monitoring_url = get_monitoring_url_response['url'][0]
            
        # Write results to CSV
        writer.writerow({'Service name': service_name, 'Service ID': service_id, 'Monitored url': service_monitoring_url})
        
    # Close file
    print "Script complete. Saving results to %s" % output_file
    csv_output.close()