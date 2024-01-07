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

