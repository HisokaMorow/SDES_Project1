Author: Aveek Podder

Content: 
	153070032.tex - tex file generating the PDF report for pendulum with friction sytem.

	 153070032.bib - Contains the bibliography.
	 pendulum_friction.py - Python file - Contains the code for generating the phase_plot and inter_state_plot of a pendulum with friction system.

	 test_pendulum_friction.py - Python file - Contains test for pendulum_friction.py.

	 153070032.ipynb - ipython notebook file contains the code for animation of pendulum with friction system.

	 makefile - contains code to run everything with one command

#######################################################################################################################################################################################################################

Software dependencies:

for running pendulum_friction.py and test_pendulum_friction.py:
	python version 2.7.12
	numpy 1.11.1
	scipy 0.18.1
	matplotlib 1.5.3

for running 153070032.ipynb:
	Ipython notebook-ipython version 2.4.1
	ffmpeg4

for running 153070032.tex and 153070032.bib
	pdfTeX 3.14159265-2.6-1.40.16

for running make file:
	GNU Make 4.1

################################################################################################################################################

Instructions for running:
	
	make first_run : Creates a folder name Source and moves the source program in it, it is only used for the first time. It is mandatory to run it for the first time
	
	make :  Compiles the source program and generates pdf and html report file, creates a folder named output and places pdf and html report file in it.
		
	make clean : Deletes Output folder

	make test : Test the correctness of the code pendulum_friction.py

