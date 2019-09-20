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

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory

Inputs
------
#. List of vulnerability scanning accounts
#. List of vulnerability scanning machines

Operations
----------
#. For each vulnerability scanning account, ensure account configuration to log in only to one or more of the vulnerability scanning machines

Measures
--------
* M1 = Total number of vulnerability scanning accounts (from Input 1)
* M2 = List of vulnerability scanning accounts configured to log in only to one or more of the vulnerability scanning machines
* M3 = Count of M2
* M4 = List of vulnerability scanning account configured to log in to any machine other than one of the vulnerability scanning machines
* M5 = Count of M4

Metrics
-------

Misconfigured Account Ratio
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of misconfigured vulnerability scanning accounts to the total number of
	    | vulnerability scanning accounts
	* - **Calculation**
	  - :code:`(M1 - M3) / M1`

.. history
.. authors
.. license
