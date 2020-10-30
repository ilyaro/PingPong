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


def print_message(msg, iterations_count):
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
	iterations_count = 1
	myhostname = os.getenv('HOSTNAME')
	## Get partner hostname
	if myhostname == "ping":
		partner = "pong"
	else:
		partner = "ping"
	while iterations_count <= iterations_int:
		iterations_count_str = str(iterations_count)
		## URL for pong
		url_pong = "http://" + partner + "/reply?iterations_count=" + iterations_count_str
		try:
			res = urllib.request.urlopen(url_pong)
			response = print_message(" ping ", iterations_count_str)
			return response
		except URLError as e:
			response = print_message(" Unknown - service problem: Cant reach server: " + url_pong + " ", iterations_count_str) 
			return response
		current_iteration += 1
		

@app.route("/reply")
def reply():
	iterations_count = request.args.get('iterations_count')
	response = print_message(" pong ", iterations_count)
	return response

if __name__ == "__main__":
	## Add check if port number is a numbers in the port allowed range
	inport = int(sys.argv[1])
	app.run(host='0.0.0.0', port=inport)
