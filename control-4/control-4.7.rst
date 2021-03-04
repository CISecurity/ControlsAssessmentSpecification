4.7: Manage Default Accounts on Enterprise Assets and Software
=========================================================
Manage default accounts on enterprise assets and software, such as root, administrator, and other pre-configured vendor accounts. Example implementations can include: disabling default accounts or making them unusable.

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
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 5.2: Use Unique Passwords

Inputs
------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV5`: Authorized software inventory
#. :code:`GV20`: Unique password policy

Operations
----------
#. Use :code:`GV5` to identify and enumerate authorized operating software, applications, and third-party software that contain default accounts (M1)
#. Use :code:`GV1` to identify and enumerate assets with software, from Operation 1, installed (M2)
#. For each identified in Operation 2, enumerate default accounts (M3)
#. Check if default accounts can be disabled
	#. Enumerate accounts that are disabled (M4)
	#. Enumerate accounts that are enabled (M5)
#. If account cannot be disabled, ensure to change default passwords according to the :code:`GV20`: enterprise's unique password policy
	#. Enumerate accounts with changed passwords (M6)

Measures
--------
* M1 = Count of software that uses default accounts
* M2 = Count of assets with software installed that uses default accounts
* M3 = Count of default accounts identified 
* M4 = Count of default accounts that have been disabled
* M5 = Count of default accounts that are enabled
* M6 = Count of enabled default accounts with changed passwords

Metrics
-------

Unusable Default Accounts 
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of default accounts that have been rendered unusable
	* - **Calculation**
	  - :code:`(M4 + M6) / M3`

.. history
.. authors
.. license
