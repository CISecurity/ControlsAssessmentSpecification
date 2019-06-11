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
In Development

Inputs
------
#. A list of known SCAP-validated vulnerability scanners is available
#. Inventory of vulnerability scanners is up-to-date
#. Enterprise-specific scanning frequency (not to be less frequent than weekly) is known

Operations
----------
#. 

Measures
--------
* M1 = 1st scan time
* M2 = 2nd scan time
* M3 = max allowed delay in consecutive scans (given)
* M4 = # of devices in the network
* M5 = # of scanned devices(from the vulnerability scanning report)

Metrics
-------

Freshness
^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | This metric is intended to determine if vulnerability scans are being performed
	    | within a reasonable time frame.
	* - **Answer**
	  - | This calculation results in a TRUE/FALSE answer, indicating whether or not consecutive
	    | vulnerability scans (M1 and M2) are performed within the maximum allowed delay (M3).
	* - **Calculation**
	  - :code:`TRUE if (M2 - M1) <= M3; FALSE otherwise`

Coverage Quality
^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | This metric is intended to determine the ratio of the number of devices on the network
	    | to those being regularly scanned for vulnerabilities.
	* - **Answer**
	  - | The calculation of this metric results in a percentage, between 0 and 100, indicating
	    | the vulnerability scanning coverage for an enterprise.
	* - **Calculation**
	  - :code:`(M5/M4) * 100`

.. history
.. authors
.. license
