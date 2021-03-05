5.4: Restrict Administrator Privileges to Dedicated Administrator Accounts
=========================================================
Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Conduct general computing activities, such as internet browsing, email, and productivity suite use, from the user’s primary, non-privileged account.

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
* Safeguard 5.1: Establish and Maintain an Inventory of Accounts

Inputs
------
#. :code:`GV22`: Inventory of accounts
#. List of users identified as administrators

Assumptions
----------
#. For the purpose of this control, it is assumed that users identified as administrators that have an active administrative and non-administrative account have properly dedicated accounts for administrative privileges. 

Operations
----------
#. Using :code:`GV22` and Input 2
	#. Identify and enumerate users identified as administrators with active administrator accounts (M1)
	#. Identify and enumerate users identified as administrators without active administrator accounts (M2)
	#. Identify and enumerate users not identified as administrators with active administrator accounts (M3)
#. Using :code:`GV22` and output of Operation 1.1 
	#. Identify and enumerate users identified as administrators that have an active non-administrative user account (M4)
	#. Identify and enumerate users identified as administrators that do not have an active non-administrative user account (M5)

Measures
--------
* M1 = Count of authorized administrative users with active administrator accounts
* M2 = Count of authorized administrative users without active administrator accounts
* M3 = Count of non-administrative users with active administrator accounts
* M4 = Count of authorized administrative users with an active administrative and non-administrative account
* M5 = Count of authorized administrative users without an active administrative and non-administrative account
* M6 = Count of Input 2

Metrics
-------

Administrative User Accounts
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The perecentage of administrative users with both an administrative account
	    | and non-administrative acount.
	* - **Calculation**
	  - :code:`M4/ M6`

Unauthorized Administrative Accounts
^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of unauthorized administrative accounts
	* - **Calculation**
	  - :code:`M3 / (M1 + M3)`


.. history
.. authors
.. license
