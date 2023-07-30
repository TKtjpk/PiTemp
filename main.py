#!/usr/bin/env python3

import sys
import psutil
import pymysql
import threading
from colorama import Fore, Back, Style
import subprocess

def get_cpu_temp():
    t = psutil.sensors_temperatures()

    for x in ['cpu-thermal', 'cpu_thermal']:
        if x in t:
            return t[x][0].current

    return 0


def update_db():
    try:

        conn = pymysql.connector.connect(host='YOUR_HOST_ADDRESS',
                            database='YOUR_DB_NAME',
                            user='YOUR_DB_USERNAME',
                            password='YOUR_DB_USER_PASSWORD')
    

        cursor = conn.cursor()

        query0 = 'INSERT INTO temp_mon (temp) VALUES (' + str(get_cpu_temp()) + ');'

        cursor.execute(query0)

        conn.commit()

        cursor.close()
        conn.close()

    except:
        print(Fore.RED + 'Database is not accessible at the moment')

    t = 5 if get_cpu_temp() > 60 else 30

    threading.Timer(t, update_db).start()

update_db()
