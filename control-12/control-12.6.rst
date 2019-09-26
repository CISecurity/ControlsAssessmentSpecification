12.6: Deploy Network-Based IDS Sensors
=========================================================
Deploy network-based Intrusion Detection Systems (IDS) sensors to look for unusual attack mechanisms and detect compromise of these systems at each of the organization’s network boundaries.

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
* Sub-control 12.1: Maintain an Inventory of Network Boundaries

Inputs
-----------
#. List of network boundaries
#. List of IDS sensors

Operations
----------
#. For each IDS sensor, enumerate network boundaries covered

Measures
--------
* M1 = Count of network boundaries (from Input 1)
* M2 = Count of IDS sensors (from Input 2)
* M4 = List of network boundaries covered by IDS sensors
* M5 = Count of network boundaries covered by IDS sensors
* M6 = List of network boundaries not covered by IDS sensors
* M7 = Count of network boundaries not covered by IDS sensors

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of network boundaries covered by IDS sensors to total number of network boundaries 
	* - **Calculation**
	  - :code:`M5 / M1`

.. history
.. authors
.. license
