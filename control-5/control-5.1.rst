5.1: Establish and Maintain an Inventory of Accounts
=====================================
Establish and maintain an inventory of all accounts managed in the enterprise. The inventory must include both user and administrator accounts. The inventory, at a minimum, should contain the person’s name, username, start/stop dates, and department. Validate that all active accounts are authorized, on a recurring schedule at a minimum quarterly, or more frequently.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Identify
	  - 1, 2, 3

Dependencies
------------
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
------
#. :code:`GV5`: Authorized software inventory
#. :code:`GV22`: Inventory of accounts
#. Date of last review of the inventory of accounts

Operations
----------
#. Check if the enterprise maintains an inventory of user and administrative accounts (Input 2)
	#. If the inventory exists M1 = 1
	#. If the inventory does not exist M1 = 0
#. Using the inventory of accounts :code:`GV22`, determine if the inventory captures the following elements: person’s name, username, start/stop dates, and department
	#. Each element is assigned a value of 1 if it exists and 0 if it does not. Total the number of elements that exist. (M3)
#. Using :code:`GV22` check each account for elements: person’s name, username, start/stop dates, and department
	#. Identify and enumerate accounts with all elements (M4)
	#. Identify and enumerate accounts missing or with incomplete elements (M5)
#. Use :code:`GV5` to identify authentication systems or other software that manages accounts :code:`GV23`.
#. Using the output of Operation 4, enumerate all current user and administrative accounts throughout the enterprise (M6)
#. Compare the output of Operation 5 with :code:`GV22` 
	#. Identify and enumerate accounts that are supposed to be active/enabled (M7)
	#. Identify and enumerate accounts that are supposed to be disabled/removed (M8)
#. Compare the current date to the date provided in Input 3 and enumerate the timeframe in months (M9)
 

Measures
--------
* M1 = Does the account inventory exist (Output of Operation 1)
* M2 = Count of accounts in :code:`GV22`
* M3 = Count of elements provided in inventory
* M4 = Count of accounts in inventory with complete information
* M5 = Count of accounts in inventory with missing or incomplete information
* M6 = Count of current accounts identified through Operation 5
* M7 = Count of authorized accounts
* M8 = Count of unauthorized accounts
* M9 = Timeframe of last update in months

Metrics
-------
If M1 is 0, this safeguard receives a failing score and other metrics don't apply.
If M9 is greater than three, this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Completeness of Inventory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of minimum elements included in the inventory.
	* - **Calculation**
	  - :code:`M3 / 4`

	* - **Metric**
	  - | The percentage of accounts with complete information.
	* - **Calculation**
	  - :code:`M4 / 2`

Accuracy of Inventory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of accurately listed accounts in the inventory.
	* - **Calculation**
	  - :code:`M8 / M6`

.. history
.. authors
.. license
