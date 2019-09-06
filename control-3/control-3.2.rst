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

Status
------
Draft

Dependencies
------------
* Subcontrol 2.1: Maintain Inventory of Authorized Software

Inputs
------
#. List of deployed vulnerability scanning tools
#. List of authenticated vulnerability scanners
#. Time threshold for last use of vulnerability scanner

Operations
----------
#. For each deployed vulnerability scanner, check whether it is in the list of authenticated vulnerability scanners
#. For each deployed vulnerability scanner, verify that it has been used within time threshold
#. For each authorized vulnerability scanner
	#. Enumerate endpoints covered
	#. Check configuration for authenticated scanning on each endpoint
#. Aggregate number of endpoints covered (becomes M5)
#. Aggregate correct configuration (becomes M6)

Measures
--------
* M1 = Number of deployed vulnerability scanning tools
* M2 = Count of unauthenticated vulnerability scanning tools
* M3 = Count of authenticated vulnerability scanning tools
* M4 = Count of vulnerability scanning tools recently used
* M5 = Count of endpoints covered by authenticated vulnerability scanners
* M6 = Count of endpoints scanned in an authenticated manner

Metrics
-------

Authenticated Vulnerability Scanning Tool Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of authenticated vulnerability scanning tools (100% is desired)
	* - **Calculation**
	  - :code:`(M1 - M3) / M1`

Recently Used Vulnerability Scanning Tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of vulnerability scanning tools recently used
	* - **Calculation**
	  - :code:`(M1 - M4) / M1`

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Authenticated scanning coverage
	* - **Calculation**
	  - :code:`M6 / M5`

.. history
.. authors
.. license