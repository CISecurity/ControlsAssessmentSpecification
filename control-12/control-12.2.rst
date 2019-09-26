12.2: Scan for Unauthorized Connections Across Trusted Network Boundaries
=========================================================================
Perform regular scans from outside each trusted network boundary to detect any unauthorized connections which are accessible across the boundary.

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
#. Inventory of Network Boundaries
#. List of most recent scan times for each network boundary
#. Maximum allowable time frame between scans

Operations
----------
#. For each network boundary in Input 1, compare the corresponding time of most recent scan from Input 2 to the maximum allowable time provided in Input 3.
#. Create a list of network boundaries whose most recent scan time was within the allowable time frame (M1).
#. Create a list of network boundaries whose most recent scan time was outside the allowable time frame (M2).

Measures
--------
* M1 = List of network boundaries whose most recent scan time was within the allowable time frame (compliant list)
* M2 = List of network boundaries whose most recent scan time was outside the allowable time frame (non-compliant list)
* M3 = Count of network boundaries that were scanned recently enough (count of M1)
* M4 = Total count of network boundaries (count of Input 1)


Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of network boundary devices scanned within the allowable timeframe to the
	    | total number of network boundary devices
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license
