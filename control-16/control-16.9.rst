16.9: Disable Dormant Accounts
=================================
Automatically disable dormant accounts after a set period of inactivity.

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
#. The list of all accounts created in the enterprise
#. An organizationally defined policy indicating a "dormant threshold"; the period of inactivity after which the account is considered dormant (recommended value 1 month)

Assumptions
^^^^^^^^^^^
* The list of accounts for the enterprise includes OS-level, database, internal and external application accounts.
* Based on the account location, a query interface is assumed enabling collection of a "last activity" timestamp, such as last logon, as well as a status indicating if the account is enabled or disabled.

Operations
----------
#. For each account, query the respective interface to collect the account's last activity.
#. For each account, query the respective interface to collect the account's enabled/disabled status.
#. Based on Operations 1 and 2, collect those accounts still marked as enabled but whose last activity is beyond the "dormant threshold" defined in Input 2

Measures
--------
* M1 = List of Accounts
* M2 = Count of M1
* M3 = List of accounts marked as enabled
* M4 = Count of M3
* M5 = List of accounts enabled and not used for a time period outside the dormant threshold
* M6 = Count of M5

Metrics
-------

Dormant Accounts
^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - What percentage of all accounts are currently dormant but still enabled?
	* - **Calculation**
	  - :code:`M6 / M2`

Enabled Dormant Accounts
^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - What percentage of accounts marked enabled are currently dormant and still enabled?
	* - **Calculation**
	  - :code:`M3 / M2`

.. history
.. authors
.. license
