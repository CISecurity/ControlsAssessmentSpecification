3.2: Perform Authenticated Vulnerability Scanning
=================================================
Perform authenticated vulnerability scanning with agents running locally on each system or with remote scanners that are configured with elevated rights on the system being tested.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Detect
	  - 2, 3

Dependencies
------------
* Sub-control 2.1: Maintain Inventory of Authorized Software

Inputs
------
#. List of deployed vulnerability scanning tools
#. List of authenticated vulnerability scanners
#. Time threshold for last use of vulnerability scanner

Operations
----------
#. For each deployed vulnerability scanner, check whether it is in the list of authenticated vulnerability scanners, noting those that are and those that are not
#. For each deployed vulnerability scanner, verify that it has been used within time threshold
#. For each authorized vulnerability scanner
	#. Enumerate endpoints covered
	#. Check configuration for authenticated scanning on each endpoint
#. Aggregate number of endpoints covered (becomes M5)
#. Aggregate correct configuration (becomes M6)

Measures
--------
* M1 = Count of deployed vulnerability scanning tools (from Input 1)
* M2 = List of unauthenticated vulnerability scanning tools
* M3 = Count of M2
* M4 = List of authenticated vulnerability scanning tools
* M5 = Count of M4
* M6 = List of vulnerability scanning tools recently used
* M7 = Count of M6
* M8 = List of vulnerability scanning tools not recently used
* M9 = Count of M8
* M10 = List of endpoints covered by at least one authenticated vulnerability scanner
* M11 = Count of M10
* M12 = List of endpoints scanned in an authenticated manner
* M13 = Count of M12
* M14 = List of endpoints not scanned in an authenticated manner
* M15 = Count of M14

Metrics
-------

Authenticated Vulnerability Scanning Tool Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of authenticated vulnerability scanning tools (100% is desired)
	* - **Calculation**
	  - :code:`(M1 - M5) / M1`

Recently Used Vulnerability Scanning Tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of vulnerability scanning tools recently used
	* - **Calculation**
	  - :code:`(M1 - M7) / M1`

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Authenticated scanning coverage
	* - **Calculation**
	  - :code:`M13 / M11`

.. history
.. authors
.. license
