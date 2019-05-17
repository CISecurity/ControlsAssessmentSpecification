2.1: Maintain Inventory of Authorized Software
==============================================
Maintain an up-to-date list of all authorized software that is required in the enterprise for any business purpose on any business system.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Identify
	  - 1, 2, 3

Status
------
Draft

Assumptions
-----------
The authorized software list is maintained as the list of anything that's allowed to be installed.  Software inventory implies correlation between
endpoints and software load.


Measures
--------
* M1 = number of softwares discovered
* M2 = total number of softwares in the system
* M3 = time a whitelisted software discovered
* M4 = time a software appears in whitelist
* M5 = max time discovery


Metrics
-------

Coverage (Quality Measure)
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - 
	* - **Answer**
	  - 
	* - **Calculation**
	  - :code:`(M1 * Quality) / (M2 * Best Quality)`

Freshness (Time to Discover)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - 
	* - **Answer**
	  - 
	* - **Calculation**
	  - :code:`((M3-M4) / M5)`

.. history
.. authors
.. license