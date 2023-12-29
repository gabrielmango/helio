.PHONY: run i f t  c branch

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
	@black tests
	@black helio
	@python scripts/replace_quotes.py

# Teste the code 
t:
	@pytest tests/test_sequence.py

# Preper project to commit
c:
	@isort .
	@black tests
	@black helio
	@pytest -v
	@prospector --with-tool pydocstyle

branch:
	@git checkout main
	@git pull