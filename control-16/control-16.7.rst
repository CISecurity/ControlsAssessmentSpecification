16.7: Establish Process for Revoking Access
=========================================================
Establish and follow an automated process for revoking system access by disabling accounts immediately upon termination or change of responsibilities of an employee or contractor.  Disabling these accounts, instead of deleting accounts, allows preservation of audit trails.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Protect
	  - 2, 3

Dependencies
------------
* Sub-control 16.6: Maintain an Inventory of Accounts

Inputs
-----------
#. The inventory of employee accounts
#. A given time period for analysis

Operations
----------
#. For each employee terminated or changed responsibilities within the Input 2 time period, enumerate the employee's accounts (a given employee may have a number of accounts)

Measures
--------
* M1 = List of employee accounts collected by Operation 1
* M2 = Count of M1
* M3 = List of employee accounts disabled within the Input 2 time period
* M4 = Count of M3

Metrics
-------

Enforcement Quality
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of employee accounts that have been terminated/revoked within the acceptable
	    | timeframe.
	* - **Calculation**
	  - :code:`M2 / M4`

.. history
.. authors
.. license
