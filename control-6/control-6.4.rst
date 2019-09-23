6.4: Ensure Adequate Storage for Logs
=========================================================
Ensure that all systems that store logs have adequate storage space for the logs generated.

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
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
------
#. The list of endpoints (subject to system logging configuration)
#. The organization's logging configuration policy, outlining log rotation policy, maximum log storage size, etc.

Operations
----------
#. For each endpoint, collect the system logging configuration

Measures
--------
* M1(i) = (For each endpoint "i") 1 if an endpoint's logging configuration complies with the organizations logging policy; 0 otherwise.
* M2 = The number of endpoints from Input 1
* M3 = List of compliant endpoints
* M4 = List of non-compliant endpoints


Metrics
-------

Logging Storage Coverage
^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints compliant with the organization's logging policy to the total
	    | number of endpoints.
	* - **Calculation**
	  - :code:`(SUM from i=1..M2 (M1(i))) / M2`

.. history
.. authors
.. license
