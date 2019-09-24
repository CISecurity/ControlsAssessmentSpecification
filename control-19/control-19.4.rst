19.4: Devise Organization-wide Standards For Reporting Incidents
================================================================
Devise organization-wide standards for the time required for system administrators and other workforce members to report anomalous events to the incident handling team, the mechanisms for such reporting, and the kind of information that should be included in the incident notification.

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
* Sub-control 19.1: Document Incident Response Procedures

Inputs
-----------
#. Incident Reporting Standards document

Operations
----------
#. Determine whether the Incident Reporting Standards document exists. If the document exists, set M1 equal to 1. If it does not exist, set M1 equal to 0 and skip the remaining operations.
#. Manually review the Incident Reporting Standards document to determine if it addresses:
	#. The time required for system administrators and other workforce members to report anomalous events to the incident handling team (M2)
	#. The mechanisms for such reporting (M3)
	#. The kind of information that should be included in the incident notification (M4)
#. For each, set the measure to 1 if the document adequately addresses the topic, or 0 if the document fails to adequately address the topic.

Measures
--------
* M1 = Boolean value indicating if the Incident Reporting Standards document exists; 1 if it exists, 0 if not
* M2 = Boolean value indicating if the Incident Reporting Standards document adequately addresses the time required for system administrators and other workforce members to report anomalous events to the incident handling team; 1 if it does, 0 if it does not
* M3 = Boolean value indicating if the Incident Reporting Standards document adequately addresses the mechanisms for reporting anomalous events to the incident handling team; 1 if it does, 0 if it does not
* M4 = Boolean value indicating if the Incident Reporting Standards document adequately addresses the kind of information that should be included in an incident notification to the incident handling team; 1 if it does, 0 if it does not

Metrics
-------

Incident Reporting Standards Completeness
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Does the Incident Reporting Standards document exist and adequately addresses the
	    | specified topics?
	* - **Calculation**
	  - :code:`M1 AND M2 AND M3 AND M4`

.. history
.. authors
.. license
