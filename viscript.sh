#!/bin/bash
cat <<EOF
*****************
Vi Script
Update Metasploit
This script was created by Mastervi
*****************  
mastervi@mail.bg
*****************
by Master Vi
EOF
echo && echo "Press Enter To Continue ${endc}"
  read input
    cd /usr/share/exploitdb
    rm -rf archive.tar.bz2
    wget https://github.com/offensive-security/exploit-database/archive/master.zip
    unzip master.zip
    rm -rf exploit-database-master.zip
    echo -e "Done"
    sleep 3
