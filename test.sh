#!/usr/bin/env bash

varButter="Butter"
varDog="Dog"

if [[ $(echo $varButter | wc -m) -gt $(echo $varDog | wc -m) ]]
then
	echo "Banana"
else
	echo "In Pyjamas"
fi

exit 0
