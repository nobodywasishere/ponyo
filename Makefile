install:
	python3 -m pip install .

docs:
	lazydocs \
		--output-path="./docs/docstrings" \
		--overview-file="README.md" \
		--src-base-url "https://github.com/nobodywasishere/ponyo/blob/master/" \
		ponyo
	mkdocs build

serve:
	python -m http.server --directory site

format:
	black ponyo/
	docstr-coverage \
		--skip-init \
		--skip-private \
		--skip-class-def \
		--skip-file-doc \
		-b docs/badge.svg \
		ponyo/

.PHONY: install docs serve format