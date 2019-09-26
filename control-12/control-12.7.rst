12.7: Deploy Network-Based Intrusion Prevention Systems
=========================================================
Deploy network-based Intrusion Prevention Systems (IPS) to block malicious network traffic at each of the organization’s network boundaries.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 3

Dependencies
------------
* Sub-control 2.1: Maintain Inventory of Authorized Software
* Sub-control 12.1: Maintain an Inventory of Network Boundaries

Inputs
-----------
#. The list of authorized software
#. The list of network boundaries

Operations
----------
#. Enumerate all IPS systems in the software inventory
#. For each IPS system:
	#. Enumerate the network boundaries covered by the system
	#. Examine its configuration to ensure that the system is configured to block malicious network traffic through that boundary
#. Enumerate network boundaries covered by all IPS systems (i.e. create a set of covered network boundaries)
#. Complement the set of covered network boundaries with the list of network boundaries to identify all uncovered network boundaries

Measures
--------
* M1 = List of all IPS systems
* M2 = List of network boundaries
* M3 = List of appropriately configured IPS systems
* M4 = List of inappropriately configured IPS systems
* M5 = List of network boundaries covered by at least one IPS system
* M6 = List of network boundaries not covered by at least one IPS system
* M7 = Count of IPS systems (count of M1)
* M8 = Count of network boundaries (count of M2)
* M9 = Count of appropriately configured IPS systems (count of M3)
* M10 = Count of inappropriately configured IPS systems (count of M4)
* M11 = Count of network boundaries covered by at least one IPS system (count of M5)
* M12 = Count of network boundaries not covered by at least one IPS system (count of M6)

Metrics
-------

IPS Coverage
^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured IPS systems to the total number of IPS systems
	* - **Calculation**
	  - :code:`M9 / M7`

Boundary Coverage
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of covered network boundaries to the total number of network boundaries
	* - **Calculation**
	  - :code:`M11 / M8`

.. history
.. authors
.. license
