12.3: Deny Communications With Known Malicious IP Addresses
=========================================================
Deny communications with known malicious or unused Internet IP addresses and limit access only to trusted and necessary IP address ranges at each of the organization’s network boundaries.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information
* Subcontrol 12.1: Maintain an Inventory of Network Boundaries

Inputs
-----------
#. The list of endpoints
#. The list of trusted and necessary IP address ranges
#. The list of known malicious IP addresses
#. The list of unused Internet IP addresses

Operations
----------
#. Enumerate all network devices identified as guarding a network boundary
#. For each network boundary device, examine its configuration to ensure rules as follows, noting appropriately and inappropriately configured devices:
	#. Allow communications only with IP addresses in the list of trusted and necessary IP address ranges
	#. Explicitly deny communications with IP addresses in the list of known malicious IP addresses
	#. Explicitly deny communications with IP addresses in the list of unused IP addresses

Measures
--------
* M1 = List of all network boundary devices
* M2 = List of appropriately configured network boundary devices
* M3 = List of inappropriately configured network boundary devices
* M4 = The number of network boundary devices (the count of M1)
* M5 = The number of appropriately configured network boundary devices (the count of M2)
* M6 = The number of inappropriately configured network boundary devices (the count of M3)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured network boundary devices to the total number of 
	    | network boundary devices
	* - **Calculation**
	  - :code:`M5 / M4`

.. history
.. authors
.. license