13.3: Monitor and Block Unauthorized Network Traffic
=========================================================
Deploy an automated tool on network perimeters that monitors for unauthorized transfer of sensitive information and blocks such transfers while alerting information security professionals.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Detect
	  - 3

Status
------
Draft

Dependencies
------------
* Sub-control 2.1: Maintain Inventory of Authorized Software
* Sub-control 12.1: Maintain an Inventory of Network Boundaries

Inputs
-----------
#. The list of authorized software
#. The list of network perimeters

Operations
----------
#. Enumerate all network perimeter monitoring systems
#. For each network perimeter monitoring system:
	#. Enumerate the network perimeters covered by the system
	#. Examine its configuration to ensure that the system is configured to:
		#. Monitor for sensitive information
		#. Block transfer of detected sensitive information
		#. Alert appropriately
#. Enumerate network perimeters covered by all network perimeter monitoring systems
#. Complement the set of covered network perimeters with the list of network perimeters to identify all uncovered network perimeters

Assumptions
^^^^^^^^^^^
* Network perimeter monitoring systems are primarily software-based


Measures
--------
* M1 = List of network perimeter monitoring systems
* M2 = List of network perimeters
* M3 = List of appropriately configured perimeter monitoring systems
* M4 = List of inappropriately configured perimeter monitoring systems
* M5 = List of network perimeters covered by at least one network perimeter monitoring system
* M6 = List of network perimeters not covered by at least one network perimeter monitoring system
* M7 = Count of network perimeter monitoring systems (count of M1)
* M8 = Count of network perimeters (count of M2)
* M9 = Count of appropriately configured perimeter monitoring systems (count of M3)
* M10 = Count of inappropriately configured perimeter monitoring systems (count of M4)
* M11 = Count of network perimeters covered by at least one network perimeter monitoring system (count of M5)
* M12 = Count of network perimeters not covered by at least one network perimeter monitoring system (count of M6)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of covered network perimeters to the total number of network perimeters
	* - **Calculation**
	  - :code:`M11 / M8`

Perimeter Monitoring Configuration Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured network perimeter monitoring systems to the total
	    | number of network perimeter monitoring systems
	* - **Calculation**
	  - :code:`M9 / M7`

.. history
.. authors
.. license
