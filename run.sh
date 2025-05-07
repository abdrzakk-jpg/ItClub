#! /bin/bash

while true;
do
    source "venv/bin/activate"
    port=5000
    PID=$(lsof -ti:$port)
    if [ ! -z "$PID" ]; then
        echo -e "\033[0;33mPort 5000 in use, killing process $PID...\033[0m"
        kill -9 $PID
    fi
    python main.py
    pkill -f flask
done