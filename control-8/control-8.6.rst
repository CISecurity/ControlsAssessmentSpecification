8.6: Centralize Anti-Malware Logging
=========================================================
Send all malware detection events to enterprise anti-malware administration tools and event log servers for analysis and alerting.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Detect
	  - 2, 3

Dependencies
------------
* Sub-control 2.1: Maintain Inventory of Authorized Software
* Sub-control 5.1: Establish Secure Configurations

Inputs
------
#. List of software instances (anti-malware software, anti-malware administration tools, and event log servers) that need to be configured to properly send, receive, and log these malware detection events.
#. Approved configuration(s) for anti-malware software, anti-malware administration tools, and event log servers to ensure that malware detection events are properly sent, received, and logged.
#. The total number of malware detection events (M5)
#. The number of alerts being correlated in a central service (M6)

Operations
----------
#. For each software instance in Input 1, check to see if it is configured according to the appropriate approved configuration(s) in Input 2.
#. Create a list of the software instances that are properly configured (M1)
#. Create a list of the software instances that are not properly configured (M2) noting where the deviations occur.

Measures
--------
* M1 = List of software instances that are properly configured for the sending/receiving of malware detection events (compliant list)
* M2 = List of software instances that are not properly configured for the sending/receiving of malware detection events (non-compliant list)
* M3 = Count of properly configured software instances (count of M1)
* M4 = Total count of software instances that need to be configured to properly send/receive malware detection events (count of Input 1)
* M5 = Count of malware detection events
* M6 = Count of alerts being correlated in a central service

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of properly configured software instances for sending/receiving malware detection
	    | events.
	* - **Calculation**
	  - :code:`M3 / M4`

Quality
^^^^^^^
.. list-table::

	* - **Metric**
	  - | Quality of Log correlation/aggregation for Anti-Malware
	* - **Calculation**
	  - :code:`M6 / M5`

.. history
.. authors
.. license
