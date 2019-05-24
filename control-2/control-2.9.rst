2.9: Implement Application Whitelisting of Scripts
=========================================================
The organization’s application whitelisting software must ensure that only authorized, digitally signed scripts (such as *.ps1,*.py, macros, etc.) are allowed to run on a system.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 3

Status
------
Draft

Assumptions
-----------
The assumption is made that

Measures
--------
* M1 = # of scripts allowed in whitelisting tool
* M2 = # of assets under consideration

Metrics
-------

Quality of script authorization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - What percentage of authorized scripts are allowed to be executed per application whitelisting protocols?
	* - **Answer**
	  - The calculation of this metric yields a percentage, from 0 to 100%, indicating the ratio of scripts that are whitelisted to the total number of scripts.
	* - **Calculation**
	  - :code:`(M1/M2) * 100`

.. history
.. authors
.. license