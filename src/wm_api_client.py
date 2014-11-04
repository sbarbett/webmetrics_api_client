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

import connection
import json

# client containing different API services

class ApiClient:
	def __init__(self, username, api_key):
		"""Initialize Webmetrics' API Client.
		
		Arguments:
		username -- The username of the user
		api_key -- The API key of the user
		
		"""
		self.api_connection = connection.ApiConnection()
		self.api_connection.auth(username, api_key)
		
	# General
	# get account services
	def get_services(self):
		"""Get a list of service names and ids for an account."""
		query = { 'method' : 'maintenance.getServices' }
		return self.api_connection.get(query)
	
	# get account notepad
	def get_notepad(self):
		"""Returns the notepad of a given account."""
		query = { 'method' : 'maintenance.getNotepad' }
		return self.api_connection.get(query)
	
	# set account notepad
	def set_notepad(self, notepad):
		"""Sets the notepad of an account.
		
		Arguments:
		notepad -- The notepad contents you wish to set.
		
		"""
		query = { 'method' : 'maintenance.setNotepad', 'notepad' : notepad }
		return self.api_connection.get(query)
		
	# get the 'type' of a service by id
	def get_service_type(self, service_id):
		"""Given a service id, returns the monitoring type.
		
		Arguments:
		service_id -- The id of the service you want to get the 
		              type of.
					 
		"""
		query = { 'method' : 'maintenance.getServiceType', 'serviceid' : service_id }
		return self.api_connection.get(query)
		
	# Admin
	# create a new monitoring service
	def add_new_service(self, service_name, service_type):
		"""Add a new monitoring service to the specified Webmetrics
		account. A trial is created for customers not on metered.
		
		Arguments:
		service_name -- The name to give the new service. Service
		                names can include alphanumeric, hyphen and
					    underscore characters.
		service_type -- The type of service. You can use the following:
		                APPLICATION
					    DNS
					    FTP
					    PING
					    POP
					    PORT
					    SMTP
					    STREAM
					    WEBSERVICE
					    WEBSITE
					    WSTRANS		
	
		"""
		query = { 'method' : 'maintenance.addNewService', 'servicename' : service_name, 'servicetype' : service_type.lower() }
		return self.api_connection.get(query)
	
	# change your user password
	def change_password(self, new_password):
		"""Sets the password for a given username.
		
		Arguments:
		new_password -- The new password.
		
		"""
		query = { 'method' : 'maintenance.changePassword', 'newpassword' : new_password }
		return self.api_connection.get(query)
	
	# rename an existing service
	def rename_service(self, new_name, service_id):
		"""Renames the service specified by the service ID.
		
		Arguments:
		new_name -- The new service name. This must contain only alpha-
		            numeric characters, underscores and dashes. The new
					service name must be different from the current and
					cannot be a duplicate of another existing service
					and/or longer than 50 chars.
		service_id -- The id of the service to be renamed.
		
		"""
		query = { 'method' : 'maintenance.renameService', 'newname' : new_name, 'serviceid' : service_id }
		return self.api_connection.get(query)
		
	# reset a service
	def reset_service(self, service_id, **kwargs):
		"""WARNING: This will remove all collected data for a service
		and is not reversible. The following will be cleared: historical
		log data, uptime info, service description, URL(s), script(s),
		search and error strings.
		
		Contact info for alerting purposes (as well as error notification
		settings), monitoring agent locations, maintenance windows, perf-
		ormance SLA objectives, interval and strikes before error are
		not affected.
		
		The service will be turned off once reset.
		
		NOTE: This API is not available for metered accounts.
		
		Arguments:
		service_id -- The id of the service you wish to reset.
		
		Keyword Arguments:
		keep_scripts -- Boolean. Monitoring scripts and URL(s) will not be
	       	            deleted.
		keep_description -- Boolean. The service description will not be
		                    deleted.
		keep_logs -- Boolean. The log data will not be deleted.
		
		"""
		query = { 'method' : 'maintenance.resetService', 'serviceid' : service_id }
		if 'keep_scripts' in kwargs and kwargs['keep_scripts'] == True:
			query.update({ 'keepscripts' : '1' })
		elif 'keep_description' in kwargs and kwargs['keep_description'] == True:
			query.update({ 'keepdescription' : '1'})
		elif 'keep_logs' in kwargs and kwargs['keep_logs'] == True:
			query.update({ 'keeplogs' : '1' })
		return self.api_connection.get(query)
		
	# duplicate a service
	# def duplicate_service(self):
	"""This method is strange. I will come back to it."""
	
	# Agent Settings
	
	# Service Status
	
	# Service Settings
	
	# Alert Contact Settings
	# get all alerting contacts
	def get_all_alerting_contacts(self, service_id):
		"""Get all contacts (diagnostic and escalation level) for a service.
		
		Arguments:
		service_id -- The service id of the service you want contacts for.
		
		"""
		query = { 'method' : 'maintenance.getAllAlertingContacts', 'serviceid' : service_id }
		return self.api_connection.get(query)
	
	# Reports
	
	# SMS/Voice Contact Settings
	
	# SLA Settings
	
	# Maintenance Windows