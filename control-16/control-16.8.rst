16.8: Disable Any Unassociated Accounts
=========================================================
Disable any account that cannot be associated with a business process or business owner.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Respond
	  - 1, 2, 3

Status
------
Draft

Dependencies
------------
* TBD

Inputs
-----------
#. Inventory of accounts
#. Inventory of business processes and/or business owners

Operations
----------
#. For each account, enumerate any associated business processes or ownership

Measures
--------
* M1 = Number of accounts not associated with any business process or ownership
* M2 = Number of accounts

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - What percentage of accounts are *not* associated with any business process or ownership?
	* - **Calculation**
	  - :code:`M1 / M2`

.. history
.. authors
.. license