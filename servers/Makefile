SHELL = /bin/bash
.SHELLFLAGS = -x -e

GITLAB_HOME=/home/fangzhex/ogma3/jobbench_gitlab
NEXTCLOUD_HOME=/home/fangzhex/ogma3/jobbench_nextcloud
FILE_SERVER_PORT=8081

init:
	@export GITLAB_HOME
	@export NEXTCLOUD_HOME

start-nextcloud:
	cd nextcloud && docker-compose up -d

stop-nextcloud:
	cd nextcloud && docker-compose down

start-file-server:
	cd static && python3 -m http.server ${FILE_SERVER_PORT} -d files/ &

start-gitlab: init
	cd gitlab && docker-compose up -d

stop-gitlab:
	cd gitlab && docker-compose down

gitlab-root-password:
	docker exec -it gitlab bash -c 'cat /etc/gitlab/initial_root_password'
