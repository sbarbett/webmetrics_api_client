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
	# def get_notepad(self):
	
	# set account notepad
	# def set_notepad(self):
	
	# get the 'type' of a service by id
	# def get_service_type(self):
	
	# Admin
	
	# Agent Settings
	
	# Service Status
	
	# Service Settings
	
	# Alert Contact Settings
	
	# Reports
	
	# SMS/Voice Contact Settings
	
	# SLA Settings
	
	# Maintenance Windows