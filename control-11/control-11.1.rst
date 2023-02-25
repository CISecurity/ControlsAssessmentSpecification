11.1: Establish and Maintain a Data Recovery Process 
===================================================================
Establish and maintain a data recovery process. In the process, address the scope of data recovery activities, recovery prioritization, and the security of backup data. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard. 

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Recover
	  - 1, 2, 3

Dependencies
------------
* None

Inputs
------
#. Data recovery process for the enterprise
#. Date of last update to the data recovery process 

Operations
----------
#. Check if enterprise has a data recovery process Input 1
	#. If so, M1 = 1
	#. If not, M1 = 0
#. Examine the enterprise's data recovery process and determine if it addresses, at a minimum, the scope of data recovery activities, recovery prioritization, and the security of backup data
	#. For each element included within the process, assing the element a value of 1. M2 = sum of all the values.
#. Compare the date of last update to the data recovery process to the curren date and capture timeframe in months (M3)

Measures
--------
* M1 = Output of Operation 1
* M2 = Sum of elements included in the data recoery process
* M3 = Timeframe in months of last update to the data recovery process


Metrics
-------
If M1 is 0, the safeguard receives a failing score. The other metrics don't apply.
If M3 is greater than twelve, this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Completeness
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of elements included in the data recovery process
	* - **Calculation**
	  - :code:`M2 / M3`

.. history
.. authors
.. license
