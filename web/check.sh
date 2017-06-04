#! /bin/bash
declare -i t=0
t= $(pidof phantomjs)
while t=0   # 判断程序上次运行是否正常结束
do
        echo "Process exits with errors! Restarting!"
        python manage.py fetch_gpys   #重启程
done
echo "Process ends!"
