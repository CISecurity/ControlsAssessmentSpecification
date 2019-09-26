11.1: Maintain Standard Security Configurations for Network Devices
===================================================================
Maintain documented security configuration standards for all authorized network devices.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Identify
	  - 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
------
#. The list of authorized network devices, per Control 1.
#. The list of enterprise security configuration standards.

Assumption
^^^^^^^^^^
* Documentation of secure configuration standards should include any approved deviations/exceptions from industry-standard security baselines such as CIS benchmarks, DISA Security Technical Implementation Guides (STIGs), or U.S. government configuration baselines (USGCB).

Operations
----------
#. Perform a set calculation, computing the Intersection (M1) of Input 1 and Input 2

Measures
--------
* M1 = The intersection of Input 1 and Input 2. This intersection measures those authorized network devices with security configuration standards.
* M2 = The "left" side of the set calculation measures the number of authorized network devices without security configuration standards.
* M3 = The "right" side of the set calculation measures the number of security configuration standards without any authorized network devices to which they are associated.
* M4 = Count of authorized network devices.

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of network devices to which standard, documented security configuration
	    | standards exist to the total number of network devices
	* - **Calculation**
	  - :code:`(M4 - M2) / M4`

.. history
.. authors
.. license
