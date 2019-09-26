1.3: Use DHCP Logging to Update Asset Inventory
=========================================================
Use Dynamic Host Configuration Protocol (DHCP) logging on all DHCP servers or IP address management tools to update the organization’s hardware asset inventory.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Identify
	  - 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory

Inputs
-----------
#. The list of DHCP servers
#. The list of CMDB servers (i.e. asset inventory systems)

Operations
----------
#. For each DHCP server, check whether DHCP logging is enabled
#. For each CMDB server, check whether DHCP logs are used to update IP addresses

Assumptions
^^^^^^^^^^^
* CMDB servers are configured to pull from DHCP logs

Measures
--------
* M1 = Count of DHCP servers (using Input 1)
* M2 = List of DHCP servers with logging enabled
* M3 = Count of M2
* M4 = Count of CMDB servers (using Input 2)
* M5 = List of CMDB servers configured to use DHCP logs to update IP addresses
* M6 = Count of M5
* M7 = List of devices in the DHCP server logs that are not included in the CMDB servers
* M8 = Count of M7
* M9 = List of devices in the DHCP server logs that are included in the CMDB servers
* M10 = Count of M9

Metrics
-------
* M5 > 0 indicates a non up-to-date asset inventory

DHCP Logging Quality
^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of appropriately configured DHCP logging enabled to known DHCP servers
	* - **Calculation**
	  - :code:`M3 / M1`

CMDB Configuration Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of appropriately configured CMDB servers using DHCP logging to update
	    | IP addresses
	* - **Calculation**
	  - :code:`M6 / M4`

.. history
.. authors
.. license
