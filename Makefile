.PHONY: get-dependencies

get-dependencies:
	./bin/get-dependencies.py | tsort | ./bin/reverse.py
