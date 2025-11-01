.PHONY: all

all: clean build push publish

clean:
	jupyter-book clean .
	rm -rf .jupyter_cache

build:
	/home/codespace/.python/current/bin/jupyter-book build .
	cp -r _output _build/html/lite

push:
	git add .
	git commit -m "Build and publish site"
	git push

publish:
	# cp readme.md _build/html/
	# cp _toc.yml _build/html/
	ghp-import -n -p -f _build/html

push-readme:
	# cp  _build/html/readme.md /
	# cp  _build/html/_toc.yml /
	# git add readme.md _toc.yml
	# git commit -m "Update README and ToC"
	# git push