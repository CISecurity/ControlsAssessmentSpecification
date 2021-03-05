5.3: Disable Dormant Accounts
=========================================================
Delete or disable any dormant accounts after a period of 45 days of inactivity, where supported

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
* Safeguard 5.1: Establish and Maintain an Inventory of Accounts

Inputs
------
#. :code:`GV22`: Inventory of accounts
#. Enterprise defined policy for dormant threshold

Assumptions
----------
#. The list of accounts for the enterprise includes OS-level, database, internal and external application accounts.
#. A query interface is assumed to enable collection of a “last activity” timestamp, such as last logon, as well as a status indicating if the account is enabled or disabled.

Operations
----------
#. Review Input 2 and note the dormant threshold in terms of days (M2)
#. For each account in :code:`GV22`, query the interface and collect 
	#. The date of last activity for each account 
	#. Whether the account is disabled or not
#. Using the output of Operation 2.1 and Input 2
	#. Identify and enumerate accounts that have exceeded the dormant threshold (M3)
	#. Identify and enumerate accounts that are still within the dormant threshold (M4)
#. Use the output of Operation 2.2 and 3.1 (M3)
	#. Identify and enumerate accounts that are disabled (M5)
	#. Identify and enumerate accounts that are still enabled (M6)

Measures
--------
* M1 = Count of accounts in :code:`GV22`
* M2 = Timeframe of dormant threshold in days
* M3 = Count of dormant accounts
* M4 = Count of active accounts
* M5 = Count of dormant accounts that have been disabled
* M6 = Count of dormant accounts still enabled

Metrics
-------

Dormant Accounts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of dormant accounts still included in
	  - | the inventory.
	* - **Calculation**
	  - :code:`M6 / M1`

Enabled Dormant Accounts 
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of dormant accounts still enabled
	* - **Calculation**
	  - :code:`M6 / M3`

.. history
.. authors
.. license
