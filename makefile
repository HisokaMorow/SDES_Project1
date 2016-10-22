./source/153070032.pdf: ./source/fig(1).png ./source/fig(2).png ./source/153070032.tex ./source/153070032.bbl ./source/153070032.blg ./source/153070032.html
	if [ ! -d ./output ]; then mkdir output; mv *.bib *.ipynb *.tex *.py ./source; fi
	cd ./source && pdflatex 153070032.tex
	cd ./source && pdflatex 153070032.tex
	mv ./source/153070032.pdf ./output/153070032.pdf
	cd ./source && rm -f *.aux *.log *.blg *.bbl *.png *.toc *.pyc *.html

./source/153070032.html: ./source/153070032.ipynb
	cd ./source && ipython nbconvert 153070032.ipynb
	if [ ! -d ./output ]; then mkdir output; fi
	mv ./source/153070032.html ./output/153070032.html

./source/fig(1).png ./source/fig(2).png: ./source/pendulum_friction.py
	cd ./source && python pendulum_friction.py

./source/153070032.bbl ./source/153070032.blg: ./source/153070032.bib
	cd ./source && pdflatex 153070032.tex
	cd ./source && bibtex 153070032

test:
	cd ./source && python test_pendulum_friction.py
	cd ./source && rm -f *.pyc

first_run:
	if [ ! -d ./source ]; then mkdir source; mv *.bib *.ipynb *.tex *.py ./source; fi

.PHONY: clean

clean:
	rm -rf ./output
