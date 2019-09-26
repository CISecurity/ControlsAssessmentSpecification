7.7: Use of DNS Filtering Services
===================================
Use Domain Name System (DNS) filtering services to help block access to known malicious domains.

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
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
------
#. EI: The list of endpoints to be audited (sub-control 1.5).
#. The list of accepted DNS filtering services, such as Quad-9.

Operations
----------
#. For each endpoint in Input 1, collect it's DNS configuration setting noting appropriately and inappropriately configured endpoints.

Measures
--------
* M1 = List of audited endpoints
* M2 = Count of M1
* M3 = List of appropriately configured endpoints
* M4 = Count of M3
* M5 = List of inappropriately configured endpoints
* M6 = Count of M5

Metrics
-------

DNS Filtering Coverage
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Determine the ratio of endpoints configured to use accepted DNS filtering services
	    | to the total number of endpoints which utilize DNS.
	* - **Calculation**
	  - :code:`M4 / M2`

Traffic Analysis
^^^^^^^^^^^^^^^^
**NOTE** A second measurement could utilize traffic analysis to determine if any traffic is *not* being sent through the prescribed DNS services.

.. history
.. authors
.. license
