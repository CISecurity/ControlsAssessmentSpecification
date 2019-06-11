1.3: Use DHCP Logging to Update Asset Inventory
=========================================================
Use Dynamic Host Configuration Protocol
(DHCP) logging on all DHCP servers or IP address
management tools to update the organization’s
hardware asset inventory.

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
In Development

Inputs
-----------

Operations
----------

Measures
--------
* M1 = # of log enabled DHCP server
* M2 = # of total DHCP server

Metrics
-------

DHCP Log Ratio
^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - What percentage of DHCP servers in the enterprise have logging enabled?
	* - **Answer**
	  - | This metric yields a percentage value, from 0 to 100%, indicating the ratio of DHCP
	    | servers to those with logging enabled.
	* - **Calculation**
	  - :code:`(M1/M2) * 100`

.. history
.. authors
.. license