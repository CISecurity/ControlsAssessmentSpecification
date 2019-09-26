3.6: Compare Back-to-Back Vulnerability Scans
=============================================
Regularly compare the results from consecutive vulnerability scans to verify that vulnerabilities have been remediated in a timely manner.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Respond
	  - 2, 3

Dependencies
------------
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
------
#. The list of endpoints
#. Previous vulnerability scan results for all covered endpoints
#. Current vulnerability scan results for all covered endpoints

Operations
----------
#. For each covered endpoint:
	#. Intersection of previous scan results with current scan results (Assumption: this should result in the complete set of results from the previous scan and set aside the new vulnerability checks introduced in the current scan)
	#. Identify set of detected vulnerabilities from previous scan, based on intersection
	#. Identify set of detected vulnerabilities from current scan, based on intersection
#. Count endpoints in the set of covered endpoints eligible for back-to-back comparisons

Assumption
^^^^^^^^^^
* The first operation carries the assumption that the intersection of previous scan results with current scan results yields the complete set of results from the previous scan and sets aside any new vulnerability checks introduced in the current scan. Doing so should also accommodate the dynamic enterprise that is adding and removing assets as a matter of course.

Measures
--------
* M1 = Set of previously detected vulnerabilities
* M2 = Set of currently detected vulnerabilities
* M3 = Count of previously detected vulnerabilities
* M4 = Count of currently detected vulnerabilities
* M5 = List of covered endpoints with back-to-back comparisons
* M6 = Count of M5
* M7 = List of endpoints in inventory eligible for back-to-back comparisons
* M8 = Count of M7

Metrics
-------

Unmitigated Vulnerabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Count of vulnerabilities previously discovered that are still discovered.
	* - **Calculation**
	  - :code:`M3 - M4`

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Coverage of back-to-back comparisons against eligible endpoints
	* - **Calculation**
	  - :code:`M6 / M8`

.. history
.. authors
.. license
