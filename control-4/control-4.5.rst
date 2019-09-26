4.5: Use Multi-Factor Authentication for All Administrative Access
==================================================================
Use multi-factor authentication and encrypted channels for all administrative account access.

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
* Sub-control 2.4: Track Software Inventory Information
* Sub-control 4.1: Maintain Inventory of Administrative Accounts

Inputs
------
#. List of Administrative accounts in the organization along with corresponding authentication system for each
#. Approved Multi-Factor Authentication Configuration(s) - there may be multiple configurations based on the types of accounts and authentication systems involved
#. Approved Encrypted Channel Configuration(s) - there may be multiple configurations based on the types of accounts and authentication systems involved

Operations
----------
#. For each account in Input 1, check its configuration against the appropriate Multi-Factor Authentication configuration in Input 2. Create a list of compliant accounts (M1) and non-compliant accounts (M2)
#. For each account in Input 1, check its configuration against the appropriate Encrypted Channel configuration in Input 3. Create a list of compliant accounts (M3) and non-compliant accounts (M4)

Measures
--------
* M1 = List of Administrative Accounts that are configured properly for Multi-Factor Authentication (Multi-Factor compliant list)
* M2 = List of Administrative Accounts that are not configured properly for Multi-Factor Authentication (Multi-Factor non-compliant list)
* M3 = List of Administrative Accounts that are configured properly to be accessed through encrypted channels (Encrypted Channel compliant list)
* M4 = List of Administrative Accounts that are not configured properly to be accessed through encrypted channels (Encrypted Channel non-compliant list)
* M5 = Count of Multi-Factor compliant Administrative Accounts (count of M1)
* M6 = Count of Encrypted Channel compliant Administrative Accounts (count of M3)
* M7 = Total count of Administrative Accounts (count of Input 1)

Metrics
-------

Multi-Factor Compliance
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Calculate the ratio of administrative accounts configured to use multi-factor
	    | authentication to the total number of administrative accounts
	* - **Calculation**
	  - :code:`M5 / M7`

Encrypted Channel Compliance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Calculate the ratio of administrative accounts configured to use encrypted channels to
	    | the total number of administrative accounts
	* - **Calculation**
	  - :code:`M6 / M7`

.. history
.. authors
.. license
