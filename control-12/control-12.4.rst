12.4: Deny Communication Over Unauthorized Ports
=========================================================
Deny communication over unauthorized TCP or UDP ports or application traffic to ensure that only authorized protocols are allowed to cross the network boundary in or out of the network at each of the organization’s network boundaries.

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
* Sub-control 2.4: Track Software Inventory Information

Inputs
-----------
#. List of endpoints to scan (assumed capable of hosting firewall/port-filtering software) as derived from the endpoint inventory (see sub-control 1.4), and potentially as additionally informed the software inventory (see sub-control 2.4)
#. A policy (or set of policies, potentially individually per endpoint) indicating the ports that are allowed to be open

Operations
----------
#. For each endpoint, retrieve its firewall policy
#. For each endpoint/firewall policy pair, examine the endpoint's configuration to enumerate the ports that allow communication and any configuration of a default deny rule, noting appropriately configured and inappropriately configured endpoints along the way.

Measures
--------
* M1 = List of scanned endpoints
* M2 = Count of M1
* M3 = List of endpoints with appropriate port configuration
* M4 = Count of M3
* M5 = List of endpoints with inappropriate port configuration
* M6 = Count of M5
* M7 = List of endpoints with appropriately configured default deny rule
* M8 = Count of M7
* M9 = List of endpoints with inappropriately configured default deny rule
* M10 = Count of M9
* M11 = List of endpoints with both appropriately configured ports and default deny rules
* M12 = Count of M11
* M13 = List of endpoints with at least one inappropriate configuration relative to ports or default deny rule
* M14 = Count of M14

Metrics
-------
.. list-table::

	* - **Metric**
	  - What is the ratio of correctly configured endpoints to the total number of endpoints?
	* - **Calculation**
	  - :code:`M12 / M2`

.. history
.. authors
.. license
