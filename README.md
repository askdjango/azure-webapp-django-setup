
# azure-webapp-django-setup

명령 한 줄 만으로 Azure Webapp Django 배포에 필요한 파일들이 모두 생성이 됩니다.

Azure WebApp 에서는 파이썬 `2.7`과 `3.4`를 지원하지만, 본 스크립트에서는 `2.7`을 지원하지 않습니다. `deploy_settings.py` 에서 `PYTHON_VERSION` 을 `2.7`로 수정하셔도 동작하지 않습니다.

다음 파일들이 생성이 됩니다.

 * .deployment : 배포 스크립트 지정
 * deploy.py : 실질적인 배포작업을 수행하는 파이썬 스크립트
 * deploy_settings.py : 배포 환경설정
 * web.3.4.config : 파이썬 3.4용 웹서비스 설정
 * ptvs\_virtualenv\_proxy.py : Python Tools for Visual Studio 용 가상환경 프록시


## 소스코드 선행작업

 1. 디렉토리 ROOT는 직접적으로 Django 프로젝트로 시작해야 합니다.
	 * 지원되는 구조
		 * manage.py
		 * myproject 디렉토리
	 * 하위 디렉토리에 django 프로젝트를 두고자할 경우, `web.3.4.config` 수정이 필요합니다.
 2. 프로젝트 ROOT 에 `requirements.txt` 파일이 꼭 필요하며, 현 Django 프로젝트 구동에 필요한 파이썬 팩키지들을 모두 명세해주세요. Azure WebApp 배포 시에 본 `requirements.txt` 에 명시한 파이썬 팩키지가 자동설치됩니다.
 3. `프로젝트/settings.py` 에 STATIC/MEDIA 설정을 꼭 넣어주세요. `web.3.4.config` 에서 아래 설정값으로 STATIC/MEDIA 파일 서빙을 하도록 설정되어있습니다.
	 * `settings.STATIC_URL = '/static/'`
	 * `settings.STATIC_ROOT = os.path.join(BASE_DIR, 'static')`
	 * `settings.MEDIA_URL = '/media/'`
	 * `settings.MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`


## Azure WebApp 에 필요한 파일 생성

### 사용법 (Python 3를 쓰실 경우)

    python -c "from urllib.request import urlopen; print(urlopen('https://raw.githubusercontent.com/askdjango/azure-webapp-django-setup/master/azure_webapp_setup.py').read().decode('utf8'))" | python - <django-settings-module>

명령 끝에 Azure WebApp 상에서 쓸 `DJANGO_SETTINGS_MODULE` 를 다음과 같이 지정해주세요. 다음은 사용 예입니다.

    python -c "from urllib.request import urlopen; print(urlopen('https://raw.githubusercontent.com/askdjango/azure-webapp-django-setup/master/azure_webapp_setup.py').read().decode('utf8'))" | python - myproject.settings


### 사용법 (Python 2를 쓰실 경우)

    python -c "from urllib import urlopen; print(urlopen('https://raw.githubusercontent.com/askdjango/azure-webapp-django-setup/master/azure_webapp_setup.py').read())" | python - <django-settings-module>

명령 끝에 Azure WebApp 상에서 쓸 `DJANGO_SETTINGS_MODULE` 를 다음과 같이 지정해주세요. 다음은 사용 예입니다.

    python -c "from urllib import urlopen; print(urlopen('https://raw.githubusercontent.com/askdjango/azure-webapp-django-setup/master/azure_webapp_setup.py').read())" | python - myproject.settings


## Azure WebApp 에 배포하기

작성 중.

### 오류확인


## 관련 문의

 * [ask@festi.kr](mailto:ask@festi.kr)
 * [AskDjango 페이스북 페이지](http://facebook.com/askdjango)
 * [AskDjango 페이스북 그룹](http://facebook.com/groups/askdjango)
 * [AskDjango 공식 사이트](http://festi.kr)
	 * [장고 차근차근 시작하기, 강의](http://festi.kr/class/django/)
