16.10: Ensure All Accounts Have An Expiration Date
=========================================================
Ensure that all accounts have an expiration date that is monitored and enforced.

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
* Sub-control 16.1: Inventory of Authentication Systems

Inputs
-----------
#. Account Inventory
#. Authentication System Inventory
#. Approved Configuration(s) for ensuring that account expiration dates are automatically enforced (there may be multiple configurations that vary by type of authentication system, etc.)
#. Optional: Maximum amount of time in the future allowed for an expiration date (example: the organization may require all accounts to have an expiration date no more than 1 year in the future so that all accounts must be re-justified every year).  This time frame could be specific to certain account types (Administrator for example), or specific to certain authentication systems.

Operations
----------
#. For each account in the account inventory (Input 1), check to see if that account has a valid expiration date that is in the future.  If the optional Input 4 was provided, also verify if that expiration date complies with any applicable additional time frame restrictions.  Based on these checks, create a list (M1) of accounts with valid expiration dates, and a list (M2) of accounts with invalid expiration dates (noting why the expiration date is invalid).
#. For each authentication system in Input 2, check to see if it is configured according to the appropriate configuration(s) from Input 3.
#. Create a list (M3) of authentication systems that are configured correctly
#. Create a list (M4) of authentication systems that are not configured correctly (noting the deviations).

Measures
--------
* M1 = List of accounts with valid expiration dates
* M2 = List of accounts with invalid expiration dates
* M3 = List of authentication systems that are configured correctly
* M4 = List of authentication systems that are not configured correctly
* M5 = Count of accounts with valid expiration dates (count of M1)
* M6 = Total count of accounts (count of Input 1)
* M7 = Count of authentication systems that are configured correctly (count of M3)
* M8 = Total count of authentication systems (count of Input 2)

Metrics
-------

.. list-table::

	* - **Metric**
	  - | The ratio of accounts with valid expiration dates to the total number of accounts
	* - **Calculation**
	  - :code:`M5 / M6`


.. list-table::

	* - **Metric**
	  - | The ratio of correctly configured authentication systems to the total number of
	    | authentication systems
	* - **Calculation**
	  - :code:`M7 / M8`

.. history
.. authors
.. license
