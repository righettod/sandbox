#!/bin/bash
port=$(netstat -nutela | grep "LISTEN" | grep -Po ":[0-9]+" | tr -d ':')
echo "Port: $port"
php -S 0.0.0.0:$port -t docs
