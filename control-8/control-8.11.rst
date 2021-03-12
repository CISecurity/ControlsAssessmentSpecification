8.11: Conduct Audit Log Reviews
=========================================================
Conduct reviews of audit logs to detect anomalies or abnormal events that could indicate a potential threat. Conduct reviews on a weekly, or more frequent, basis..

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Detect
	  - 2, 3

Dependencies
------------
* None

Inputs
------
#. Timestamp for two consecutive log reviews

Assumptions
----------
#. Log reviews are conducted at regular and consistent intervals

Operations
----------
#. Compare each timestamp to determine timeframe between log reviews in days (M1)

Measures
--------
* M1 = Timeframe between log reviews

Metrics
-------
If M1 is greater than seven, this safeguard is measured at a 0 and receives a failing score. 

.. history
.. authors
.. license
