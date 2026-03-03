#!/bin/bash
set +x
set +v
export HOME=/righettod
/usr/bin/ttyd --cwd /tools --port 8000 --writable --credential "righettod:righettod" /bin/zsh
