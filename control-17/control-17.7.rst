17.7: Train Workforce on Sensitive Data Handling
=========================================================
Train workforce members on how to identify and properly store, transfer, archive, and destroy sensitive information.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - N/A
	  - 1, 2, 3

Status
------
Draft

Dependencies
------------
* None

Inputs
-----------
#. List of workforce members
#. List of most recent security awareness training completion dates for each workforce member
#. Required frequency of training (at least annually)

Operations
----------
#. For each workforce member in Input 1, check Input 2 to see if that workforce member's most recent security awareness training completion date was within the time frame specified by Input 3 (if the workforce member is not listed in Input 2, assume the workforce member is not compliant). Generate a list of compliant workforce members (M1) and a list of non-compliant workforce members (M2).

Measures
--------
* M1 = List of workforce members who have completed the security awareness training within the specified time frame (compliant list)
* M2 = List of workforce members who have not completed the security awareness training within the specified time frame (non-compliant list)
* M3 = Number of workforce members in the compliant list (M1)
* M4 = Number of workforce members in the non-compliant list (M2)
* M5 = Total number of workforce members in Input 1

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Question**
	  - | What percentage of workforce members have completed the security awareness training
	    | module within the specified time frame?
	* - **Answer**
	  -
	* - **Calculation**
	  - :code:`M3 / M5`

.. history
.. authors
.. license
