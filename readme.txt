Author: Aveek Podder

Content: 153070032.tex - tex file generating the PDF report for pendulum with friction sytem.
	 153070032.bib - Contains the bibliography.
	 pendulum_friction.py - Python file - Contains the code for generating the phase_plot and inter_state_plot of a pendulum with friction system. 
	 test_pendulum_friction.py - Python file - Contains test for pendulum_friction.py.
	 153070032.ipynb - ipython notebook file contains the code for animation of pendulum with friction system.
	 makefile - contains code to run everything with one command


Instructions for running:
	
	make first_run : Creates a folder name Source and moves the source program in it, it is only used for the first time. It is mandatory to run it for the first time
	
	make :  Compiles the source program and generates pdf and html report file, creates a folder named output and places pdf and html report file in it.
		
	make clean : Deletes Output folder

	make test : Test the correctness of the code pendulum_friction.py

