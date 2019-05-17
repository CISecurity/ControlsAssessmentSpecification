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

**Pre-requisites**

1. vulnerability scanning account name
2. authorized vulnerability scanning machines

**Measure**

1. vulnerability accounts usage data (traffic/log analysis) for each account
2. scanning machine configuration (static IP address assignment)

**Metric**

1. Boolean: enterprise has designated accounts
2. Ratio of designated account alternate use to designated accounts used appropriately
3. Ratio of scanning machines with static IP assignments to scanning machines in total

Measures
--------


Metrics
-------
.. list-table::

	* - **Question**
	  - 
	* - **Answer**
	  - 
	* - **Calculation**
	  - :code:`?`

.. history
.. authors
.. license