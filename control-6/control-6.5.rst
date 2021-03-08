6.5: Require MFA for Administrative Access
=========================================================
Require MFA for all administrative access accounts, where supported, on all enterprise assets, whether managed on-site or through a third-party provider.

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
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process
* Safeguard 5.1: Establish and Maintain an Inventory of Accounts 

Inputs
------
#. :code:`GV22`: Inventory of accounts 
#. :code:`GV3`: Configuration Standard

Operations
----------
#. Using :code:`GV22` identify and enumerate all administrative accounts (M1)
#. For each administrative account identified in Operation 1 check configurations in :code:`GV3`
	#. Identify and enumerate administrative accounts properly configured to require MFA (M2)
	#. Identify and enumerate administrative accounts not properly configure to require MFA (M3)

Measures
--------
* M1 = Count of administrative accounts 
* M2 = Count of administrative accounts properly configured to require MFA
* M3 = Count of administrative accounts not properly configured to require MFA

Metrics
-------

Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of administrative accounts properly configured to
	  - | require MFA.
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
