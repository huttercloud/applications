#!/usr/bin/env python3

"""

"""

import requests


if __name__ == '__main__':

    payload = dict(
    )

    r = requests.post(
            url='https://hutter-cloud.eu.auth0.com/oauth/token',
            json=payload
        )
    print(r.json())
    r.raise_for_status()

    data = r.json()
    print(data)


