2.8: Implement Application Whitelisting of Libraries
=========================================================
The organization’s application whitelisting software must ensure that only authorized software libraries (such as *.dll, *.ocx, *.so, etc.) are allowed to load into a system process.

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


Measures
--------
* M1 = # of libraries with whitelisting enabled
* M2 = # of libraries under consideration

Metrics
-------

Quality of software library authorization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - What percentage of authorized software libraries are allowed to be loaded per application whitelisting protocols?
	* - **Answer**
	  - The calculation of this metric yields a percentage, from 0 to 100%, indicating the ratio of software libraries that are whitelisted to the total number of software libraries.
	* - **Calculation**
	  - :code:`(M1/M2) * 100`

.. history
.. authors
.. license