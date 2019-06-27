#!/bin/bash
export PYTHONPATH="$PYTHONPATH:/usr/local/python3/lib/python3.6/site-packages"
# cd /Users/sgcy/data/MinuteBarDownloader
# export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_40.jdk/Contents/Home
# export PATH=$JAVA_HOME/bin:$PATH
# /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 -u downloader.py
cd /root/data/hkMoneyFlow
/usr/bin/python3 -u getData.py > log.txt 2>&1 &
# /usr/local/bin/python3.5 -u selector.py > g.out 2>&1 &
# /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 -u smallcapstock.py > g.out 2>&1 &
