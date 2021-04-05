12.1: Ensure Network Infrastructure is Up-to-Date
=========================================================
Ensure network infrastructure is kept up-to-date. Example implementations include running the latest stable release of software and/or using currently supported network-as-a-service (NaaS) offerings. Review software versions monthly, or more frequently, to verify software support.

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
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory

Inputs
-----------
#. :code:`GV1`: Enterprise asset inventory
#. Authoritative source of latest version information
#. Date of last review of network infrastructure 

Operations
----------
#. Use :code:`GV1` to identify and enumerate assets that are part of the network infrastructure :code:`GV35` (M1)
#. Compare the network infrastructre asset version to the version in Input 2
	#. Identify and enumerate assets that match the most recent version (M2)
	#. Identify and enumerate assets that don't match the most recent version (M3)
#. Compare Input 3 to current date and capture timeframe in days (M4)

Measures
--------
* M1 = Count of network infrastructure assets
* M2 = Count of network infrastructure assets up to date
* M3 = Count of network infrastructure assets not up to date
* M4 = Timeframe since last review of network infrastrucute

Metrics
-------
If M4 is greater than thirty days, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of network infrastructure assets that are up to date
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
