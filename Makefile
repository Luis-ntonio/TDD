# Define variables
PYTHON = python
PYTHONW = pythonw
COVERAGE = coverage
STRESSOR = stressor

# Define paths
FLASK_APP_SCRIPT = .\testings\exercise\example.py
COVERAGE_FILE = ./coverage/.coverage
TEST_SCRIPT = ./testings/test_structural.py
STRESS_SCENARIO = ./stress_test/scenario1/scenario.yaml
STRESS_LOG = ./stress_test/stress.log

# Define tasks change star_flask with start_docker if you want to run the server in a docker container
run: start_docker run_coverage run_stressor stop_flask

# Launch Flask server
start_docker:
	docker-compose up --build -d

start_flask:
	powershell -Command "Start-Process -NoNewWindow -FilePath '$(PYTHONW)' -ArgumentList '$(FLASK_APP_SCRIPT)'"

# Testing with coverage
run_coverage:
	$(COVERAGE) run --data-file=$(COVERAGE_FILE) -m pytest $(TEST_SCRIPT)
	$(COVERAGE) report --data-file=$(COVERAGE_FILE) -m

# Stress testing
run_stressor:
	$(STRESSOR) run $(STRESS_SCENARIO) --log $(STRESS_LOG)

# Stop Flask server
stop_flask:
	-@taskkill /F /IM pythonw.exe /T 2> NUL || echo "No pythonw.exe process found."

.PHONY: run start_flask run_coverage run_stressor stop_flask
