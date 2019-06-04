4.8: Log and Alert on Changes to Administrative Group Membership
================================================================
Configure systems to issue a log entry and alert when an account is added to or removed from any group assigned administrative privileges.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Detect
	  - 2, 3

Status
------
Draft

Assumptions
-----------
It is assumed that the number of endpoints under test for an organization (N) is known or accessible via query of an asset inventory.

Measures
--------
* M1 = log enabled for account addition to group with admin privileges (1 = Enabled; 0 = Disabled)
* M2 = log enabled for account removal from group with admin privileges (1 = Enabled; 0 = Disabled)
* M3 = alert enabled for account addition to group with admin privileges (1 = Enabled; 0 = Disabled)
* M4 = alert enabled for account removal from group with admin privileges (1 = Enabled; 0 = Disabled)

Metrics
-------

Log and Alert Enabled
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - What percentage of endpoints in the organization have properly configured logging and alerting for modifications to administrative groups?
	* - **Answer**
	  - The calculation will yield a percentage, from 0 to 100, of those endpoints which have configured logging and alerting correctly.
	* - **Calculation**
	  - :code:`((SUM from 1 to N { M1=1 AND M2=1 AND M3=1 AND M4=1 }) / N) * 100`

.. history
.. authors
.. license