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

Dependencies
------------
* None

Inputs
-----------
#. Inventory of accounts
#. Inventory of business processes and/or business owners

Operations
----------
#. For each account, enumerate any associated business processes or ownership

Measures
--------
* M1 = List of accounts
* M2 = Count of M1
* M3 = List of accounts not associated with any business process or ownership
* M4 = Count of M3
* M5 = List of accounts associated with at least one business process or ownership
* M6 = Count of M5

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - What percentage of accounts are associated with at least one business process or ownership?
	* - **Calculation**
	  - :code:`M6 / M2`

.. history
.. authors
.. license
