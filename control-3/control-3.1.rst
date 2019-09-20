3.1: Run Automated Vulnerability Scanning Tools
===============================================
Utilize an up-to-date Security Content Automation Protocol (SCAP) compliant vulnerability scanning tool to automatically scan all systems on the network on a weekly or more frequent basis to identify all potential vulnerabilities on the organization’s systems.

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
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 2.3: Utilize Software Inventory Tools

Inputs
------
#. List of endpoints
#. List of vulnerability scanning tools
#. List of SCAP-validated vulnerability scanning tools
#. Most recent scan results for each vulnerability scanning tool

Operations
----------
#. For each vulnerability scanning tool, enumerate the set of covered endpoints
#. Union the set of covered endpoints
#. For each vulnerability scanning tool, inspect tool configuration for at least weekly scans
#. For each vulnerability scanning tool, inspect tool results/logs for at least weekly scans

Measures
--------
* M1 = List of endpoints covered by vulnerability scanning tools
* M2 = Count of M1
* M3 = Count of endpoints (from Input 1)
* M4 = List of vulnerability scanning tools configured to scan at least weekly
* M5 = Count of M4
* M6 = List of vulnerability scanning tools not configured to scan at least weekly
* M7 = Count of M6
* M8 = List of vulnerability scanning results having occurred in at least the past week
* M9 = Count of M8
* M10 = List of vulnerability scanning results having not occurred in at least the past week
* M11 = Count of M10
* M12 = Count of SCAP-validated vulnerability scanning tools (from Input 2)
* M13 = Count of vulnerability scanning tools (from Input 3)

Metrics
-------

Vulnerability Scanning Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints covered by at least one vulnerability scanning tool to the total
	    | number of endpoints
	* - **Calculation**
	  - :code:`M2 / M3`

Vulnerability Scanner Configuration Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of correctly configured vulnerability scanners to the total number of
	    | vulnerability scanners
	* - **Calculation**
	  - :code:`M5 / M13`

Vulnerability Scan Timeliness
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of scanners having actually scanned in at least the past week to the total
	    | number of vulnerability scanners
	* - **Calculation**
	  - :code:`M9 / M13`

SCAP-Validated Vulnerability Scanner Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of SCAP-validated scanners to the total number of vulnerability scanners
	* - **Calculation**
	  - :code:`M12 / M13`

.. history
.. authors
.. license
