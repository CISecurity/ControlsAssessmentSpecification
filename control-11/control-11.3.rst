11.3: Use Automated Tools to Verify Standard Device Configurations and Detect Changes
=====================================================================================
Compare all network device configurations against approved security configurations defined for each network device in use, and alert when any deviations are discovered.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Detect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 2.1: Maintain Inventory of Authorized Software

Inputs
------
#. The organization's configuration monitoring system
#. The list of network devices
#. The inventory and mappings of secure configuration policy(ies) to the list of network devices

Operations
----------
#. For each network devices, obtain the configuration assessment results using Input 1

Measures
--------
* M1(i) = (For each network device "i") Count of non-compliant recommendations resulting from Operation 1
* M2(i) = (For each network device "i") Count of recommendations assessed

Metrics
-------

Non-Compliance Ratio
^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of network devices not in compliance with secure configuration policies to the
	    | total number of network devices.
	* - **Calculation**
	  - :code:`(SUM from i=1..M2 (M1(i))) / M2`

.. history
.. authors
.. license
