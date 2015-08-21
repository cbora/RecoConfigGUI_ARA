

all: config

config : Configuration.ui
	@echo "<Making... $@>"
	pyuic4 Configuration.ui -o Configuration.py