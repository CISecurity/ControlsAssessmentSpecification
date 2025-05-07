6.3: Require MFA for Externally-Exposed Applications
=========================================================
Require all externally-exposed enterprise or third-party applications to enforce MFA, where supported. Enforcing MFA through a directory service or SSO provider is a satisfactory implementation of this Safeguard.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process
* Safeguard 5.1: Establish and Maintain an Inventory of Accounts

Inputs
------
#. :code:`GV5`: Authorized Software Inventory
#. :code:`GV22`: Inventory of Accounts
#. :code:`GV3`: Configuration Standard

Operations
---------- 
#. Use Input 1 to identify and enumerate externally exposed and third party applications
#. Using the output of Operation 1 and :code:`GV22` identify and enumerate all user accounts associated with the applications (M1) 
#. For each account identified in Operation 2 use :code:`GV3` to
	#. Identify and enumerate accounts properly configured to require MFA (M2)
	#. Identify and enumerate accounts not properly configured to require MFA (M3)

Measures
--------
* M1 = Count of accounts associated with externally exposed and third party applications
* M2 = Count of accounts properly configured to require MFA
* M3 = Count of accounts not properly configured to require MFA

Metrics
-------

Coverage
^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of externally exposed and third party application accounts
	    | properly configured for MFA
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
