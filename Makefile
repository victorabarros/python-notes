.DEFAULT_GOAL := help
.PHONY: help

APP_NAME?=$(shell pwd | xargs basename)
APP_DIR = /src/${APP_NAME}
PWD=$(shell pwd)

clean-up:
	@docker rm -f ${APP_NAME}

debug:
	@echo "\e[1m\033[32m\nDebug mode\e[0m"
	# @docker rm -f go_notes
	docker run -it -v ${PWD}:${APP_DIR} -w ${APP_DIR} \
		-p 8091:8091 --name ${APP_NAME} python bash
