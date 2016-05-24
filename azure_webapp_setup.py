# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
import os
import sys
try:
    import requests
except ImportError:
    print('Error) Missing python package : requests', file=sys.stderr)
    sys.exit(1)

try:
    from django.conf import settings
except ImportError:
    print('Error) Missing python pakcage : django', file=sys.stderr)
    sys.exit(1)

settings.configure(
    DEBUG=True,
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
    }])

import django
django.setup()

from django.template import engines


def main(settings_module):
    if not os.path.exists('requirements.txt'):
        print('Error) Missing file : requirements.txt', file=sys.stderr)
        sys.exit(1)

    base_url = 'https://raw.githubusercontent.com/askdjango/azure-webapp-django-setup/master/'
    filenames = ['ptvs_virtualenv_proxy.py', '.deployment', 'deploy.py', 'deploy_settings.py', 'web.3.4.config']

    for filename in filenames:
        print(filename + ' ...', end=' ')
        url = os.path.join(base_url, filename)
        content = requests.get(url).text
        if os.path.exists(filename):
            print('overwrite.')
        else:
            print('created.')

        template = engines['django'].from_string(content)
        content = template.render({'settings_module': settings_module})
        open(filename, 'wb').write(content.encode('utf8'))


if __name__ == '__main__':
    try:
        settings_module = sys.argv[1]
        main(settings_module)
    except IndexError:
        print('Error) Missing settings_module', file=sys.stderr)
        sys.exit(1)

    print()
    print('Powered by AskDjango : http://festi.kr')

