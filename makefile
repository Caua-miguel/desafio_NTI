# Variables
PYTHON = python
PIP = pip

# Install dependencies
install:
	$(PIP) install -r requirements.txt

# Run tests
test:
	$(PYTHON) -m pytest tests/

# # Format code using black
# format:
#     $(PYTHON) -m black src/ tests/

# # Lint code using flake8
# lint:
#     $(PYTHON) -m flake8 src/ tests/

# Clean up temporary files
clean:
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +