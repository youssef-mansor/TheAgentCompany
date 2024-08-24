GITLAB_HOME=/home/fangzhex/ogma3/jobbench_gitlab

init:
	@export GITLAB_HOME

start-gitlab: init
	@echo "Navigating to gitlab directory and starting GitLab with Docker Compose..."
	cd gitlab && docker-compose up -d

stop-gitlab:
	@echo "Navigating to gitlab directory and stopping GitLab with Docker Compose..."
	cd gitlab && docker-compose down

gitlab-root-password:
	docker exec -it gitlab bash -c 'cat /etc/gitlab/initial_root_password'
