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

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def print_message(msg, iterations_count):
	now = datetime.now()
	date_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
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
	more_details = " Please see docker compose output for more details"
	## Get iterations argument
	iterations = request.args.get('iterations')
	if is_integer(iterations):
		iterations_int = int(iterations)
	else:
		response = print_message(" iterations must be integer " + "Example: /pingpong?iterations=10 " + "Provided /pingpong?iterations=" + iterations, "") 
		return response + more_details
	##Get timeout optional argument
	timeout = request.args.get('timeout', None)
	if timeout:
		if is_integer(timeout):
			timeout_int = int(timeout)
		else:
			response = print_message(" timeout must be integer " + "Example: &timeout=40 " + "Provided &timeout=" + timeout, "") 
			return response + more_details
	iterations_count = 1
	inport_str = str(inport)
	myhostname = os.getenv('HOSTNAME')
	## Get partner hostname
	if myhostname == "ping":
		partner = "pong"
	else:
		partner = "ping"
	##Get pongsleep optional argument
	pongsleep = request.args.get('pongsleep', None)
	if pongsleep:
		if is_integer(pongsleep):
			url_po = "http://" + partner + ":" + inport_str + "/reply?pongsleep=" + pongsleep + "&iterations_count="
		else:
			response = print_message(" pongsleep must be integer " + "Example: &pongsleep=3 " + "Provided &pongsleep=" + iterations, "") 
			return response + more_details
	else:
		url_po = "http://" + partner + ":" + inport_str + "/reply?" + "iterations_count="
	## Iteration of ping pong
	while iterations_count <= iterations_int:
		iterations_count_str = str(iterations_count)
		a = datetime.now()
		if iterations_count == 1:
			start_time = a
		print_message(" ping ", iterations_count_str)
		## URL for pong
		url_pong = url_po + iterations_count_str
		try:
			res = urllib.request.urlopen(url_pong)
			b = datetime.now()
			c = b - a
			##Check if timeout is reached
			curr_whole_time = round((b - start_time).total_seconds() * 1000)
			if curr_whole_time > timeout_int:
				response = print_message(" Game Over. Timeout: " + timeout + " miliseconds " + " is reached. " + "The Game time is " + str(curr_whole_time) + " miliseconds. ", "") 
				return response + more_details
		except URLError as e:
			response = print_message(" Unknown - service problem: Cant reach server: " + url_pong + " ", iterations_count_str) 
			return response + more_details
		print_message( " iteration " + iterations_count_str + " done, took " + str(round(c.total_seconds() * 1000, 3)) + " miliseconds ", "")
		iterations_count += 1
	finish_time = datetime.now()
	c = finish_time - start_time
	fin_message = " Game Over, took " + str(round(c.total_seconds() * 1000, 3)) + " ms"
	print_message(fin_message, "")
	return fin_message + more_details

@app.route("/reply")
def reply():
	## Get iteration counter
	iterations_count = request.args.get('iterations_count')
	##Get pongsleep optional argument
	pongsleep = request.args.get('pongsleep', None)
	if pongsleep:
		import time
		time.sleep(pongsleep/1000)
	response = print_message(" pong ", iterations_count)
	return response

if __name__ == "__main__":
	## Add check if port number is a numbers in the port allowed range
	inport = int(sys.argv[1])
	app.run(host='0.0.0.0', port=inport)
