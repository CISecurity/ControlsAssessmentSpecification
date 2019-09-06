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

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information

Inputs
------
#. List of endpoints to scan (assumed capable of hosting firewall/port-filtering software)
#. A policy (or set of policies, potentially individually per endpoint) indicating the ports that are allowed to be open

Operations
----------
#. For each endpoint, retrieve the firewall policy
#. For each firewall policy, enumerate both the ports which allow communication, and any configuration of a default deny rule (could that be a default?)

Measures
--------
* M1(i) = (For each endpoint "i") 1 if all of the described open ports are in the allowed list in the endpoint's firewall policy
* M2(i) = (For each endpoint "i") 1 if a default deny rule exists in the endpoint's firewall policy, and is enforced.
* M3 = Total number of endpoints
* M4(i) = (For each endpoint "i") Logical AND of M1 and M2 for that endpoint

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of correctly configured endpoints to the total number of endpoint?
	* - **Calculation**
	  - :code:`(SUM from i=1..M3 (M4(i))) / M3`

.. history
.. authors
.. license