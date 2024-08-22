MAKEFLAGS += -s

.PHONY: help run debug freeze sort publish test lint format clean install dev-install build check all

default: run

help:
	@echo "⚈ run			---> 🎮 Run project locally (default)."
	@echo "⚈ debug			---> 🕵️  Debug project locally."
	@echo "⚈ freeze		---> 🧊 Freeze requirements."
	@echo "⚈ sort			---> ⬇️  Sort requirements and env files alphabetically."
	@echo "⚈ publish		---> 🚀 Build and publish a new package version."
	@echo "⚈ test			---> 🧪 Run tests."
	@echo "⚈ lint			---> 🔍 Run linter."
	@echo "⚈ format		---> 💅 Format code."
	@echo "⚈ clean			---> 🧹 Remove build artifacts."
	@echo "⚈ install		---> 📦 Install the package."
	@echo "⚈ dev-install	---> 🛠️  Install the package in editable mode with dev dependencies."
	@echo "⚈ build			---> 🏗️  Build the package."
	@echo "⚈ check			---> ✅ Run tests and linter."
	@echo "⚈ all			---> 🔄 Clean, install, test, lint, and format."

run:
	@echo "\n> 🎮 Running the project locally... (default)\n"

debug:
	@echo "\n> 🕵️  Debugging the project locally...\n"

freeze:
	@echo "\n> 🧊 Freezing the requirements...\n"
	@for file in requirements*.txt; do \
		if [ -f $$file ]; then \
			pip3 freeze -q -r $$file | sed '/freeze/,$$ d' > requirements-froze.txt && mv requirements-froze.txt $$file; \
			echo "Froze requirements in $$file"; \
		else \
			echo "$$file not found, skipping..."; \
		fi \
	done
	@python src/update_pyproject.py

sort:
	@echo "\n> ⬇️ Sorting requirements and env files alphabetically...\n"
	@for file in requirements*.txt; do \
		if [ -f $$file ]; then \
			sort --ignore-case -u -o $$file{,}; \
			echo "Sorted $$file"; \
		else \
			echo "$$file not found, skipping..."; \
		fi \
	done
	@for file in .env*; do \
		if [ -f $$file ]; then \
			sort --ignore-case -u -o $$file{,}; \
			echo "Sorted $$file"; \
		else \
			echo "$$file not found, skipping..."; \
		fi \
	done

publish:
	@echo "\n> 🚀 Building and publishing a new package version...\n"
	@echo "\n> 📦 Installing build dependencies...\n"
	pip install -r requirements-build.txt
	@echo "\n> 🗑️ Erasing previous build...\n"
	rm -rf src/dist
	@echo "\n> ⬆️ Bumping package version...\n"
	bump2version patch --verbose
	@echo "\n> 🔨 Building package...\n"
	python -m build src
	@echo "\n> 🌐 Uploading package to Test PyPi...\n"
	python -m twine upload --repository yatl-python src/dist/*

test:
	@echo "\n> 🧪 Running tests...\n"
	pytest tests/

lint:
	@echo "\n> 🔍 Running linter...\n"
	flake8 src/ tests/
	mypy src/ tests/

format:
	@echo "\n> 💅 Formatting code...\n"
	black src/ tests/
	isort src/ tests/

clean:
	@echo "\n> 🧹 Removing build artifacts...\n"
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete

install:
	@echo "\n> 📦 Installing the package...\n"
	pip install .

dev-install:
	@echo "\n> 🛠️ Installing the package in editable mode with dev dependencies...\n"
	pip install -e ".[dev]"

build:
	@echo "\n> 🏗️ Building the package...\n"
	python -m build

check: test lint

all: clean install test lint format
