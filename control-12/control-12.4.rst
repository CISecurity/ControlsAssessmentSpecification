12.4: Establish and Maintain Architecture Diagram(s)
=========================================================
Establish and maintain architecture diagram(s) and/or other network system documentation. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard.

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
* None

Inputs
-----------
#. :code:`GV4`: Enterprise network architecture documentation
#. Date of last review or update to documentation 

Operations
----------
#. Determine if Input 1 :code:`GV4` exists within the enterprise
	#. If the network architecture documentation exists, M1 = 1
	#. If the network architecture documentation does not exist, M1 = 0
#. Compare Input 2 to the current date. Capture the timeframe in months.  

Measures
--------
* M1 = Output of Operation 1. 
* M2 = Timeframe in months of last review or update to documentation


Metrics
-------
If M1 is not provided or available, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.
If M2 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

.. history
.. authors
.. license
