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

Status
------
Draft

Dependencies
------------
* TBD

Inputs
-----------
#. The list of all accounts created in the enterprise
#. An organizationally defined policy indicating a "dormant threshold"; the period of inactivity after which the account is considered dormant.

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
* M1 = The total number of accounts
* M2 = The total number of accounts marked as enabled
* M3 = The total number of accounts collected by Operation 3

Metrics
-------

Dormant Accounts
^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - What percentage of all accounts are currently dormant but still enabled?
	* - **Calculation**
	  - :code:`M3 / M1`

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