19.5: Maintain Contact Information For Reporting Security Incidents
===================================================================
Assemble and maintain information on third-party contact information to be used to report a security incident, such as Law Enforcement, relevant government departments, vendors, and Information Sharing and Analysis Center (ISAC) partners.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - N/A
	  - 1, 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 19.1: Document Incident Response Procedures

Inputs
-----------
#. Incident response plan
#. List of relevant third-party incident reporting entities

Operations
----------
#. Determine whether incident response plan exists (becomes M1)
#. If it exists, then manual review of incident response plan (determine M2)

Measures
--------
* M1 = A plan exists
* M2 = The plan includes information on third-party contacts for incident reporting (M1 includes Input 2)

Metrics
-------
.. list-table::

	* - **Metric**
	  - Is information on third-party contact information maintained, for use in incident handling?
	* - **Calculation**
	  - :code:`M1 AND M2`

.. history
.. authors
.. license
