run-dev:
	docker-compose up

.PHONY: build
build:
	docker-compose build

.PHONY: migrate
migrate:
	docker-compose run web python manage.py migrate

###################
## Docker target##
###################

.PHONY: docker-kill
docker-kill:
	docker-compose kill

.PHONY: docker-rm
docker-rm: docker-kill
	docker-compose rm -v -f

.PHONY: clean
clean: docker-kill docker-rm
