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

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information
* Subcontrol 12.1: Maintain an Inventory of Network Boundaries

Inputs
-----------
#. List of network boundaries
#. List of IDS sensors

Operations
----------
#. For each IDS sensor, enumerate network boundaries covered

Measures
--------
* M1 = Count of network boundaries
* M2 = Count of IDS sensors
* M3 = Count of network boundaries covered by IDS sensors

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of network boundaries not covered by IDS sensors
	* - **Calculation**
	  - :code:`?`

.. history
.. authors
.. license