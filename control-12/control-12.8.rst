12.8: Deploy NetFlow Collection on Networking Boundary Devices
==============================================================
Enable the collection of NetFlow and logging data on all network boundary devices.

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
#. List of network boundary devices (from inventory)

Assumption
^^^^^^^^^^
* Assumes organization has positive control over inventory - explicitly ignores the case where there may be a network boundary device present and not accounted for (if other controls are working, this should not be the case). 

Operations
----------
#. For each network boundary device,
	#. Check configuration for NetFlow data (i.e. NetFlow is enabled)
	#. Check configuration for logging data (i.e. logging is enabled)

Measures
--------
* M1 = Count of network boundary devices
* M2 = Count of network boundary devices with NetFlow enabled
* M3 = Count of network boundary devices with logging enabled
* M4 = Count of network boundary devices with both NetFlow and logging enabled

Metrics
-------

NetFlow Coverage
^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of network boundary devices with misconfigured NetFlow
	* - **Calculation**
	  - :code:`(M1 - M2) / M1`


Logging Coverage
^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of network boundary devices with misconfigured logging
	* - **Calculation**
	  - :code:`(M1 - M3) / M1`


Total Coverage
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of misconfigured network boundary devices
	* - **Calculation**
	  - :code:`(M1 - M4) / M1`
.. history
.. authors
.. license