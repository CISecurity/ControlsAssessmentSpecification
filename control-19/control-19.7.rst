19.7: Conduct Periodic Incident Scenario Sessions for Personnel
===============================================================
Plan and conduct routine incident response exercises and scenarios for the workforce involved in the incident response to maintain awareness and comfort in responding to real-world threats.  Exercises should test communication channels, decision making, and incident responder’s technical capabilities using tools and data available to them.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - N/A
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 19.1: Document Incident Response Procedures

Inputs
-----------
#. After Action Report from most recent incident response exercise
#. Incident Response Plan

Operations
----------
#. Examine the After Action Report (Input 1) and determine the date of the exercise.  Examine the Incident Response Plan (Input 2) to determine the required time frame for incident response exercises and determine if the most recent exercise was within that time frame (M1).
#. Manually review the After Action Report to determine if it details that the incident response exercise tested the following: communication channels (M2), decision making (M3), incident responder's technical capabilities using the tools and data available to them (M4).

Measures
--------
* M1 = Boolean value indicating if the most recent incident response exercise was within the required time frame; 1 if so, 0 if not
* M2 = Boolean value indicating if the most recent incident response exercise After Action Report contains information about the exercise's testing of communication channels; 1 if so, 0 if not
* M3 = Boolean value indicating if the most recent incident response exercise After Action Report contains information about the exercise's testing of decision making; 1 if so, 0 if not
* M4 = Boolean value indicating if the most recent incident response exercise After Action Report contains information about the exercise's testing of incident responder's technical capabilities using the tools and data available to them; 1 if so, 0 if not

Metrics
-------

Timeliness
^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Timeliness of most recent incident response exercise
	* - **Calculation**
	  - :code:`M1`

Completeness
^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Were incident response After Action Reports complete, containing information regarding
	    | testing of communication channels, decision making, and technical competence?
	* - **Calculation**
	  - :code:`(M2 + M3 + M4) / 3`

.. history
.. authors
.. license