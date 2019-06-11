5.5: Implement Automated Configuration Monitoring Systems
=========================================================

Utilize a Security Content Automation Protocol (SCAP) compliant configuration monitoring system to verify all security configuration elements, catalog approved exceptions, and alert when unauthorized changes occur.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Detect
	  - 2, 3

Status
------
In Development

Inputs
------
#. 

Assumptions
^^^^^^^^^^^
* The SCAP-compliant configuration monitoring system has access to machine-readable versions of security assessment content, either from a single source or multiple sources, for each approved configuration documented by control 5.1.
* A list of approved exceptions or deviations from the documented security configuration standard is available for the system(s) under test.
* A "compliance percentage" metric, detailing the percentage of compliance of the system under test to the approved configuration standards, is assumed to be provided by the SCAP-compliant configuration monitoring system.

Operations
----------
#. 

Measures
--------
* M1 = # of total exception in the configuration
* M2 = # of reported exception from configuration

Metrics
-------

Exception Report Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | What percentage of deviations from the approved configuration standard have been
	    | documented?
	* - **Answer**
	  - | The calculation will yield a percentage, from 0 to 100, indicating whether or not
	    | all reported exceptions have been documented.
	* - **Calculation**
	  - :code:`((M1-M2) / M1) * 100`

.. history
.. authors
.. license