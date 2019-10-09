#!/usr/bin/env bash


# avvio il virtualenv
cd ~/.virtualenvs/gse3.6/
source bin/activate

# mi sposto nella cartella del watchdog e lo avvio in background e in NoHangUp mode
#cd ~/PycharmProjects/watchdog/
nohup python3 watchdog_fotoresize.py &
