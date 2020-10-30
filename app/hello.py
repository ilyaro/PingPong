#!/bin/env python3 
#Description: PingPong game between 2 docker imanges microservices 
#
#Author: Ilya Rokhkin
#Date: 
import flask
from flask import request
import sys
import os
from datetime import datetime
##import requests
import urllib.request
from urllib.error import URLError

app = flask.Flask(__name__)


@app.route("/")
def hello():
	return "PingPong Game of 2 Microservices"

@app.route("/pingpong")
def pingpong():
	iterations = request.args.get('iterations')
	iterations_int = int(iterations)
	current_iteration = 1
	partner = os.getenv('PARTNER')
	while current_iteration <= iterations_int:
		#print "DEBUG: $url $warnnum $critnum" if ($debug);
		url_pong = "http://" + partner + "/reply?iterations_count=" + str(current_iteration)
		try:
			res = urllib.request.urlopen(url_pong)
			dateTimeObj = datetime.now()
			print(dateTimeObj + " ping " + iterations_count, file=sys.stderr)
			return redirect('/')
		except URLError as e:
			response="Unknown - servcie problem: Cant reach server: " + url_pong 
			sys.stdout.write(response)
			sys.stdout.flush()
			return response
		current_iteration += 1
		

@app.route("/reply")
def reply():
	iterations_count = request.args.get('iterations_count')
	##print "DEBUG: $url $warnnum $critnum" if ($debug);
	now = datetime.now()
	date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
	## respose to write to browser and std out
	response = date_time + " pong " + iterations_count 
	sys.stdout.write(response)
	sys.stdout.flush()
	return response

if __name__ == "__main__":
	## Add check if port number is a numbers in the port allowed range
	inport = int(sys.argv[1])
	app.run(host='0.0.0.0', port=inport)
