15.3: Use a Wireless Intrusion Detection System
=========================================================
Use a wireless intrusion detection system (WIDS) to detect and alert on unauthorized wireless access points connected to the network.

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
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. The list of approved wireless access points connected to the network
#. The list of WIDS sensors

Operations
----------
#. For each WIDS sensor, enumerate the approved wireless access points covered

Measures
--------
* M1 - Count of approved wireless access points (from Input 1)
* M2 - Count of WIDS sensors (from Input 2)
* M3 = List of approved wireless access points covered by WIDS sensors
* M4 = Count of M3
* M5 = List of approved wireless access points not covered by WIDS sensors
* M6 = Count of M5

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of wireless access points covered by WIDS sensors to the total number of wireless access points
	* - **Calculation**
	  - :code:`M4 / M1`

.. history
.. authors
.. license
