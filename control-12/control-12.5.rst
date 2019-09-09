12.5: Configure Monitoring Systems to Record Network Packets
=============================================================
Configure monitoring systems to record network packets passing through the boundary at each of the organization’s network boundaries.

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
* Subcontrol 2.1: Maintain Inventory of Authorized Software
* Subcontrol 12.1: Maintain an Inventory of Network Boundaries

Inputs
-----------
#. List of network monitoring systems
#. List of network boundaries

Operations
----------
#. For each network monitoring system:
	#. Retrieve configuration
	#. Check configuration for recording
	#. Enumerate network boundaries covered

Measures
--------
* M1 = Count of network monitoring systems
* M2 = Count of misconfigured network monitoring systems
* M3 = Count of network boundaries
* M4 = Count of network boundaries covered by network monitoring systems


Metrics
-------

Monitoring System Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of appropriately configured monitoring systems
	* - **Calculation**
	  - :code:`(M1 - M2) / M1`

Network Boundary Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of network boundaries not covered by a monitoring system
	* - **Calculation**
	  - :code:`(M3 - M4) / M3`

.. history
.. authors
.. license