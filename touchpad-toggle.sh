#!/bin/bash
set -o errexit #(equivalent -e)
set -o nounset #(equivalent -u)

usage(){
	builtin echo "Usage: ${0} {-enable|-e|-disable|-d}"
}

if [ $# -ne 1 ]; then
  usage
  exit 1
fi

#this folder doesn't work. Need something else. lsusb?
#or can we use what usb-scanner was doing? Probably.
base_dir=/sys/bus/serio/drivers/psmouse
device_id=serio1

if [ ${1} = "-disable" -o ${1} = "-d" ]; then
	logger "${0} is disabling the touchpad"
	builtin echo -n manual > $base_dir/bind_mode
	builtin echo -n $device_id > $base_dir/unbind 2>/dev/null || true
elif [ ${1} = "-enable" -o ${1} = "-e" ]; then
	logger "${0} is enabling the touchpad"
	builtin echo -n auto > $base_dir/bind_mode
else
	usage
	exit 1
fi

