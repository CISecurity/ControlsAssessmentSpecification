2.3: Address Unauthorized Software
=========================================================
Ensure that unauthorized software is either removed from use on enterprise assets or receives a documented exception. Review monthly, or more frequently..

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Respond
	  - 1, 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
------
#. Authorized software list with detailed information
#. Detailed enterprise asset inventory
#. Enterprise defined timeframe for scanning of enterprise assets.
#. Enterprise defined allowable timeframe for resolution of discovered unauthorized software (recommend at least monthly)

Assumptions
--------
#. The scanning schedule timeframe is greater than the enterprise defined allowable timeframe for resolution of discovered unauthorized software. 

Operations
--------
#. Identify the software capable enterprise assets in Input 2 
#. Scan the assets identified in Operation 1 and note software present on each asset (M1)
#. Compare the scan results to the authorized software list in Input 1
	#. Note unauthorized software identified on assets (M2)
#. Conduct subsquent scan of assets identified in Operation 1 as dictated by timeframe in Input 3
	#. Compare to list generated in Operation 3 (M2)
#. For each software still present in Operation 4, check the authorized software list in Input 1
	#. Software that remains installed and is not listed in Input 1 is placed on the unaddressed software list (M3).

Measures
--------
* M1 = The count of software installed on a given asset
* M2 = The count of unauthorized software installed on a given asset
* M3 = The count of unaddressed software installed on a given asset, identified by follow-up scan.
* M4 = Timeframe for resolution of discovered unauthorized software in weeks

Metrics
-------
* If M4 is greater than four weeks, then this safeguard is measured at a 0 and receives a failing score. The other metrics don’t apply.

Unauthorized software Per Asset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ensure unauthorized software installations are addressed
	* - **Calculation**
	  - :code:`(M2-M3) / M3`

Unauthorized software for the enterprise
^^^^^^^^^^^^^^^^^^^^^^^^^^
* The enterprise metric is calculated through averaging the results calculated above per asset.

.. history
.. authors
.. license
