18.5: Perform Periodic Internal Penetration Tests
==========================================================================
Perform periodic internal penetration tests based on program requirements, no less than annually. The testing may be clear box or opaque box.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - Identify
	  - 3

Dependencies
------------
* Safeguard 18.1: Establish and Maintain a Penetration Testing Program

Inputs
-----------
#. :code:`GV55`: Most Recent Internal Penetration Report

Operations
----------
#. Check Input 1 :code:`GV55` for date of most recent internal penetration test. Compare date to current date and capture timeframe in months (M1) 

Measures
--------
* M1 = Timeframe since last internal penetration test

Metrics
-------
* If M1 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

.. history
.. authors
.. license
