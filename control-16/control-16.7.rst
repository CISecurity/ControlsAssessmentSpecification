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

Status
------
Draft

Dependencies
------------
* TBD

Inputs
-----------
#. The inventory of employee accounts
#. A given time period for analysis

Operations
----------
#. For each employee terminated or changed responsibilities within the Input 2 time period, enumerate the employee's accounts (a given employee may have a number of accounts)

Measures
--------
* M1 = The number of employee accounts collected by Operation 1
* M2 = The number of employee accounts disabled within the Input 2 time period

Metrics
-------

Enforcement Quality
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of employee accounts that have been terminated/revoked within the acceptable
	    | timeframe.
	* - **Calculation**
	  - :code:`M1 / M2`

.. history
.. authors
.. license