
# azure-webapp-django-setup

[Azure 공식문서 - Azure에서 Django를 활용하여 웹앱 만들기](https://azure.microsoft.com/documentation/articles/web-sites-python-create-deploy-django-app/) 문서에도 배포방법을 설명하고 있습니다. 하지만 불필요한 설명이 많고 배포스크립트가 ***bat 스크립트***로 되어있어서 (암호같아요 ;;; ), 불필요한 파일들을 정리하고 코드 가독성이 좋도록 ***Azure WebApp Django Setup*** 프로젝트를 만들었습니다.


## 튜토리얼 실습 영상

본 스크립트를 통해, Azure WebApp 배포를 실습하는 영상을 찍어봤습니다.

 * [장고걸스 튜토리얼, Azure WebApp 배포 동영상 (한글버전)](https://www.facebook.com/askdjango/videos/634463410050050/)


## Azure WebApp

[Azure](https://azure.microsoft.com/)는 Microsoft에서 서비스하고 있는 클라우드 서비스입니다. 클라우드 서비스는 크게 IaaS, PaaS, SaaS로 구분됩니다. Azure PaaS서비스로서 [Azure WebApp](https://azure.microsoft.com/services/app-service/web/)가 서비스되고 있습니다.

Azure WebApp의 주요 특징

 * 인프라 운영부담이 없습니다. (PaaS의 일반적인 특징)
 * Github 등을 활용한 지속적인 배포지원 : Github 에 올리는 것만으로 배포를 수행할 수 있습니다.
 * 지원언어 : .NET, Java, PHP, Node.js 및 ***Python***
 * 배포된 프로그램은 윈도우, IIS 웹서버 상에서 구동됩니다.


## Azure WebApp Django Setup

Azure WebApp 상에서 Django 애플리케이션을 돌리기 위해서는, 다음 파일들이 필요합니다.

 * .deployment : 배포 스크립트 지정
 * deploy.py : 실질적인 배포작업을 수행하는 파이썬 스크립트
 * deploy\_settings.py : 배포 환경설정
 * web.3.4.config : 파이썬 3.4용 웹서비스 설정
 * web.2.7.config : 파이썬 2.7용 웹서비스 설정
 * ptvs\_virtualenv\_proxy.py : Python Tools for Visual Studio 용 가상환경 프록시

명령 한 줄 만으로 Azure Webapp Django 배포에 필요한 위 파일들이 모두 생성이 됩니다.

파이썬 `3.4` 와 `2.7` 을 지원합니다. 디폴트로 `3.4` 로 설정되어있습니다. `2.7` 로 설정하실려면,  `deploy_settings.py` 에서 `PYTHON_VERSION` 을 `2.7`로 수정하시면 됩니다.


## 소스코드 선행작업

 * 스크립트 실행을 위해 `requests` 라이브러리가 필요합니다. 아래 명령으로 설치해주세요.
```
쉘> pip install requests
```
 * 디렉토리 ROOT는 직접적으로 Django 프로젝트로 시작해야 합니다.
	 * 지원되는 구조
		 * manage.py
		 * myproject 디렉토리
	 * 하위 디렉토리에 django 프로젝트를 두고자할 경우, `web.3.4.config` 수정이 필요합니다. (파이썬 2.7을 쓰시고자 하실 경우에는 `web.2.7.config` 파일을 수정해주세요.)

 * 프로젝트 ROOT 에 `requirements.txt` 파일이 꼭 필요하며, 현 Django 프로젝트 구동에 필요한 파이썬 팩키지들을 모두 명시해주세요. Azure WebApp 배포 시에 본 `requirements.txt` 에 명시한 파이썬 팩키지가 자동설치됩니다. 아래는 예시입니다.
```
django
pillow
```
 * `프로젝트/settings.py` 에 STATIC/MEDIA 설정을 꼭 넣어주세요. `web.3.4.config` (혹은 `web.2.7.config`) 에서 아래 설정값으로 STATIC/MEDIA 파일 서빙을 하도록 설정되어있습니다.
```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```


### 주의사항

 * `env` 이름으로 virtualenv를 만들어서 업로드하지 마세요. virtualenv는 Azure WebApp상에서 배포과정 중에 `env` 이름으로 자동으로 생성이 됩니다.


## Azure WebApp 설정파일 다운로드

다음 명령을 `manage.py` 가 있는 경로에서 명령프롬프트 혹은 터미널을 통해 실행시켜주세요.

```
쉘> python -c "import requests; exec(requests.get('https://festi.kr/azure/d.py').content)"
```


`web.3.4.config` (혹은 `web.2.7.config`) 파일 내 `DJANGO_SETTINGS_MODULE` 값을 Azure WebApp 에서 쓸 settings 로 설정해주세요. 다음은 설정 예입니다.

```xml
<add key="DJANGO_SETTINGS_MODULE" value="myproject.settings" />
```


## Azure WebApp 에 배포하기

![](Azure WebApp Slides/004.jpeg)

![](Azure WebApp Slides/005.jpeg)

![](Azure WebApp Slides/006.jpeg)

![](Azure WebApp Slides/007.jpeg)

![](Azure WebApp Slides/008.jpeg)

![](Azure WebApp Slides/009.jpeg)

![](Azure WebApp Slides/010.jpeg)

![](Azure WebApp Slides/011.jpeg)

![](Azure WebApp Slides/012.jpeg)

![](Azure WebApp Slides/013.jpeg)

![](Azure WebApp Slides/014.jpeg)

![](Azure WebApp Slides/015.jpeg)

![](Azure WebApp Slides/016.jpeg)

![](Azure WebApp Slides/017.jpeg)

![](Azure WebApp Slides/018.jpeg)

![](Azure WebApp Slides/019.jpeg)

![](Azure WebApp Slides/020.jpeg)

![](Azure WebApp Slides/021.jpeg)

![](Azure WebApp Slides/022.jpeg)

![](Azure WebApp Slides/023.jpeg)

![](Azure WebApp Slides/024.jpeg)

![](Azure WebApp Slides/025.jpeg)

![](Azure WebApp Slides/026.jpeg)

![](Azure WebApp Slides/027.jpeg)

![](Azure WebApp Slides/028.jpeg)


## 참고

Azure WebApp 에 배포한 Django 프로젝트 샘플은 [이곳](http://msdjangoisbest.azurewebsites.net/)에서 확인하실 수 있으며, 소스코드는 [github 저장소](https://github.com/askdjango/djangoisbest)에서 확인하실 수 있습니다.


## 관련 문의

 * [ask@festi.kr](mailto:ask@festi.kr)
 * [AskDjango 페이스북 페이지](http://facebook.com/askdjango)
 * [AskDjango 페이스북 그룹](http://facebook.com/groups/askdjango)
 * [AskDjango 공식 사이트](http://festi.kr)
	 * [서비스 차근차근 시작하기, 강의](http://festi.kr/class/service/) : 접수 중
     * [장고 차근차근 시작하기, 강의](http://festi.kr/class/django/) : 4기 진행 중
     * [파이썬 차근차근 시작하기, 강의](http://festi.kr/class/python/) : 4기 준비 중

