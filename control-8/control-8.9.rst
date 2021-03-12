8.9: Centralize Audit Logs
=========================================================
Centralize, to the extent possible, audit log collection and retention across enterprise assets.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Detect
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
------
#. :code:`GV27`: Assets capable of supporting logging
#. :code:`GV5`: Authorized software inventory

Operations
----------
#. Use the software inventory :code:`GV5` to identify and enumerate log aggregating software :code:`GV28`
#. For each asset capable of supporting logging, check if asset is covered by at least one log aggregating software
	#. Identify and enumerate assets covered by at least one aggregating software (M2)
	#. Identify and enumerate assets not covered by at least one aggregating software (M3)

Measures
----------
* M1 = Count of :code:`GV27`
* M2 = Count of assets covered by at least one aggregating software
* M3 = Count of assets not covered by at least one aggregating software

Metrics
-------

Log Aggregating
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of log producing assets covered by aggregating
	    | software.
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
