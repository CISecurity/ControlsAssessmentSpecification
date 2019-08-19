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

Status
------
Draft

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
* M1 = Count of DHCP servers
* M2 = Count of DHCP servers with logging enabled
* M3 = Count of CMDB servers
* M4 = Count of CMDB servers configured to use DHCP logs to update IP addresses
* M5 = Number of devices in the DHCP server logs that are not included in the CMDB servers

Metrics
-------
* M5 > 0 indicates a non up-to-date asset inventory

DHCP Logging Quality
^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Ratio of appropriately configured DHCP logging enabled to known DHCP servers**
	  - :code:`M2 / M1`

^^^^^^^^^^^^^^
.. list-table::

	* - **Ratio of appropriately configured CMDB servers using DHCP logging to update IP addresses**
	  - :code:`M4 / M3`

.. history
.. authors
.. license