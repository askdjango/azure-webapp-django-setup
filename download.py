# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests


def main():
    base = 'https://raw.githubusercontent.com/askdjango/azure-webapp-django-setup/master/'
    names = ['.deployment', 'deploy.py', 'deploy_settings.py', 'web.2.7.config', 'web.3.4.config', 'ptvs_virtualenv_proxy.py']

    for name in names:
        url = base + name
        print('downloading {} ...'.format(name))
        open(name, 'wb').write(requests.get(url).content)


if __name__ == '__main__':
    main()

