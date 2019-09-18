16.6: Maintain an Inventory of Accounts
=========================================================
Maintain an inventory of all accounts organized by authentication system.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Identify
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 16.1: Inventory of Authentication Systems

Inputs
-----------
#. Authentication System Inventory
#. The organization's current account inventory (the "to be checked" inventory)

Operations
----------
#. For each authentication system in Input 1, enumerate the accounts under that authentication system.  This ground truth list of accounts organized by authentication system becomes M1.
#. Compare the accounts listed in M1 to the accounts listed in the current account inventory (Input 2).  
#. Create a list of the correct accounts in Input 2 (which will be M2)
#. Create a list of the incorrect accounts in Input 2 (which will be M3).

Measures
--------
* M1 = Ground truth account inventory
* M2 = Correct accounts from the current (to be checked) inventory
* M3 = Incorrect accounts from the current (to be checked) inventory
* M4 = Count of accounts in the ground truth account inventory (count of M1)
* M5 = Count of correct accounts in the current (to be checked) account inventory (count of M2)

Metrics
-------

.. list-table::

	* - **Metric**
	  - | Calculate the accuracy of current (to be checked) account inventory
	* - **Calculation**
	  - :code:`M5 / M4`

.. history
.. authors
.. license