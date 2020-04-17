#!/bin/sh

python manager.py db migrate 

python manager.py db upgrade

flask run --host=0.0.0.0 --port 5000

 
