export FLASK_APP=app

run:
	python app.py

#RUN=docker compose run --rm project
#
#all:
#	DOCKER_BUILDKIT=0 docker compose build
#
#run:
#	docker compose run --service-ports --rm project
#
#shell:
#	docker compose run --rm project /bin/bash
#
#stop:
#	docker compose down
