8.7: Enable DNS Query Logging
=========================================================
Enable Domain Name System (DNS) query logging to detect hostname lookups for known malicious domains.

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
* Subcontrol 2.5: Integrate Software and Hardware Asset Inventories

Inputs
------
#. The list of internal DNS servers
#. The organization's DNS configuration policy

Assumption
^^^^^^^^^^
* The organization maintains its own internal DNS server

Operations
----------
#. For each internal DNS server (Input 1), compare the server's DNS configuration with the organization's DNS configuration policy

Measures
--------
* M1 = The number of internal DNS servers
* M2 = The number of internal DNS servers matching the organization's configuration policy

Metrics
-------

DNS Configuration Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of internal DNS servers matching the approved configuration to the 
	    | total number of internal DNS servers.
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license