"""
Data model for resource search
"""

import json
from ..api.external_api import search_books

def get_resource(keyword=""):

	"""
	returns json file of organized data from extenal api

	Args:
		keyword (str): search string

	Returns:
		List: list of dictionarues conatining book information.
	"""

	lis = []

	data = search_books(keyword)

	for i in range(len(data)):
		lis.append(data[i])

	return lis
