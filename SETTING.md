# Settings



### 가상환경 폴더이름

가상환경 폴더이름은 venv로 해주세요!

다른 이름을 쓰신다면 .gitignore 파일을 수정해주세요.



### requirements.txt

python library 버전 충돌을 방지하기 위해 통일이 필요합니다. 가상환경을 켜고 아래 명령어를 입력해주세요.

~~~
(venv) > pip freeze > requirements.txt
~~~


 `requirements.txt`가 update된 경우 

~~~
(venv) > pip install -r requirements.txt
~~~



