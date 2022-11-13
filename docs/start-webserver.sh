#!/bin/bash
if [ "$#" -lt 1 ]; then
    script_name=$(basename "$0")
    echo "Usage:"
    echo "   $script_name [LISTENING_PORT]"
    echo ""
    echo "Call example:"
    echo "    $script_name 9588"
    exit 1
fi
Port=$1
php -S 0.0.0.0:$Port
