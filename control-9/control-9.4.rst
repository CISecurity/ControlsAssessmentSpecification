9.4: Apply Host-Based Firewalls or Port-Filtering
=========================================================
Apply host-based firewalls or port-filtering tools on end systems, with a default-deny rule that drops all traffic except those services and ports that are explicitly allowed.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
------
#. EI: Derive from the endpoint inventory those endpoints able to scan (assumed capable of hosting firewall/port-filtering software)
#. A policy (or set of policies, potentially individually per endpoint) indicating the ports that are allowed to be open

Operations
----------
#. For each endpoint, retrieve the firewall policy
#. For each firewall policy, enumerate both the ports which allow communication, and any configuration of a default deny rule (could that be a default?), noting along the way appropriately configured policies and inappropriately configured policies

Measures
--------
* M1 = List of endpoints
* M2 = Count of M1
* M3 = List of endpoints with appropriately configured firewall ports policy
* M4 = Count of M3
* M5 = List of endpoints with inappropriately configured firewall ports policy
* M6 = Count of M5
* M7 = List of endpoints with appropriately configured default deny rule
* M8 = Count of M7
* M9 = List of endpoints with inappropriately configured default deny rule
* M10 = Count of M9
* M11 = List of endpoints with both appropriately configured firewall policy
* M12 = Count of M11
* M13 = List of endpoints with at least one inappropriate firewall configuration
* M14 = Count of M13

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of correctly configured endpoints to the total number of endpoint?
	* - **Calculation**
	  - :code:`M14 / M2`

.. history
.. authors
.. license
