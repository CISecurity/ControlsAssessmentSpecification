16.8: Separate Production and Non-Production Systems
=========================================================
Maintain separate environments for production and non-production systems.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 2, 3

Dependencies
------------
* None

Inputs
-----------
#. :code:`GV1`: Enterprise Asset Inventory

Operations
----------
#. Use Input 1 :code:`GV1` to identify and enumerate productions systems (M1)
#. For each production system identified in Operation 1, use Input 1 :code:`GV1` to identify if at least one non-production system exists for the system
	#. Identify and enumerate productions systems with at least one non-production system (M2)
	#. Identify and enumerate productions systems without a non-production system (M3)

Measures
--------
* M1 = Count of production systems
* M2 = Count of production systems with a non-production system to complement 
* M3 = Count of productions systems without a non-production system to complement

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of productions systems with an existing 
	  - | non-production system
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
