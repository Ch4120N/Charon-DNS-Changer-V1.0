export CHDNSCHANGER="/opt/Charon-DNS-Changer"

if [[ $1 == '-h' || $1 == 'help' ]]; then
	echo "To run \`Charon DNS Changer\` type \`ChDNSChanger\` in your prompt"
	echo

else
	cd $CHDNSCHANGER
	sudo python3 ./ChDNSChanger.py
fi
