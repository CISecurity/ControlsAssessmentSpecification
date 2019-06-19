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

Status
------
Draft

Inputs
------
#. The list of endpoints to be audited.
#. The list of accepted DNS filtering services, such as Quad-9.

Operations
----------
#. For each endpoint in Input 1, collect it's DNS configuration setting.

Measures
--------
* M1 = 1 if an endpoint audited in Operation 1 is configured correctly; 0 otherwise.
* M2 = Total number of endpoints audited.

Metrics
-------

DNS Filtering Coverage
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | Determine the ratio of endpoints configured to use accepted DNS filtering services
	    | to the total number of endpoints which utilize DNS.
	* - **Answer**
	  - | The calculation will yield a percentage, from 0 to 100, indicating the ratio of
	    | correctly configured endpoints to the total number of endpoints.
	* - **Calculation**
	  - :code:`(SUM(M1)) / M2`

Traffic Analysis
^^^^^^^^^^^^^^^^
**NOTE** A second measurement could utilize traffic analysis to determine if any traffic is *not* being sent through the prescribed DNS services.

.. history
.. authors
.. license