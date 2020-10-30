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

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def convert(msf):
    minutes, seconds = msf.split(':')
    seconds, milliseconds = seconds.split('.')
    minutes, seconds, milliseconds = map(int, (minutes, seconds, milliseconds))
    return (minutes * 60 + seconds) * 1000 + milliseconds

def print_message(msg, iterations_count):
	now = datetime.now()
	date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
	## respose to write to browser and std out
	response = date_time + msg + iterations_count + "\n" 
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
	inport_str = str(inport)
	myhostname = os.getenv('HOSTNAME')
	## Get partner hostname
	if myhostname == "ping":
		partner = "pong"
	else:
		partner = "ping"
	while iterations_count <= iterations_int:
		iterations_count_str = str(iterations_count)
		a = datetime.now()
		if iterations_count == 1:
			start_time = a
		print_message(" ping ", iterations_count_str)
		## URL for pong
		url_pong = "http://" + partner + ":" + inport_str + "/reply?iterations_count=" + iterations_count_str
		try:
			res = urllib.request.urlopen(url_pong)
			b = datetime.now()
			c = b - a
		except URLError as e:
			response = print_message(" Unknown - service problem: Cant reach server: " + url_pong + " ", iterations_count_str) 
			return response
		print_message( " iteration " + iterations_count_str + " done, took " + str(c.total_seconds() * 1000) + " microseconds", "")
		iterations_count += 1
	finish_time = datetime.now()
	c = finish_time - start_time
	fin_message = " Game Over, took " + str(c.total_seconds() * 1000) + " ms"
	print_message(fin_message, "")
	return fin_message

@app.route("/reply")
def reply():
	iterations_count = request.args.get('iterations_count')
	response = print_message(" pong ", iterations_count)
	return response

if __name__ == "__main__":
	## Add check if port number is a numbers in the port allowed range
	inport = int(sys.argv[1])
	app.run(host='0.0.0.0', port=inport)
