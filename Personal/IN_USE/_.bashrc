#!/bin/bash
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

################################################################################
##  FUNCTIONS                                                                 ##
################################################################################

##
## ARRANGE $PWD AND STORE IT IN $NEW_PWD
## * The home directory (HOME) is replaced with a ~
## * The last pwdmaxlen characters of the PWD are displayed
## * Leading partial directory names are striped off
##  /home/me/stuff -> ~/stuff (if USER=me)
##  /usr/share/big_dir_name -> ../share/big_dir_name (if pwdmaxlen=20)
##
## Original source: WOLFMAN'S color bash promt
## https://wiki.chakralinux.org/index.php?title=Color_Bash_Prompt#Wolfman.27s
##
bash_prompt_command() {
	# How many characters of the $PWD should be kept
	#local pwdmaxlen=25

	# Indicate that there has been dir truncation
	#local trunc_symbol=".."

	# Store local dir
	#local dir=${PWD##*/}

	# Which length to use
	#pwdmaxlen=$(( ( pwdmaxlen < ${#dir} ) ? ${#dir} : pwdmaxlen ))

	#NEW_PWD=${PWD/#$HOME/\~}
 
	#local pwdoffset=$(( ${#NEW_PWD} - pwdmaxlen ))

	# Generate name
	#if [ ${pwdoffset} -gt "0" ]; then
		#NEW_PWD=${NEW_PWD:$pwdoffset:$pwdmaxlen}
		#NEW_PWD=${trunc_symbol}/${NEW_PWD#*/}
	#fi
	#Bypass all of that for the sake of verbosity
	if [ "$PWD" == "$HOME" ]; then
		NEW_PWD="~"
	else
		NEW_PWD="$PWD"
	fi
}




##
## GENERATE A FORMAT SEQUENCE
##
format_font()
{
 ## FIRST ARGUMENT TO RETURN FORMAT STRING
	local output=$1


	case $# in
		2)
			eval $output="'\[\033[0;${2}m\]'"
			;;
		3)
			eval $output="'\[\033[0;${2};${3}m\]'"
			;;
		4)
			eval $output="'\[\033[0;${2};${3};${4}m\]'"
			;;
		*)
			eval $output="'\[\033[0m\]'"
			;;
	esac
}



##
## COLORIZE BASH PROMT
##
bash_prompt() {

 ############################################################################
 ## COLOR CODES                                                            ##
 ## These can be used in the configuration below                           ##
 ############################################################################
 
 ## FONT EFFECT
	local      NONE='0'
	local      BOLD='1'
	local       DIM='2'
	local UNDERLINE='4'
	local     BLINK='5'
	local    INVERT='7'
	local    HIDDEN='8'
 
 
	## COLORS
	local   DEFAULT='9'
	local     BLACK='0'
	local       RED='1'
	local     GREEN='2'
	local    YELLOW='3'
	local      BLUE='4'
	local   MAGENTA='5'
	local      CYAN='6'
	local    L_GRAY='7'
	local    D_GRAY='60'
	local     L_RED='61'
	local   L_GREEN='62'
	local  L_YELLOW='63'
	local    L_BLUE='64'
	local L_MAGENTA='65'
	local    L_CYAN='66'
	local     WHITE='67'
 
 
	## TYPE
	local     RESET='0'
	local    EFFECT='0'
	local     COLOR='30'
	local        BG='40'
 
 
	## 256 COLOR CODES
	local NO_FORMAT="\[\033[0m\]"
	local ORANGE_BOLD="\[\033[1;38;5;208m\]"
	local TOXIC_GREEN_BOLD="\[\033[1;38;5;118m\]"
	local RED_BOLD="\[\033[1;38;5;1m\]"
	local CYAN_BOLD="\[\033[1;38;5;87m\]"
	local BLACK_BOLD="\[\033[1;38;5;0m\]"
	local WHITE_BOLD="\[\033[1;38;5;15m\]"
	local GRAY_BOLD="\[\033[1;90m\]"
	local BLUE_BOLD="\[\033[1;38;5;74m\]"
 
 
 
 
 
 ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  
   ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##
 ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ## 

 
 
 ##                          CONFIGURE HERE                                ##

 
 
 ############################################################################
 ## CONFIGURATION                                                          ##
 ## Choose your color combination here                                     ##
 ############################################################################
	local FONT_COLOR_1=$BLACK
	local BACKGROUND_1=$RED
	local TEXTEFFECT_1=$BOLD
 
	local FONT_COLOR_2=$BLACK
	local BACKGROUND_2=$GREEN
	local TEXTEFFECT_2=$BOLD
 
	local FONT_COLOR_3=$GREEN
	local BACKGROUND_3=$BLACK
	local TEXTEFFECT_3=$BOLD
 
	if [ "$EUID" == "0" ]; then
		local PROMPT_SYMBOL="#"
	else
		local PROMPT_SYMBOL="$"
	fi
 
	local PROMT_FORMAT="$TOXIC_GREEN_BOLD$PROMPT_SYMBOL$NO_FORMAT"
 
 
 ############################################################################
 ## TEXT FORMATING                                                         ##
 ## Generate the text formating according to configuration                 ##
 ############################################################################
 
	## CONVERT CODES: add offset
	FC1=$(($FONT_COLOR_1+$COLOR))
	BG1=$(($BACKGROUND_1+$BG))
	FE1=$(($TEXTEFFECT_1+$EFFECT))
 
	FC2=$(($FONT_COLOR_2+$COLOR))
	BG2=$(($BACKGROUND_2+$BG))
	FE2=$(($TEXTEFFECT_2+$EFFECT))
 
	FC3=$(($FONT_COLOR_3+$COLOR))
	BG3=$(($BACKGROUND_3+$BG))
	FE3=$(($TEXTEFFECT_3+$EFFECT))
 
	FC4=$(($FONT_COLOR_4+$COLOR))
	BG4=$(($BACKGROUND_4+$BG))
	FE4=$(($TEXTEFFECT_4+$EFFECT))
 

	## CALL FORMATING HELPER FUNCTION: effect + font color + BG color
	local TEXT_FORMAT_1
	local TEXT_FORMAT_2
	local TEXT_FORMAT_3
	local TEXT_FORMAT_4 
	format_font TEXT_FORMAT_1 $FE1 $FC1 $BG1
	format_font TEXT_FORMAT_2 $FE2 $FC2 $BG2
	format_font TEXT_FORMAT_3 $FC3 $FE3 $BG3
	format_font TEXT_FORMAT_4 $FC4 $FE4 $BG4
 
 
	# GENERATE PROMT SECTIONS
	local PROMT_USER=$"$TEXT_FORMAT_1 \u "
	local PROMT_HOST=$"$TEXT_FORMAT_2 \h "
	local PROMT_PWD=$"$TEXT_FORMAT_3 \${NEW_PWD} "
	local PROMT_INPUT=$"$PROMT_FORMAT "


 ############################################################################
 ## SEPARATOR FORMATING                                                    ##
 ## Generate the separators between sections                               ##
 ## Uses background colors of the sections                                 ##
 ############################################################################
 
	## CONVERT CODES
	TSFC1=$(($BACKGROUND_1+$COLOR))
	TSBG1=$(($BACKGROUND_2+$BG))
 
	TSFC2=$(($BACKGROUND_2+$COLOR))
	TSBG2=$(($BACKGROUND_3+$BG))
 
	TSFC3=$(($BACKGROUND_3+$COLOR))
	TSBG3=$(($DEFAULT+$BG))
 

	## CALL FORMATING HELPER FUNCTION: effect + font color + BG color
	local SEPARATOR_FORMAT_1
	local SEPARATOR_FORMAT_2
	local SEPARATOR_FORMAT_3
	format_font SEPARATOR_FORMAT_1 $TSFC1 $TSBG1
	format_font SEPARATOR_FORMAT_2 $TSFC2 $TSBG2
	format_font SEPARATOR_FORMAT_3 $TSFC3 $TSBG3
 

	# GENERATE SEPARATORS WITH FANCY TRIANGLE
	#Stunted Triangle
	local TRIANGLE=""
	if [ "$(uname -o)" != "Android" ]; then
		local TRIANGLE=$'\342\226\266'
	fi
	#What is SUPPOSED to be used
	#local TRIANGLE=$'\356\202\260' 
	local SEPARATOR_1=$SEPARATOR_FORMAT_1$TRIANGLE
	local SEPARATOR_2=$SEPARATOR_FORMAT_2$TRIANGLE
	local SEPARATOR_3=$SEPARATOR_FORMAT_3$TRIANGLE



 ############################################################################
 ## WINDOW TITLE                                                           ##
 ## Prevent messed up terminal-window titles                               ##
 ############################################################################
	case $TERM in
		xterm*|rxvt*)
			local TITLEBAR='\[\033]0;\u:${NEW_PWD}\007\]'
			;;
		*)
			local TITLEBAR=""
			;;
	esac



 ############################################################################
 ## BASH PROMT                                                             ##
 ## Generate promt and remove format from the rest                         ##
 ############################################################################
if $(echo "$PROMPT_PWD" | grep -q "$HOME"); then
	PROMPT_PWD=$(echo "$PROMPT_PWD" | sed s:"$HOME" :~:g)
fi
PS1="$TITLEBAR\n${PROMT_USER}${SEPARATOR_1}${PROMT_HOST}${SEPARATOR_2}${PROMT_PWD}${SEPARATOR_3}${PROMT_INPUT}"

 

	## For terminal line coloring, leaving the rest standard
	none="$(tput sgr0)"
	trap 'echo -ne "${none}"' DEBUG
}




################################################################################
##  MAIN                                                                      ##
################################################################################

## Bash provides an environment variable called PROMPT_COMMAND. 
## The contents of this variable are executed as a regular Bash command 
## just before Bash displays a prompt. 
## We want it to call our own command to truncate PWD and store it in NEW_PWD
PROMPT_COMMAND=bash_prompt_command

## Call bash_promnt only once, then unset it (not needed any more)
## It will set $PS1 with colors and relative to $NEW_PWD, 
## which gets updated by $PROMT_COMMAND on behalf of the terminal
bash_prompt
unset bash_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
alias delete='rm'
clear
if [ $(uname -o) != "Android" ]; then
	echo -e "\nCurrent Display Server: $XDG_SESSION_TYPE\n"
	alias root='sudo'
	alias please='sudo'
	alias fucking='sudo'
	alias autoremove='root apt -y autoremove'
	alias remove='root apt -y purge'
	alias install-app='root apt -y install'
	alias update='root apt update && root apt -y upgrade && sudo apt -y autoremove && sudo apt -y clean && notify-send "Updates Completed Succesfully" || notify-send "Updates Failed"'
	alias clean="root apt clean && root apt purge -y $(dpkg -l | grep '^rc' | awk '{print $2}')"
else
	export PATH="$HOME/bin:$PATH"
	alias autoremove='apt -y autoremove'
	alias remove='apt -y purge'
	alias install-app='apt -y install'
	alias update='apt update && apt -y upgrade && apt -y autoremove && apt -y clean && echo "Updates Completed Succesfully" || echo "Updates Failed"'
	alias clean="apt clean && apt purge -y $(dpkg -l | grep '^rc' | awk '{print $2}')"
	which sudo 1>/dev/null 2>/dev/null
	check_sudo="$?"
	which su 1>/dev/null 2>/dev/null
	check_su="$?"
	if [ "$check_sudo" == "0" ]; then
		alias root='sudo'
		alias please='sudo'
		alias fucking='sudo'
	elif [ "$check_su" == "0" ]; then
		alias root='echo "Sudo not available. Please use su."'
		alias please='echo "Sudo not available. Please use su."'
		alias fucking='echo "Sudo not available. Please use su."'
	else
		alias root='Root not available'
		alias please='Root not available'
		alias fucking='Root not available'
	fi
fi
alias dpkg-info='dpkg-deb -I'
alias nano='nano -l'
echo -e "Welcome, Master\n"
screenfetch
alias csci-ssh='ssh tcastlem@montreat.cs.unca.edu'
alias nextcloud-ssh='ssh batcastle@47.38.113.25'
if [ "$EUID" == "0" ]; then
	builtin echo -e "WARNING: YOU ARE ROOT.\n"
fi



# EOF
