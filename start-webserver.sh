#!/bin/bash
# Start a webserver from a THC disposable server
host=$(cat /config/self/reverse_ip)
port=$(cat /config/self/reverse_port)
php -S $host:$port -t docs
