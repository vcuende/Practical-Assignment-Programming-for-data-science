Here you can see the general hierarchy of our code:

- Final assignment Group-2
   - assets_historical_prices
	* amundi-msci-wrld-ae-c_investing.csv
	* db-x-trackers-ii-global-sovereign-5_investing.csv
	* ishares-global-corporate-bond-$_investing.csv
	* spdr-gold-trust_investing.csv
	* usdollar_investing.csv
   - files
	- all
	    * all.csv
	    * all_2.csv
	- cash
	    * usdollar.csv
	- corporate bonds
	    * ishares-global-corporate-bond-$.csv
	- gold
	    * spdr-gold-trust.csv
	- public bonds
	    * db-x-trackers-ii-global-sovereign-5.csv
	- stocks
	    * amundi-msci-wrld-ae-c.csv
	- task_2
	    * portfolio_allocations.csv
	    * portfolio_metrics.csv
   * geckodriver
   * README.txt
   * merge_datasets.py
   * portfolio_part_2.ipynb
   * web_scrapping_cash.py
   * web_scrapping_corporate_bonds.py
   * web_scrapping_gold.py
   * web_scrapping_public_bonds.py
   * web_scrapping_stocks.py
   * Report.pdf


Our project is divided in several files and directories:

- "assets_historical_prices": here you can find the 5 data assets provided by the professors (found in Moodle)
- "files": here it can be seen the 5 data assets that we have extracted by applying web scrapping, as well as the merge datasets used for the "data generation" part
- "geckodriver": the driver needed to use Firefox for web scrapping. IMPORTANT: In order to run our code, the path which uses this file needs to be change to the path where the geckodriver file has been downloaded/inserted
- "merge_datasets.py": file created to merge the 5 data assets (either the ones from the professors or the ones that we have created)
- "portfolio_part_2.ipynb": notebook created to address the "data generation" and "data analysis" parts
- "web_scrapping_cash.py": file created to perform web scrapping on the cash webpage
- "web_scrapping_corporate_bonds.py": file created to perform web scrapping on the corporate bonds webpage
- "web_scrapping_gold.py": file created to perform web scrapping on the gold webpage
- "web_scrapping_public_bonds.py": file created to perform web scrapping on the public bonds webpage
- "web_scrapping_stocks.py": file created to perform web scrapping on the stocks webpage
- "Report.pdf": file created to perform the analysis and answer the questions of the last part of the project



Moreover, each file and their functionalities belongs to one of these parts:

Web Scrapping part: to run this part of our code, you need to have, apart from everything explained here, Firefox installed.
- "files": inside this directory, the subdirectories related to this part (cash, corporate bonds, gold, public bonds and stocks)
- "geckodriver"
- "web_scrapping_cash.py"
- "web_scrapping_corporate_bonds.py"
- "web_scrapping_gold.py"
- "web_scrapping_public_bonds.py"
- "web_scrapping_stocks.py"


Data Generation part: to run this part of our code, you need to have the requirements mentioned below as well as all the files described here
- "assets_historical_prices":
- "files": inside this directory, the subdirectories related to this part (all, task_2)
- "merge_datasets.py"
- "portfolio_part_2.ipynb"


Data Analysis part: to run this part of our code, you need to have the requirements mentioned below as well as all the files described here
- "portfolio_part_2.ipynb"
- "Report.pdf"




Packages and versions requirements are the following:

For the Web Scrapping part:
- selenium==3.141.0
- pandas==1.3.3


For the Data Generation part:
- pandas==1.3.3
- numpy==1.22.3


For the Data Analysis part:
- pandas==1.3.3
- matplotlib==3.7.0




