# Makefile default shell is /bin/sh which does not implement source.
# https://stackoverflow.com/questions/7507810/how-to-source-a-script-in-a-makefile
SHELL := /bin/bash

preliminary:
	# Install global system pip and venv (its possible as user, but not very common)
	sudo apt install python3-pip python3-venv
	
	# Install pipx (see https://pypi.org/project/pipx/)
	python3 -m pip install --user pipx
	
	# Add localpath entry to .bashrc 
	python3 -m pipx ensurepath
	
	# Add shell completion to bashrc 
	echo 'eval "$(register-python-argcomplete pipx)"' >> ~/.bashrc

	#################################################
	# You may want to restart the current shell?    #
	#################################################
	
	# Install virtualenv
	pipx install virtualenv

virtualenv: 
	# Create virtualenv
	virtualenv performance
	
	# Activate virtualenv manually!
	# https://stackoverflow.com/questions/7507810/how-to-source-a-script-in-a-makefile
	#################################################
	# Run manually: source performance/bin/activate #
	#################################################

setup: requirements.txt		
	pip install -r requirements.txt

install:
	pip install -e .

time_run: $(PROG)
	/usr/bin/time -p -v python3 $(PROG)

multitime_run: $(PROG)
	multitime -n 50 -v python3 $(PROG)

run: $(PROG)
	python3 $(PROG)

cpu_profiler_cum: $(PROG)
	python3 -m cProfile -s cumulative $(PROG)

cpu_profiler_out: $(PROG)
	python3 -m cProfile -o profile.stats $(PROG)

line_profiler: $(PROG)
	kernprof -l -v $(PROG)

memory_profiler: $(PROG)
	python3 -m memory_profiler $(PROG)

.PHONY: cython
cython:
	python3 setup.py build_ext --inplace

snakeviz:
	snakeviz profile.stats

tox:
	tox -e py39

.PHONY: test
test:
	pytest tests

.PHONY: coverage
coverage:
	pytest --cov=src --cov-report=html tests

.PHONY: clean
clean:
	rm -rf __pycache__

markdown:
	pandoc --from=rst --to=markdown --output=README.md README.rst
