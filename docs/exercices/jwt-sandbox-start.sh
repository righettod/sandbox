#!/bin/bash
port=$(cat /config/self/reverse_port)
ip=$(cat /config/self/reverse_ip)
export FLASK_ENV="production"
export FLASK_APP="jwt-sandbox"
echo "[i] Server url: http://$ip:$port"
flask run --host=0.0.0.0 --port=$port --eager-loading --no-reload --no-debugger --with-threads