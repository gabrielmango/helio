.PHONY: run i f t  c

# Run the projet
run:
	@poetry shell
	
# Install dev dependences
i:
	@poetry add --group dev pytest pip-audit isort mkdocs black prospector
	@pylint --generate-rcfile > .pylintrc
	@mkdocs new .
	@pip-audit

# Format the code
f:
	@isort .
	@black .

# Teste the code 
t:
	@pytest tests/test_user.py

# Preper project to commit
c:
	@isort .
	@black .
	@pytest -v
	@prospector --with-tool pydocstyle