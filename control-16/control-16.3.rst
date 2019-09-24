16.3: Require Multi-Factor Authentication
=========================================================
Require multi-factor authentication for all user accounts, on all systems, whether managed on-site or by a third-party provider.

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
* Sub-control 16.6: Maintain an Inventory of Accounts

Inputs
-----------
#. Account inventory organized by authentication system (from Sub-Control 16.6)
#. Approved configuration(s) to require multi-factor authentication (MFA).  This will likely be a configuration for each type of authentication system in use

Operations
----------
#. For each account in the account inventory (Input 1), check to see if that account is configured to require MFA in accordance with the appropriate approved configuration(s) from Input 2.  
#. Create a list of accounts that are properly configured to require MFA (M1)
#. Create a list of accounts that are not properly configured to require MFA (M2) noting the deviations from the approved configuration.

Measures
--------
* M1 = List of accounts that are properly configured to require MFA (compliant list)
* M2 = List of accounts that are not properly configured to require MFA (non-compliant list)
* M3 = Count of accounts properly configured to require MFA (count of M1)
* M4 = Total number of accounts (count of Input 1)

Metrics
-------

.. list-table::

	* - **Metric**
	  - | The ratio of accounts that are properly configured to require MFA to the total number
	    | of accounts.
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license
