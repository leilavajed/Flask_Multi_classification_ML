@echo off


curl -X POST -F file=@%1 http://localhost:5000/send_file

