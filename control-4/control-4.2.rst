4.2: Change Default Passwords
=============================
Before deploying any new asset, change all default passwords to have values consistent with administrative level accounts.

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

Assumptions
-----------
There are really two parts to this measure: 

1. default passwords are not in use, and 
2. the non-default password is compliant with enterprise standards (i.e. a password policy).

This metric is concerned with number 1, above.

Consideration needs to be made for software applications that require credentials - applying this measure and password policies at the application level is also important (in addition to the OS level).

Measures
--------
* M1 = # of total account 
* M2 = # of account with default password


Metrics
-------

Coverage (Quality Measure)
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - What percentage of total accounts remain configured with default passwords?
	* - **Answer**
	  - This metric yields a positive percentage value indicating what percentage of accounts remain configured with a default password.
	* - **Calculation**
	  - :code:`100 - (((M1-M2)/M1) * 100)`

.. history
.. authors
.. license