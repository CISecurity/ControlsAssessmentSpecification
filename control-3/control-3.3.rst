3.3: Configure Data Access Control Lists
===========================================
Configure data access control lists based on a user’s need to know. Apply data access control lists, also known as access permissions, to local and remote file systems, databases, and applications. 

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Safeguard 3.2: Establish and Maintain a Data Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process
* Safeguard 5.1: Establish and Maintain an Inventory of Accounts

Inputs
------
#. :code:`GV12`: Sensitive Data Inventory 
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV3`: Configuration Standards
#. :code:`GV13`: Portion of data management process addressing data owners
#. :code:`GV14`: Portion of data management process addressing data handling
#. :code:`GV22`: Inventory of Accounts 

Assumptions
----------



Operations
----------
#. Use the data managemet process, specifically :code:`GV13` and :code:`GV14`, as guidelines to map user account to sensitive data in :code:`GV12`.
	#. Identify and enumerate sensitive data correctly mapped to user accounts (M1)
	#. Idenitfy and enumerate sensitive data not correctly mapped to user accounts (M2)
#. For each enterprise asset storing sensitive data, as outlined by :code:`GV12,
	#. Identify and enumerate all assets storing sensitive data (3)
	#. Use :code:`GV3` to check and enumerate assets that are properly configured to only allow users as identified in Operation 1 (M3)
	#. Use :code:`GV3` to check and enumerate assets that are improperly configured to only allow users as identified in Operation 1 (M4)

Measures
----------
* M1 = Count of sensitive data correctly mapped to user accounts per the data management process
* M2 = Count of sensitive data correctly mapped to user accounts per the data management process
* M3 = Count of assets storing sensitive data
* M4 = Count of properly configured assets to support data access control
* M5 = Count of improperly configured assets to support data access control
* M6 = Count of :code:`GV17`
* M7 = :code:'GV13`
* M8 = :code:`GV14`

Metrics
-------
If either M7 or M8 is 0, this safeguard receives a failing score. The other metrics don't apply.

Completeness of User Access Control
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of user accounts properly mapped to sensitive data 
	* - **Calculation**
	  - :code:`M1 / M6`

Properly Configured Assets
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of assets properly configured to control acess of
	    | sensitive data
	* - **Calculation**
	  - :code:`M4 / M3`

.. history
.. authors
.. license
