16.2: Configure Centralized Point of Authentication
=========================================================
Configure access for all accounts through as few centralized points of authentication as possible, including network, security, and cloud systems.

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
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. The list of endpoints

Operations
----------
#. Enumerate centralized authentication points in inventory
#. For each identified centralized authentication point to determine necessity (i.e. can a given authentication system be consolidated with another?)
#. Enumerate the list of unnecessary centralized authentication points

Measures
--------
* M1 = List of centralized authentication points in inventory
* M2 = List of unnecessary centralized authentication points
* M3 = Count of centralized authentication points in the inventory (The count of M1)
* M4 = Count of unnecessary centralized authentication points (The count of M2)
* M5 = M3 - M4 (the target number of centralized authentication points)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of desired centralized authentication points to actual authentication
	    | points, where the goal is for M5 / M3 = 1.
	* - **Calculation**
	  - :code:`M5 / M3`

.. history
.. authors
.. license
