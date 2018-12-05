all: pages.tsv

pages.tsv:
	python3 build.py > pages.tsv