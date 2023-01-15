#!/usr/bin/env python3

"""

"""

import requests
import syslog

if __name__ == '__main__':

    syslog.syslog('pure-ftpd extauth: started')

    # payload = dict(
    # )

    # r = requests.post(
    #         url='https://hutter-cloud.eu.auth0.com/oauth/token',
    #         json=payload
    #     )
    # print(r.json())
    # r.raise_for_status()

    # data = r.json()
    # print(data)


    print('auth_ok:1')
    print('uid:999')
    print('gid:999')
    print('dir:/ftp')
    print('end')

    syslog.syslog('pure-ftpd extauth: ended')
