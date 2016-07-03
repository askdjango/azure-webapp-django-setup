# -*- coding: utf-8 -*-
import os

PYTHON_VERSION = '3.4'

assert(PYTHON_VERSION in ('3.4', '2.7'))


# 가상환경을 env 디렉토리에 이미 생성하셨다면, True로 설정해주세요.
IS_SKIP_PYTHON_DEPLOYMENT = False

# Azure WebApp 상에서 collectstatic 및 compilemessages 명령을 수행하지 않으실려면,
# True로 설정해주세요.
IS_SKIP_DJANGO_EXTRA = False
