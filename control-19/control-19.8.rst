19.8: Create Incident Scoring and Prioritization Schema
=========================================================
Create incident scoring and prioritization schema based on known or potential impact to your organization. Utilize score to define frequency of status updates and escalation procedures.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - N/A
	  - 3

Status
------
Draft

Dependencies
------------
* Subcontrol 19.1: Document Incident Response Procedures

Inputs
-----------
#. Enterprise incident management policy

Operations
----------
#. Examine the enterprise incident management policy for the following properties:
	#. Incident scoring and prioritization schema based on known or potential impact
	#. Procedure relying on this schema is used to determine status update frequency during incident handling
	#. Procedure relying on this schema is used to determine escalation paths during incident handling

Measures
--------
* M1 = (Boolean) 1 if an incident scoring and prioritization schema is present in the policy; 0 otherwise
* M2 = (Boolean) 1 if status update procedure relies on aforementioned schema; 0 otherwise
* M3 = (Boolean) 1 if escalation procedure relies on aforementioned schema; 0 otherwise

Metrics
-------

Scoring/Prioritization
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Does the incident management policy include a scoring/prioritization schema, and are
	    | status update frequency and escalation paths reliant upon that schema?
	* - **Calculation**
	  - :code:`M1 AND M2 AND M3`

.. history
.. authors
.. license