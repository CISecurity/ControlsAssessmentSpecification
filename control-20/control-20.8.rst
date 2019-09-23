20.8: Control and Monitor Accounts Associated With Penetration Testing
======================================================================
Any user or system accounts used to perform penetration testing should be controlled and monitored to make sure they are only being used for legitimate purposes, and are removed or restored to normal function after testing is over.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - N/A
	* - N/A
	  - 2, 3

Status
------
Draft

Dependencies
------------
* None

Inputs
-----------
#. The historical inventory of user and system accounts (prior to input 3)
#. The current inventory of user and system accounts (after input 4)
#. The timestamp for the beginning of the most recent penetration testing period
#. The timestamp for the ending of the most recent penetration testing period

Operations
----------
#. Enumerate historical user and system accounts (Input 1) and note any privileges specifically assigned for penetration testing (M1)
#. Enumerate the current user and system accounts and privileges for those accounts determined in Operation 1

Measures
--------
* M1 = The list of historical user and system accounts authorized for use in penetration testing
* M2 = The number of historical user and system accounts authorized for use in penetration testing (count of M1)
* M3 = The list of current user and system accounts that were authorized for use in penetration testing
* M4 = The number of current user and system accounts that were authorized for use in penetration testing (count of M3)
* M5 = The list of current user and system accounts with penetration testing privileges still assigned
* M6 = The number of current user and system accounts with penetration testing privileges still assigned (count of M5)

Metrics
-------

Privileged Accounts Remain
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | If :code:`M5 > 0`, then privileged user accounts remain following the penetration 
	    | testing period.
	* - **Calculation**
	  - :code:`M5 > 0`

.. history
.. authors
.. license