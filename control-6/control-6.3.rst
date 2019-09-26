6.3: Enable Detailed Logging
=========================================================
Enable system logging to include detailed information such as an event source, date, user, timestamp, source addresses, destination addresses, and other useful elements.

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
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
------
#. The list of endpoints (subject to system logging configuration)
#. The organization's logging configuration policy, outlining the detailed information to be written to system logs

Operations
----------
#. For each endpoint, collect the system logging configuration

Measures
--------
* M1(i) = (For each endpoint "i") 1 if the endpoint's logging configuration complies with the organizations logging policy; 0 otherwise.
* M2 = Count of endpoints from Input 1
* M3 = List of compliant endpoints
* M4 = List of non-compliant endpoints

Metrics
-------

Logging Coverage
^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints configured to enable detailed system logging to the total number
	    | of endpoints.
	* - **Calculation**
	  - :code:`(SUM from i=1..M2 (M1(i))) / M2`

.. history
.. authors
.. license
