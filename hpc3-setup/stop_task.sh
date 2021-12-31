kill `ps --user $(id -u) ax | grep "sleep 7d$" | egrep -o "^[[:space:]]*[[:digit:]]+"`
