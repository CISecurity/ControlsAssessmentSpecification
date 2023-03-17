16.2: Establish and Maintain a Process to Accept and Address Software Vulnerabilities
=========================================================
Establish and maintain a process to accept and address reports of software vulnerabilities, including providing a means for external entities to report. The process is to include such items as: a vulnerability handling policy that identifies reporting process, responsible party for handling vulnerability reports, and a process for intake, assignment, remediation, and remediation testing. As part of the process, use a vulnerability tracking system that includes severity ratings, and metrics for measuring timing for identification, analysis, and remediation of vulnerabilities. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard.

Third-party application developers need to consider this an externally-facing policy that helps to set expectations for outside stakeholders.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 2, 3

Dependencies
------------
* None

Inputs
-----------
#. :code:`GV48`: Process to Accept and Address Software Vulnerabilities 
#. Date of last update or review of process

Operations
----------
#. Determine whether Input 1 exists within the enterprise
	#. If Input 1 exists, M1 = 1
	#. If Input 1 does not exist, M1 = 0
#. Review Input 1 :code:`GV48` and dermine whether it includes, at a minimum, the following components: reporting process, responsible party for handling vulnerability reports, a process for intake, assignment, remediation, remediation testing, and a vulnerability tracking system
	#. For each component included in the process, assign a value of 1.  Sum all values. (M2)
#. Compare Input 2 to current date and capture timeframe in months (M3)


Measures
--------
* M1 = Output of Operation 1
* M2 = Count of components included in the process
* M3 = Timeframe in months since last review or update

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
* If M3 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Completeness
^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percent of components included in the secure application 
	  - | development process
	* - **Calculation**
	  - :code:`M2 / 7`

.. history
.. authors
.. license
