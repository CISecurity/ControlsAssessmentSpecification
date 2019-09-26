19.2: Assign Job Titles and Duties for Incident Response
=========================================================
Assign job titles and duties for handling computer and network incidents to specific individuals, and ensure tracking and documentation throughout the incident through resolution.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - N/A
	  - 2, 3

Dependencies
------------
* Sub-control 19.1: Document Incident Response Procedures

Inputs
-----------
#. Incident Response Plan including Incident Response Job Titles/Duties
#. Mapping of individuals to Incident Response Job Titles/Duties

Operations
----------
#. Manually review the Incident Response Plan to verify that it exists and that it contains Incident Response job titles and duties. If the document exists and contains job titles and duties, set M1 equal to 1. If it does not exist, set M1 equal to 0 and skip the remaining operations.
#. Manually review the Incident Response Plan to verify that it ensures tracking and documentation throughout the incident through resolution. If this is adequately addressed in the document, set M2 equal to 1. If it is not, set M2 equal to 0.
#. For each job title specified in the Incident Response Plan, check Input 2 to ensure that at least one individual is mapped to that job. Create a list of jobs that have been assigned at least one individual (M3) and a list of jobs that have not been assigned at least one individual (M4).

Measures
--------
* M1 = Boolean value indicating if the Incident Response Plan exists and contains Incident Response job titles and duties; 1 if so, 0 if not
* M2 = Boolean value indicating if the Incident Response Plan adequately addresses tracking and documentation throughout the incident; 1 if so, 0 if not
* M3 = List of Incident Response jobs with individuals assigned
* M4 = List of Incident Response jobs without individuals assigned
* M5 = Count of Incident Response jobs with individuals assigned (count of M3)
* M6 = Total number of Incident Response jobs defined

Metrics
-------

Incident Response Plan Completeness
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Does the incident response plan exist, contain job titles/duties, and adequately
	    | address tracking and documentation throughout the incident?
	* - **Calculation**
	  - :code:`M1 AND M2`

Assignment Coverage
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of incident response jobs/duties with assignees to the total number of
	    | incident response jobs/duties
	* - **Calculation**
	  - :code:`M4 / M6`

.. history
.. authors
.. license
