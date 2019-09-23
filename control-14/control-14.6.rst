14.6: Protect Information Through Access Control Lists
=========================================================
Protect all information stored on systems with file system, network share, claims, application, or database specific access control lists.  These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 1, 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 5.1: Establish Secure Configurations

Inputs
-----------
#. Endpoint Inventory
#. Access control configuration policy

Operations
----------
#. For each endpoint in Input 1, collect the "ground truth" access policy for that endpoint and compare it to the access control configuration policy in Input 2. Generate a list of endpoints which comply with the specified access control configuration policy (M1) and a list of endpoints that do not comply with the specified policy (M2)

Measures
--------
* M1 = List of endpoints that comply with access control configuration policy (compliant list)
* M2 = List of endpoints that do not comply with access control configuration policy (non-compliant list)
* M3 = Count of endpoints in M1 (number of compliant endpoints)
* M4 = Count of endpoints in M2 (number of non-compliant endpoints)
* M5 = Count of endpoints in Input 1 (total number of endpoints to check)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What is the percentage of endpoints which are compliant with the organization's
	    | access control policy?
	* - **Calculation**
	  - :code:`M3 / M5`

.. history
.. authors
.. license
