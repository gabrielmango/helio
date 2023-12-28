.PHONY: run i f t  c

# Run the projet
run:
	@poetry install
	@poetry shell

# Install dev dependences
i:
	@poetry add --group dev pytest pip-audit isort mkdocs blue pylint
	@pylint --generate-rcfile > .pylintrc
	@mkdocs new .
	@pip-audit

# Format the code
f:
	@isort .
	@blue .

# Teste the code 
t:
	@pytest .

# Preper project to commit
c:
	@isort .
	@blue .
	@pytest -v
	@pylint .