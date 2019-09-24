13.5: Monitor and Detect Any Unauthorized Use of Encryption
===========================================================
Monitor all traffic leaving the organization and detect any unauthorized use of encryption.

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
* Subcontrol 2.1: Maintain Inventory of Authorized Software
* Subcontrol 12.1: Maintain an Inventory of Network Boundaries

Inputs
-----------
#. The list of authorized software
#. The list of network boundaries at the organization's perimeter
#. Unauthorized encrypted connections

Operations
----------
#. Enumerate all network monitoring systems in the software inventory
#. For each network monitoring system
	#. Enumerate the network boundaries covered by the system
	#. Examine its configuration to ensure that the system is configured to monitor for unauthorized encrypted connections
#. Enumerate network boundaries covered by all network monitoring systems (i.e. create a set of covered network boundaries)
#. Complement the set of covered network boundaries with the list of network boundaries to identify all uncovered network boundaries

Measures
--------
* M1 = List of all network monitoring systems
* M2 = List of network boundaries at the perimeter
* M3 = List of appropriately configured network monitoring systems
* M4 = List of inappropriately configured network monitoring systems
* M5 = List of network boundaries covered by at least one network monitoring system
* M6 = List of network boundaries not covered by at least one network monitoring system
* M7 = The number of network monitoring systems (count of M1)
* M8 = The number of network boundaries at the perimeter (count of M2)
* M9 = The number of appropriately configured network monitoring systems (count of M3)
* M10 = The number of inappropriately configured network monitoring systems (count of M4)
* M11 = The number of network boundaries covered by at least one network monitoring system (count of M5)
* M12 = The number of network boundaries not covered by at least one network monitoring system (count of M6)

Metrics
-------

Network Monitoring Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured network monitoring systems to the total number
	    | of network monitoring systems
	* - **Calculation**
	  - :code:`M9 / M7`

Network Boundary Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of covered network boundaries to the total number of network boundaries
	* - **Calculation**
	  - :code:`M11 / M8`

.. history
.. authors
.. license