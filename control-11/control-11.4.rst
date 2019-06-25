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

Status
------
Draft

Inputs
-----------
#. Network device inventory
#. Network device version information (this is a list of acceptable versions for each model of network device in Input 1; this version information needs to be updated frequently to reflect current version information and age off outdated versions)

Operations
----------
#. For each network device in Input 1, compare the network device's version to the allowable versions from Input 2. Generate a list of those network devices that match an allowable version (M1) and a list of those network devices that do not match an allowable version (M2).

Measures
--------
* M1 = List of network devices that match an allowable version (compliant list)
* M2 = List of network devices that do not match an allowable version (non-compliant list)
* M3 = Number of network devices in Input 1

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Question**
	  - | What percentage of inventoried network devices match the allowable version for that
	    | device/OS?
	* - **Answer**
	  - 
	* - **Calculation**
	  - If M3 > 0, then :code:`M1 / M3`; otherwise `0`

.. history
.. authors
.. license