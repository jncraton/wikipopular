all: pages.txt

pages.txt:
	python3 build.py > pages_unsorted.txt
	sort -n -r pages_unsorted.txt | uniq > pages.txt
