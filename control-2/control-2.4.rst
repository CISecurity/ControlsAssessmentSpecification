2.4: Utilize Automated Software Inventory Tools
=========================================================
Utilize software inventory tools, when possible, throughout the enterprise to automate the discovery and documentation of installed software.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Detect
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory

Inputs
------
#. Detailed enterprise asset inventory
#. List of software inventory tools

Operations
----------
#. Use Input 1 to identify software capable assets.
	#. Note software capable assets (M1)
	#. Note assets unable to support software (M2)
#. For each software capable asset identified in Operation 1
	#. Identify and note if the asset is covered by at least one software inventory tool (M3)
	#. Identify and note if the asset is not covered by at least one software inventory tool (M4)

Measures
--------
* M1 = Count of software capable assets
* M2 = Count of assets unable to to support software
* M3 = Count of assets covered by software inventory tools
* M4 = Count of assets not covered by software inventory tools
* M5 = Count of Input 2

Metrics
-------
* If M5 is 0 or unavailable, then this safeguard is measured at a 0 and receives a failing score. The other metrics don’t apply.

Inventory Tool Coverage
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of endpoints covered by software inventory tools to the total
	  - | number of applicable endpoints
	* - **Calculation**
	  - :code:`M3 / M1`

.. history
.. authors
.. license
