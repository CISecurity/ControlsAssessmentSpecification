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
* M1 = Count of endpoints covered by vulnerability scanning tools (count of operation 2)
* M2 = Total number of endpoints
* M3 = Count of vulnerability scanning tools configured to scan at least weekly
* M4 = Count of vulnerability scanning results having occurred in at least the past week
* M5 = Count of SCAP-validated vulnerability scanning tools
* M6 = Count of vulnerability scanning tools

Metrics
-------

Vulnerability Scanning Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints covered by at least one vulnerability scanning tool to the total 
	    | number of endpoints
	* - **Calculation**
	  - :code:`M1 / M2`

Vulnerability Scanner Configuration Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of correctly configured vulnerability scanners to the total number of 
	    | vulnerability scanners
	* - **Calculation**
	  - :code:`M3 / M6`

Vulnerability Scan Timeliness
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of scanners having actually scanned in at least the past week to the total 
	    | number of vulnerability scanners
	* - **Calculation**
	  - :code:`M4 / M6`

SCAP-Validated Vulnerability Scanner Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of SCAP-validated scanners to the total number of vulnerability scanners
	* - **Calculation**
	  - :code:`M5 / M6`

.. history
.. authors
.. license