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

Dependencies
------------
* Subcontrol 2.5: Integrate Software and Hardware Asset Inventories
* Sub-control 5.1: Establish Secure Configurations

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
* M1 = Count of internal DNS servers
* M2 = Count of internal DNS servers matching the organization's configuration policy
* M3 = List of compliant DNS servers
* M4 = List of non-compliant DNS servers

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
