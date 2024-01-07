# github_test
깃허브 초기 세팅 관련해서 연습하는 깃허브 테스트입니다.
아래는 깃허브에 대해서 필요한 자료들 모아놓는 링크입니

1. https://udemy.wjtb.co.kr/newsletter/id/10000236

2. https://blog.naver.com/trust_respect/223286552292

3. https://tagilog.tistory.com/377

저장소 생성 및 초기화

git init: 새로운 Git 저장소 초기화
git clone <URL>: 원격 저장소를 복제하여 로컬 저장소 생성
변경 사항 확인

git status: 변경된 파일 목록 확인
git diff: 변경된 내용을 확인
변경 사항 스테이징 및 커밋

git add <파일>: 변경 사항을 스테이징
git commit -m "커밋 메시지": 스테이징된 변경 사항을 커밋
브랜치 관리

git branch: 브랜치 목록 확인
git checkout <브랜치>: 특정 브랜치로 이동
git merge <브랜치>: 브랜치 병합
원격 저장소 관리

git remote -v: 연결된 원격 저장소 확인
git pull origin <브랜치>: 원격 저장소에서 변경 사항을 가져와 병합
git push origin <브랜치>: 로컬 변경 사항을 원격 저장소로 푸시
로그 및 히스토리

git log: 커밋 히스토리 확인
git blame <파일>: 파일의 각 라인에 대한 최종 수정자 확인
태그 관리

git tag <태그명>: 현재 커밋에 태그 추가
git tag -a <태그명> -m "태그 메시지": 주석이 달린 태그 추가
이 명령어들은 기본적인 Git 작업을 수행하는 데 도움이 됩니다. 더 많은 옵션과 명령어를 알고 싶다면 git --help를 사용하거나 Git 공식 문서를 참고하세요.

kwonn@BOOK-AKBDRO9VGJ MINGW64 ~
$ git -help
unknown option: -help
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]
           $ mkdir git
cd git
git clone https://github.com/davidkims/github_test
Cloning into 'github_test'...
remote: Enumerating objects: 22, done.
remote: Counting objects: 100% (22/22), done.
remote: Compressing objects: 100% (20/20), done.
remote: Total 22 (delta 8), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (22/22), 12.33 KiB | 4.11 MiB/s, done.
Resolving deltas: 100% (8/8), done.

이 코드는 HTML, CSS, JavaScript를 사용하여 간단한 웹 페이지를 만드는 예제입니다. 여기에 몇 가지 주요 사항을 정리하겠습니다:

jQuery 라이브러리 추가:

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>: jQuery 라이브러리를 CDN을 통해 추가합니다.
colors.js 파일 추가:

<script src="colors.js"></script>: colors.js 파일을 현재 HTML 파일과 동일한 디렉토리에 위치한 것으로 가정합니다. 이 파일은 nightDayHandler 함수를 정의한 것으로 추측됩니다.
nightDayHandler 함수:

<input id="night_day" type="button" value="night" onclick="nightDayHandler(this);">: 버튼을 클릭하면 nightDayHandler 함수가 호출되며, 이 함수는 무언가를 처리하는 것으로 예상됩니다. colors.js 파일에서 이 함수를 확인할 수 있을 것입니다.
페이지 내용 로딩:

<ol> 요소 내부에는 각각 "HTML", "CSS", "JavaScript"에 대한 링크가 있습니다. 각 링크는 클릭 시 fetch를 사용하여 해당 파일의 내용을 가져와서 <article> 요소에 표시하는 방식으로 동작합니다.
페이지 구조:

<h1> 요소 안에는 "WEB" 링크가 있으며, 페이지 상단에 위치합니다.
<input> 요소는 "night"라는 초기 텍스트를 가진 버튼으로, 클릭 시 nightDayHandler 함수가 호출됩니다.
<ol> 요소 안에는 "HTML", "CSS", "JavaScript"에 대한 링크 목록이 있습니다.
<article> 요소는 링크를 클릭할 때 해당 내용이 표시되는 부분입니다.
CSS 스타일링:

현재 코드에서는 CSS 스타일링 부분이 빠져 있습니다. 페이지의 디자인과 스타일을 추가하려면 필요한 CSS 코드를 작성해야 합니다.
위의 정리를 통해 이 코드는 간단한 웹 페이지를 구성하고, 사용자가 각 링크를 클릭할 때마다 해당 내용을 비동기적으로 로드하는 기능을 가지고 있습니다. 페이지의 완전한 동작은 colors.js 파일과 추가적인 CSS 스타일에 의존할 수 있습니다.


