3.3: Protect Dedicated Assessment Accounts
===========================================
Use a dedicated account for authenticated vulnerability scans, which should not be used for any other administrative activities and should be tied to specific machines at specific IP addresses.

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

Inputs
------
#. List of vulnerability scanning accounts
#. List of vulnerability scanning machines

Operations
----------
#. For each vulnerability scanning account, ensure account configuration to log in only to one or more of the vulnerability scanning machines

Measures
--------
* M1 = Total number of vulnerability scanning accounts
* M2 = Number of vulnerability scanning accounts configured to log in only to one or more of the vulnerability scanning machines


Metrics
-------

Misconfigured Account Ratio
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of misconfigured vulnerability scanning accounts to the total number of 
	    | vulnerability scanning accounts
	* - **Calculation**
	  - :code:`(M1 - M2) / M1`

.. history
.. authors
.. license