18.2: Perform Periodic External Penetration Tests
==========================================================================================
Perform periodic external penetration tests based on program requirements, no less than annually. External penetration testing must include enterprise and environmental reconnaissance to detect exploitable information. Penetration testing requires specialized skills and experience and must be conducted through a qualified party. The testing may be clear box or opaque box.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Identify
	  - 2, 3

Dependencies
------------
* Safeguard 18.1: Establish and Maintain a Penetration Testing Program

Inputs
-----------
#. :code:`GV54`: Most Recent External Penetration Report

Operations
----------
#. Check Input 1 :code:`GV54` for date of most recent external penetration test. Compare date to current date and capture timeframe in months (M1) 

Measures
--------
* M1 = Timeframe since last external penetration test

Metrics
-------
* If M1 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

.. history
.. authors
.. license
