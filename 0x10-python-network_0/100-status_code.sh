#!/bin/bash
# script to get back the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
