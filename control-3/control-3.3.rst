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

Assumptions
-----------
This sub-control requires that a specific user account be designated to be used only for authenticated vulnerability scans. No other activities should be performed with this account. Seems that we would need some input from the operator/systems administrator/enterprise.

1. List of vulnerability scanning account names
2. List of authorized vulnerability scanning machines

Measures
--------

1. Vulnerability accounts usage data (traffic/log analysis) for each account
2. Scanning machine configuration (static IP address assignment)

Metrics
-------

Designated Accounts
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - Does the enterprise use dedicated accounts for vulnerability scans?
	* - **Answer**
	  - Boolean.
	* - **Calculation**
	  - :code:`?`

Account Misuse Ratio
^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - What is the proportion of designated accounts used improperly?
	* - **Answer**
	  - Ratio of misused vulnerability scanning accounts to the total number of vulnerability scanning accounts.
	* - **Calculation**
	  - :code:`?`

Machine Misconfiguration Ratio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - What is the proportion of vulnerability scanning machines without a static IP assignment?
	* - **Answer**
	  - Ratio of misconfigured vulnerability scanning machines to the total number of vulnerability scanning machines.
	* - **Calculation**
	  - :code:`?`

.. history
.. authors
.. license
