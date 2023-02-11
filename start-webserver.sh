#!/bin/bash
# Start a webserver from a THC disposable server
port=$(cat /config/self/reverse_port)
ip=$(cat /config/self/reverse_ip)
echo "[i] Server url: http://$ip:$port"
php -S 0.0.0.0:$port -t docs
