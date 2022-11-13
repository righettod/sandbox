#!/bin/bash
function write_step(){
    echo -e "\e[93m[+] $1\e[0m"
}
if [ "$#" -lt 1 ]; then
    script_name=$(basename "$0")
    write_step "Usage:"
    echo "$script_name [LISTEN_PORT]"
    write_step "Call example:"
    echo "$script_name 9588"
    exit 1
fi
Port=$1
php -S 0.0.0.0:$Port -t docs
