19.3: Designate Management Personnel to Support Incident Handling
=================================================================
Designate management personnel, as well as backups, who will support the incident handling process by acting in key decision-making roles.

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
* Sub-control 19.1: Document Incident Response Procedures

Inputs
-----------
#. Incident response plan

Operations
----------
#. Determine whether incident response plan exists (becomes M1)
#. If it exists, then manual review of incident response plan (determine M2 and M3)

Measures
--------
* M1 = A plan exists
* M2 = The plan identifies management personnel filling incident response handling decision-making roles
* M3 = The plan identifies backup personnel to the management personnel identified by M2

Metrics
-------
.. list-table::

	* - **Metric**
	  - Are personnel, including backups, designated to support the incident handling process?
	* - **Calculation**
	  - :code:`M1 AND M2 AND M3`

.. history
.. authors
.. license
