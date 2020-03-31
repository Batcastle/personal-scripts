#!/bin/bash
# -*- coding: utf-8 -*-
#
#  noise-canceling-daemon.sh
#
#  Copyright 2019 Thomas Castleman <contact@draugeros.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
regex="microphone|audio|JMTek"
{
	if [ "$EUID" == "0" ]; then
		/usr/bin/notify-send --app-name="noise-canceling-daemon" "noise-canceling-daemon running as root. Please correct."
		builtin echo "noise-canceling-daemon running as root. Please correct."
		builtin exit 1
	else
		# figure out if user has their own config for some reason
		USER_CONF="$HOME/.config/pulse/default.pa"
		if [ ! -f "$USER_CONF" ]; then
			/bin/cp /etc/pulse/default.pa "$USER_CONF"
		fi
	fi
	MAGIC_LINE="load-module module-echo-cancel source_name=noechosource sink_name=noechosink"
	while true; do
		USB=$(/usr/bin/lsusb)
		if $(/usr/bin/grep -q "$MAGIC_LINE" "$USER_CONF") && $(builtin echo "$USB" | /usr/bin/grep -qiE "$regex"); then
			/usr/bin/sleep 2s
		elif [ ! $(/usr/bin/grep -q "$MAGIC_LINE" "$USER_CONF") ] && $(builtin echo "$USB" | /usr/bin/grep -qiE "$regex"); then
			builtin echo "### NEW MIC DETECTED. ENABLING NOISE CANCELATION AND RESTARTING PULSEAUDIO . . . ###"
			/bin/cp "$USER_CONF" "$USER_CONF.bak"
			builtin echo "$MAGIC_LINE" >> "$USER_CONF"
			/usr/bin/pulseaudio -k
		elif $(/usr/bin/grep -q "$MAGIC_LINE" "$USER_CONF") && [ ! $(builtin echo "$USB" | /usr/bin/grep -qiE "$regex") ]; then
			builtin echo "### NEW MIC REMOVED. DISABLING NOISE CANCELATION AND RESTARTING PULSEAUDIO . . . ###"
			/usr/bin/sed -i "s/$MAGIC_LINE//g" "$USER_CONF"
			/usr/bin/pulseaudio -k
		elif [ ! $(/usr/bin/grep -q "$MAGIC_LINE" "$USER_CONF") ] && [ ! $(builtin echo "$USB" | /usr/bin/grep -qiE "$regex") ]; then
			/usr/bin/sleep 2s
		fi
	done
} | tee --append /tmp/noise-canceling-daemon.log
