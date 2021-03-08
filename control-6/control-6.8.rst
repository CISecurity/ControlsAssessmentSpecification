6.8: Define and Maintain Role-Based Access Control
=========================================================
Define and maintain role-based access control, through determining and documenting the access rights necessary for each role within the enterprise to successfully carry out its assigned duties. Perform access control reviews of enterprise assets to validate that all privileges are authorized, on a recurring schedule at a minimum annually, or more frequently.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 3

Dependencies
------------
* Safeguard 5.1: Establish and Maintain an Inventory of Accounts

Inputs
------
#. Enterprise documented process for assigning role-based access control
#. :code:`GV22`: Inventory of accounts
#. Date of last validation of role-based access control

Operations
----------
#. Determine whether the enterprise has a process for assigning role-based access control
	#. If the process exists, M1 = 1
	#. If the process does not exist, M1 = 1
#. Use :code:`GV22` and check if each account is assigned a role or group as outlined by the role-based access control process
	#. Identify and enumerate accounts that are assigned a role or group (M3)
	#. Identify and enumerate accounts that are not assigned a role or group (M4)
#. Compare the date in Input 3 to the current date and capture timeframe in months (M5)

Measures
--------
* M1 = Does a role-based access control process exist as defined by the Output of Operation 1
* M2 = Count of :code:`GV22`
* M3 = Count of accounts found in the inventory with assigned role or group
* M4 = Count of accounts found in the inventory not assigned a role or group
* M5 = Timeframe in months of last review of role-bases access control process

Metrics
-------
If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
If M5 is greater than twelve months, this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Coverage
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of account inventory with a properly assigned
	  - | role or group.
	* - **Calculation**
	  - :code:`M3 / M2`


.. history
.. authors
.. license
