11.4: Install the Latest Stable Version of Any Security-Related Updates on All Network Devices
==============================================================================================
Install the latest stable version of any security-related updates on all network devices.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. Network device inventory, derived from the endpoint inventory (see sub-control 1.4)
#. Network device version information (this is a list of acceptable versions for each model of network device in Input 1; this version information needs to be updated frequently to reflect current version information and age off outdated versions)

Operations
----------
#. For each network device in Input 1, compare the network device's version to the allowable versions from Input 2.
#. Generate a list of those network devices that match an allowable version (M1)
#. Generate a list of those network devices that do not match an allowable version (M2).

Measures
--------
* M1 = List of network devices
* M2 = Count of M1
* M3 = List of network devices that match an allowable version (compliant list)
* M4 = Count of M3
* M5 = List of network devices that do not match an allowable version (non-compliant list)
* M6 = Count of M5

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of inventoried network devices match the allowable version for that
	    | device/OS?
	* - **Calculation**
	  - If M2 > 0, then :code:`M4 / M2`; otherwise :code:`0`

.. history
.. authors
.. license
