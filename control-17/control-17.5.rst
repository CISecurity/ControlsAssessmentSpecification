17.5: Assign Key Roles and Responsibilities
=========================================================
Assign key roles and responsibilities for incident response, including staff from legal, IT, information security, facilities, public relations, human resources, incident responders, and analysts, as applicable. Review annually, or when significant enterprise changes occur that could impact this Safeguard.

.. list-table:: 
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - Respond
	  - 2, 3

Dependencies
------------
* Safeguard 17.4: Establish and Maintain an Incident Response Process

Inputs
-----------
#. :code:`GV52`: Incident response process
#. Date of last update or review of the documentation

Operations
----------
#. Determine whether the enterprise documents key roles and responsibilities by reviewing Input 1 :code:`GV52`
	#. If documentation exists, M1 = 1
	#. If documentation does not exist, M1 = 0
#. Using the documentation in Input 1 :code:`GV52`, identify and enumerate the roles and responsibilities (M2)
#. For each role and responsibility identified in Operation 2, determine whether an individual is mapped to that role and responsibility
	#. Identify and enumerate those that are mapped (M3)
	#. Identify and enumerate those that are not mapped (M4)
#. Compare Input 2 to current date and capture timeframe in months (M5)

Measures
--------
* M1 = Output of Operation 1
* M2 = Count of roles and responsibilities outlined in process
* M3 = Count of roles and responsibilities that are mapped to an individual
* M4 = Count of roles and responsibilities that are not mapped to an individual
* M5 = Timeframe since last update or review of documentation in months

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
* If M5 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Completeness
^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of roles and responsibilities that are
	    | mapped to an individual 
	* - **Calculation**
	  - :code:`M3 / M2`


.. history
.. authors
.. license
