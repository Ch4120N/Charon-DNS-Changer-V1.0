export CHDNSCHANGER="/opt/Charon-DNS-Changer-V1.0"

if [[ $1 == '-h' || $1 == 'help' ]]; then
	echo "To run \`Charon DNS Changer\` type \`chdnschanger\` in your prompt"
	echo

else
	cd $CHDNSCHANGER
	python3 ./chdnschanger.py
fi
