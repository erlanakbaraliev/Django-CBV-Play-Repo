.PHONY: run
run: export PYTHONPATH=$(PWD)/apps
run:
	python3 manage.py runserver_plus 8001

.PHONY: shell
shell: export PYTHONPATH=$(PWD)/apps
shell:
	python3 manage.py shell_plus
