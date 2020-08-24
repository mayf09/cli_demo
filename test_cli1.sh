#!/bin/sh

python3 cli1.py hello --count 3 abc > cli1_output.txt
diff cli1_success.txt cli1_output.txt
