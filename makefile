all: pages.tsv

pages.tsv:
	python3 build.py > pages_unsorted.tsv
	sort -n -r pages.tsv | uniq > pages.tsv