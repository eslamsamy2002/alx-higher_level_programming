#!/bin/bash
# URL as an argument, sends a post request to the URL
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST ${1}
