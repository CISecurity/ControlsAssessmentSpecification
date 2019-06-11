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
In Development

Inputs
------
#. A list of authorized software (M2) is known to the organization
#. The time software appears (M4) is known to us since we are installing the software
#. Max software discovery time (M5) is defined by the organization

Operations
----------
#. 

Measures
--------
* M1 = number of softwares discovered
* M2 = total number of softwares in the system
* M3 = time a whitelisted software discovered
* M4 = time a software appears
* M5 = max time discovery


Metrics
-------

Coverage (Quality Measure)
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | The coverage metric intends to determine what percentage of software discovered
	    | in the enterprise is maintained in the software inventory.
	* - **Answer**
	  - | By dividing the number of discovered software assets in the enterprise, by the
	    | total number tracked in the software inventory, an enterprise can determine this
	    | coverage percentage and evaluate those software assets which have been installed
	    | but are not tracked by the software inventory.
	* - **Calculation**
	  - :code:`(M1 / M2) * 100`

Freshness (Time to Discover)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | The freshness metric intends to determine the percentage of the maximum discovery
	    | time that it takes to discover new software installed in the enterprise
	* - **Answer**
	  - | This calculation will yield a value greater than or equal to 0, with 0 indicating
	    | the software was discovered immediately, a value less than 1 indicating the software
	    | was discovered in an amount of time less than the current maximum, and any value
	    | greater than 1 indicates the discovery of the newly installed software took longer
	    | than the currently established maximum time (M5).
	* - **Calculation**
	  - :code:`((M3-M4) / M5)`

.. history
.. authors
.. license