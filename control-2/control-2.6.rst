2.6: Address Unapproved Software
================================
Ensure that unauthorized software is either removed or the inventory is updated in a timely manner.

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
* Sub-control 2.1: Maintain Inventory of Authorzied Software
* Sub-control 1.4: Maintain Detailed Asset Inventory

Inputs
------
#. ASL\ :sub:`i`\ : The previous list of authorized software
#. An organizationally defined allowable time frame for resolution of discovered unauthorized software (recommend at least monthly)
#. SCE: The list of endpoints to be checked (derived from hardware inventory; see sub-control 1.4)
#. ASL\ :sub:`i+1`\ : The updated authorized software list, following the time frame defined by Input 2
#. The "scanning threshold"; the time period between scan 1 and scan 2

Assumptions
^^^^^^^^^^^
* For Input 4, that the authorized software list may have been updated after a manual review of unauthorized software based on user requests, etc.
* For Input 5, that the scanning threshold time period is greater than Input 2 (resolution time frame).

Operations
----------
#. For each endpoint in Input 3, scan the installed software present on that endpoint.
#. Compare the installed software list for each endpoint (M1) to the authorized software list (Input 1) to generate the unauthorized software list for that endpoint (M2).
#. Wait the "scanning threshold" time period (Input 5) and re-scan the endpoints specified by Input 3.
#. For each software on the M2 list, determine if that software is still present in the Operation 3 scan.
#. For those that are still present, check Input 4 to determine if the software is now present on the updated authorized software list (Input 4).  Software that remains installed on the machine, but does not appear on the updated authorized software list is added to the unaddressed software list for that endpoint (M3).

Measures
--------
* M1 = The list of software installed on a given endpoint, per Operation 1.
* M2 = The list of unauthorized software installed on a given endpoint, identified by comparing M1 to Input 1.
* M3 = The list of unaddressed software installed on a given endpoint, identified by follow-up scan.
* M4 = The number of items in M2 (# of unauthorized software per endpoint).
* M5 = The number of items in M3 (# of unaddressed software per endpoint).

Metrics
-------

Unauthorized Software (Per Endpoint)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ensure unauthorized software installations are addressed
	* - **Calculation**
	  - :code:`(M4 - M5) / M4`

Unauthorized Software (Organizational)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The organizational metric is calculated by averaging the results of the "per endpoint" metric above.

.. history
.. authors
.. license
