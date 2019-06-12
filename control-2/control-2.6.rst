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

Status
------
Draft

Inputs
------
#. The list of authorized software
#. An organizationally defined allowable timeframe for resolution of discovered unauthorized software
#. The list of endpoints to be checked
#. The updated authorized software list, following the timeframe defined by Input 2

Assumptions
^^^^^^^^^^^
The assumption is made, for Input 4, that the authorized software list may have been updated after a manual review of unauthorized software based on user requests, etc.

Operations
----------
#. For each endpoint in Input 3, scan the installed software present on that endpoint.
#. Compare the installed software list for each endpoint (M1) to the authorized software list (Input 1) to generate the unauthorized software list for that endpoint (M2).
#. Wait the allowable timeframe for resolution (Input 2) and rescan the endpoints specified by Input 3.
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
.. list-table::

	* - **Question**
	  - TBD
	* - **Answer**
	  - TBD
	* - **Calculation**
	  - | If M4 = 0, this indicates no unauthorized software is installed on a given endpoint.
	    | Otherwise, this metric is calculated as :code:`(M4 - M5) / M4`

.. history
.. authors
.. license