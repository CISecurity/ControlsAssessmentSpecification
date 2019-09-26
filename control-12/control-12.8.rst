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

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 12.1: Maintain an Inventory of Network Boundaries

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
* M1 = Count of network boundary devices (from Input 1)
* M2 = List of network boundary devices with NetFlow enabled
* M3 = Count of M2
* M4 = List of network boundary devices without NetFlow enabled
* M5 = Count of M4
* M6 = List of network boundary devices with logging enabled
* M7 = Count of M6
* M8 = List of network boundary devices without logging enabled
* M9 = Count of M8
* M10 = List of network boundary devices with both NetFlow and logging enabled
* M11 = Count of M10
* M12 = List of network boundary devices with either NetFlow or logging disabled
* M13 = Count of M12

Metrics
-------

NetFlow Coverage
^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of network boundary devices with appropriately configured NetFlow to the total number of network boundary devices
	* - **Calculation**
	  - :code:`M3 / M1`


Logging Coverage
^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of network boundary devices with appropriately configured logging to the total number of network boundary devices
	* - **Calculation**
	  - :code:`M7 / M1`


Total Coverage
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of appropriately configured network boundary devices to the total number of network boundary devices
	* - **Calculation**
	  - :code:`M11 / M1`
.. history
.. authors
.. license
