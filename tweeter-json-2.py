#!/usr/bin/env python
import requests
import psycopg2
import json

conn = psycopg2.connect(database="tweeter_db", user="tweeteruser", host="localhost",port="26257")

req = requests.get('https://github.com/zalamgir/tweeter-go-tester/blob/master/tweet-2.json')

#data here is a list of dictionaries

