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


def print_message(msg):
	now = datetime.now()
	date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
	## respose to write to browser and std out
	response = date_time + msg + iterations_count 
	sys.stdout.write(response)
	sys.stdout.flush()
	return response


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
			response = print_message("ping")
			return response
		except URLError as e:
			response = print_message("Unknown - service problem: Cant reach server: " + url_pong) 
			return response
		current_iteration += 1
		

@app.route("/reply")
def reply():
	iterations_count = request.args.get('iterations_count')
	response = print_message("pong")
	return response

if __name__ == "__main__":
	## Add check if port number is a numbers in the port allowed range
	inport = int(sys.argv[1])
	app.run(host='0.0.0.0', port=inport)
