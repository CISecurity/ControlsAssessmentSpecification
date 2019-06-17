4.3: Ensure the Use of Dedicated Administrative Accounts
=========================================================
Ensure that all users with administrative account access use a dedicated or secondary account for elevated activities. This account should only be used for administrative activities and not Internet browsing, email, or similar activities.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Protect
	  - 1, 2, 3

Status
------
Draft

Inputs
------
#. The list of users defined as Administrators
#. The list of user accounts for the users defined in Input 1
#. The list of users NOT defined as Administrators
#. The list of user accounts for the users defined in Input 3
#. The list of all user accounts.
#. The list of all Administrative user accounts
#. The list of non-Administrative user accounts

Operations
----------
#. For each user defined in Input 1, collect the Administrative user account for that user from Input 6 and the non-Administrative user account from Input 7
#. For each user defined in Input 3, collect any Administrative user account for that user from Input 6 and the non-Administrative user account from Input 7

Measures
--------
* M1 = The number of users defined as Administrators
* M2 = For each user, this measure describes the number of user accounts identified by Operation 1
* M3 = For each user, this measure describes the number of user accounts identified by Operation 2


Metrics
-------

Administrative User Accounts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | This metric is intended to determine whether those users identified as Administrative-level
	    | have at least one Administrative-level and one non-Administrative level user account.
	* - **Answer**
	  - | Operation 1 above should result in a list of users defined as Administrators mapped to
	    | Administrative user accounts tied to that user.  All Administrative-level users must be
	    | assigned at least one secondary Administrative user account.
	* - **Calculation**
	  - | The mapping performed by Operation 1 must show that, for each Administrative-level
	    | user, at least 1 Administrative-level user account and at least 1
	    | non-Administrative-level user account are available.  Otherwise, this metric is a :code:`FAIL`

Unauthorized User Accounts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | This metric is intended to illustrate any non-Administrative-level users that
	    | have been assigned an Administrative-level user account.
	* - **Answer**
	  - | Operation 2 above should result in a list of any non-Administrative-level users
	    | that have been assigned an Administrative-level user account.
	* - **Calculation**
	  - If any users exist in the mapping M3, then :code:`FAIL`; otherwise :code:`PASS`

.. history
.. authors
.. license