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

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. List of endpoints to scan (assumed capable of hosting firewall/port-filtering software)
#. A policy (or set of policies, potentially individually per endpoint) indicating the ports that are allowed to be open

Operations
----------
#. For each endpoint, retrieve the firewall policy
#. For each firewall policy, enumerate both the ports which allow communication, and any configuration of a default deny rule (could that be a default?)

Measures
--------
* M1(i) = (For each endpoint "i") 1 if all of the described open ports are in the allowed list; 0 otherwise
* M2(i) = (For each endpoint "i") 1 if a default deny rule exists and is enforced; 0 otherwise
* M3 = Total number of endpoints
* M4(i) = (For each endpoint "i") The logical :code:`M1(i) AND M2(i)`

Metrics
-------
.. list-table::

	* - **Metric**
	  - What is the ratio of correctly configured endpoints to the total number of endpoints?
	* - **Calculation**
	  - :code:`(SUM from i=1..M3 (M4(i))) / M3`

.. history
.. authors
.. license