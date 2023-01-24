#!/bin/bash
# Start a webserver from a THC disposable server
port=$(cat /config/self/reverse_port)
php -S 0.0.0.0:$port -t docs
