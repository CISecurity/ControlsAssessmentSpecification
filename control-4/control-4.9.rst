4.9: Log and Alert on Unsuccessful Administrative Account Login
===============================================================
Configure systems to issue a log entry and alert on unsuccessful logins to an administrative account.

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


Measures
--------
* M1 = Log enabled for unsuccessful login attempt with admin account
* M2 = Alert enabled for unsuccessful login attempt with admin account

Metrics
-------

Log and Alert Enabled
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - This measurement is meant to determine if a log entry and alert are generated when an unsuccessful administrative login attempt is made.
	* - **Answer**
	  - The calculation results in TRUE if both log entry and alert are generated.
	* - **Calculation**
	  - :code:`M1 AND M2`

.. history
.. authors
.. license