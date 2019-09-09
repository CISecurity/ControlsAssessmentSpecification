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

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. The list of approved wireless access points connected to the network
#. The list of WIDS sensors

Operations
----------
#. For each WIDS sensor, enumerate the approved wireless access points covered

Measures
--------
* M1 - Count of approved wireless access points
* M2 - Count of WIDS sensors
* M3 - Count of approved wireless access points covered by WIDS sensors

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of wireless access points not covered by WIDS sensors
	* - **Calculation**
	  - :code:`(M1 - M3) / M1`

.. history
.. authors
.. license