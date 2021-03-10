7.7: Remediate Detected Vulnerabilities
===================================
Remediate detected vulnerabilities in software through processes and tooling on a monthly, or more frequent, basis, based on the remediation process.

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
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory

Inputs
------
#. :code:`GV1`: Enterprise asset inventory
#. Current vulnerability scan
#. Previous vulnerability scan 
#. Date of current vulnerability scan
#. Date of previous vulnerability scan

Assumptions 
----------
#. Asset-Vulnerability combinations not found in most recent scan is indicative of remediation of that vulnerability on that asset.

Operations
----------
#. For each asset in :code:`GV1`, compare Inputs 2 and 3
	#. Identify and enumerate assets listed with the same vulnerability on both scans (M2)
	#. Identify and enumerate assets previously found in Input 3 that are no longer listed in Input 2 with the same vulnerability (M3)
#. Compare Inputs 4 and 5 and capture timeframe between scans in days (M4)


Measures
--------
* M1 = Count of vulnerabilities identified in Input 3
* M2 = Count of unremediated vulnerabilities
* M3 = Count of remediated vulnerabilities
* M4 = Timeframe in between scans

Metrics
-------
If M4 is greater than thirty, this safeguard receives a failing score. The other metrics don't apply.

Remediation
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of remediated vulnerabilities 
	* - **Calculation**
	  - :code:`M3 / M1`

.. history
.. authors
.. license
