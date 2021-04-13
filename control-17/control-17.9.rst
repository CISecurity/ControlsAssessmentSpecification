17.9: Establish and Maintain Security Incident Thresholds
====================================================================
Establish and maintain security incident thresholds, including, at a minimum, differentiating between an incident and an event. Examples can include: abnormal activity, security vulnerability, security weakness, data breach, privacy incident, etc. Review annually, or when significant enterprise changes occur that could impact this Safeguard.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - N/A
	  - 1, 2, 3

Dependencies
------------
* Safeguard 17.4: Establish and Maintain an Incident Response Process

Inputs
-----------
#. :code:`GV52`: Incident response process
#. Date of last update or review of the documentation

Operations
----------
#. Determine whether the enterprise documents security incident threshold by reviewing Input 1 :code:`GV52`
	#. If documentation for a security incident threshold exists, M1 = 1
	#. If documentation for a security incident threshold does not exist, M1 = 0
#. Determine whether the documentation, at a minimum, outlines the following components: differentiates between incident and event, prioritization schema based on known or potential impact, procedure relying on this schema is used to determine status update frequency during incident handling, and procedure relying on this schema is used to determine escalation paths during incident handling
	#. For each mechanism included, assign a value of 1. Sum the values. (M2)
#. Compare Input 2 to current date and capture timeframe in months (M3)

Measures
--------
* M1 = Output of Operation 1
* M2 = Count of components included in documentation
* M3 = Timeframe since last update or review of documentation in months

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
* If M3 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Completeness
^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of components included in documentation for 
	    | security incident thresholds 
	* - **Calculation**
	  - :code:`M2 / 4`

.. history
.. authors
.. license
