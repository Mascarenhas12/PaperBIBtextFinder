This is a program with the purpose of getting bibtex out of papers through web scrapping
thus it will require internet and, in particular, it will require Google Chrome (you can change it code if you prefer another
browser just be aware as bugs might appear if you change something you aren't supposed).

This is originally made for phD student in Economics therefore if you have no economic papers just don't use the working paper functionality
and the program will research the paper normally through google schoolar.

The program will go through each file in papers folder and search its name (which needs to be the title of the paper for a better chance
to find the right paper) and it will search it on google schollar or NBER (if it's a working paper and you need to add "wp" to the title of each working
paper).

ATTENTION! THIS WILL ONLY TRY TO GET THE BIBTEX OUT OF THE FIRST PAPER IT FINDS SO IT MAY NOT BE THE CORRECT PAPER. AFTERWARDS CHECK IF THE OUTPUT
MAKES SENSE ACCORDING TO EACH SEARCH.

OUTPUT WILL BE IN THIS FORMAT:

	name of file 1

	bibtex or error message

	name of file 2
	...

Enable first the setup(test script) by going in the terminal and doing command:
	chmod +x setup.sh
Run setup.sh and when it asks for user password write your password (this is needed in order to download chrome webdriver
alternatively comment out the line "sudo install chromium webdriver" with # before sudo. You will need to install it for yourself before you can run
the script.)

After it finishes check setup.txt and verify that in the end there is this output (order may vary):

A Crash Course on the Euro Crisis wp

% WARNING: This file may contain UTF-8 (unicode) characters.
% While non-8-bit characters are officially unsupported in BibTeX, you
% can use them with the biber backend of biblatex
%    usepackage[backend=biber]{biblatex}

@techreport{NBERw26229,
 title = "A Crash Course on the Euro Crisis",
 author = "Brunnermeier, Markus K and Reis, Ricardo",
 institution = "National Bureau of Economic Research",
 type = "Working Paper",
 series = "Working Paper Series",
 number = "26229",
 year = "2019",
 month = "September",
 doi = {10.3386/w26229},
 URL = "http://www.nber.org/papers/w26229",
 abstract = {The financial crises of the last twenty years brought new economic concepts into classrooms discussions. This article introduces undergraduate students and teachers to seven of these models: (i) misallocation of capital inflows, (ii) modern and shadow banks, (iii) strategic complementarities and amplification, (iv) debt contracts and the distinction between solvency and liquidity, (v) the diabolic loop, (vi) regional flights to safety, and (vii) unconventional monetary policy. We apply each of them to provide a full account of the euro crisis of 2010-12.},
}

damdapo9dj2m3dna0dh

Couldn't find anything in search

The Sources of Capital Misallocation

@techreport{david2017sources,
  title={The sources of capital misallocation},
  author={David, Joel M and Venkateswaran, Venky},
  year={2017},
  institution={National Bureau of Economic Research}
}

If output correct than everything is setup correctly so just copy every paper onto papers(DON'T FORGET TO RENAME EACH PAPER TO IT'S 
TITLE! IF IT'S A WORKING PAPER JUST ADD 'wp' TO THE END OF THE TITLE) folder, then do "chmod +x test.sh" in terminal.
After that you can run the test.sh script and everything should be fine.
