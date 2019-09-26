6.1: Utilize Three Synchronized Time Sources
=========================================================
Use at least three synchronized time sources from which all servers and network devices retrieve time information on a regular basis so that timestamps in logs are consistent.

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
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
------
#. The list of endpoints
#. The list of network time sources/NTP servers

Operations
----------
#. From the list of endpoints, filter to collect the list of those servers and network devices that should be configured.
#. From the list of servers/network devices, collect each endpoint's network time configuration
#. Collect the list of servers/network devices whose network time configuration does not include a network time source.

Measures
--------
* M1 = Count of endpoints
* M2 = Count of endpoints configured to synchronize with NTP servers
* M3 = Count of endpoints whose network time configuration does not include an approved network time source
* M4(i) = (For each endpoint "i" collected in Operation 1) 1 when the number of configured NTP servers >= 3; 0 otherwise.
* M5 = List of endpoints configured to synchronize with NTP servers
* M6 = List of endpoints whose network time configuration does not include an approved network time source

Metrics
-------

NTP Compliance Coverage
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints using at least 3 synchronized time sources to the total
	    | set of endpoints
	* - **Calculation**
	  - :code:`(SUM from i=1..M2 (M4(i)) / M2)`

.. history
.. authors
.. license
