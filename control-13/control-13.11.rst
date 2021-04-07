13.11: Tune Security Event Alerting Thresholds
=========================================================
Tune security event alerting thresholds monthly, or more frequently.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Detect
	  - 3

Dependencies
------------
* Safeguard 13.1: Centralize Security Event Alerting

Inputs
-----------
#.  Date of last tuning of security event alert thresholds of :code:`GV42` Log correlation or log analytic tool

Operations
----------
#. Compare Input 1 to current date and capture timeframe in days

Measures
--------
* M1 = Timeframe in days since last tuning of security event alert thresholds for log correlation or log analytic tool

Metrics
-------

If M1 is greater than thirty days, then this safeguard is measured at a 0 and receives a failing score.
 
.. history
.. authors
.. license
