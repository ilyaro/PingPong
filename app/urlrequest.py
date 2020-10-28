#!/bin/env python3 
#Description: 
#
#Author: Ilya Rokhkin
#Date: 

##my $debug=0;
import sys
##import requests
import urllib.request
from urllib.error import URLError
import json 
url = sys.argv[1]
##print(url)
warnnum = sys.argv[2]
critnum = sys.argv[3]

##print "DEBUG: $url $warnnum $critnum" if ($debug);
try:
    res = urllib.request.urlopen(url)
except URLError as e:
    print("Unknown - servcie problem: Can't reach server: " + url + " " + str(e))
    exit(3)

##print @bccerrsite if ($debug);
res_body = res.read()
content = json.loads(res_body.decode("utf-8"))
number_builds = len(content["items"])

