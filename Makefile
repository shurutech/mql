# Variables
DOCKER_COMPOSE = docker-compose

# Colors
COLOR_RESET = \033[0m
COLOR_BOLD = \033[1m
COLOR_GREEN = \033[32m
COLOR_YELLOW = \033[33m

# Check if Docker is installed
DOCKER_INSTALLED := $(shell command -v docker-compose 2> /dev/null)

# Targets
install:
    ifndef DOCKER_INSTALLED
	    $(error Docker is not installed. Please visit https://www.docker.com/get-started to download and install Docker.)
    endif

	@echo "$(COLOR_BOLD)=== Putting the services down (if already running) ===$(COLOR_RESET)"
	$(DOCKER_COMPOSE) down
	@echo "$(COLOR_BOLD)=== Building services ===$(COLOR_RESET)"
	$(DOCKER_COMPOSE) build --no-cache
	$(DOCKER_COMPOSE) up -d
	@echo "$(COLOR_BOLD)=== Waiting for services to start (~20 seconds) ===$(COLOR_RESET)"
	@sleep 20
	@$(MAKE) create-default-user
	@echo "$(COLOR_BOLD)=== Default Login Credentials >>> Email -> admin@example.com , Password -> admin ===$(COLOR_RESET)"
	@echo "$(COLOR_BOLD)=== Installation completed ===$(COLOR_RESET)"
	@echo "$(COLOR_BOLD)=== 🔥🔥 You can now access the dashboard at -> http://localhost:3000 ===$(COLOR_RESET)"
	@echo "$(COLOR_BOLD)=== Enjoy! ===$(COLOR_RESET)"

create-default-user:
	@echo "$(COLOR_BOLD)Creating default user...$(COLOR_RESET)"
	$(DOCKER_COMPOSE) exec -T backend python3 -m app.user_utils
	@echo "$(COLOR_BOLD)Default user creation attempted. Check logs for details.$(COLOR_RESET)"

down:
	$(DOCKER_COMPOSE) down --remove-orphans

restart:
	$(DOCKER_COMPOSE) restart
	@echo "$(COLOR_BOLD)=== Restart completed ===$(COLOR_RESET)"
	@echo "$(COLOR_BOLD)=== 🔥🔥 You can now access the dashboard at -> http://localhost:3000 ===$(COLOR_RESET)"
	@echo "$(COLOR_BOLD)=== Enjoy! ===$(COLOR_RESET)"

logs:
	$(DOCKER_COMPOSE) logs -f

.PHONY: install down