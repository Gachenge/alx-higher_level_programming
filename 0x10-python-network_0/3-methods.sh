#!/usr/bin/bash
# displays all HTTP methods the server will accespt
curl -sI "$1" | grep Allow | cut -c 8-
