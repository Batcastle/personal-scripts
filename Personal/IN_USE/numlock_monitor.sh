#!/bin/bash
prev=""
current=$(numlockx status)
while true; do
	if [ "$prev" == "" ] || [ "$current" == "$prev" ]; then
		sleep 0.5s
	else
		notify-send --app-name="Numlock Monitor" "$current"
	fi
	prev="$current"
	current=$(numlockx status)
done
