import csv
from django.apps import apps


def dump(qs, outfile):

    model = qs.model
    writer = csv.writer(outfile)
    
    headers = []
    for field in model._meta.fields:
    	headers.append(field.name)
    writer.writerow(headers)
    
    for obj in qs:
    	row = []
    	for field in headers:
    		val = getattr(obj, field)
    		if callable(val):
    			val = val()
    		if type(val) == 'unicode':
    			val = val.encode("utf-8")
    		row.append(val)
    	writer.writerow(row)
