20.4: Include Tests for Presence of Unprotected System Information and Artifacts
================================================================================
Include tests for the presence of unprotected system information and artifacts that would be useful to attackers, including network diagrams, configuration files, older penetration test reports, emails or documents containing passwords or other information critical to system operation.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	* - N/A
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 20.1: Establish a Penetration Testing Program

Inputs
-----------
#. Penetration Testing Program document

Operations
----------
#. Manually review the Penetration Testing Program document (Input 1) to determine if it requires tests to discover the following unprotected system information:
	#. Network diagrams (M1)
	#. Configuration files (M2)
	#. Penetration test reports (M3)
	#. Emails or documents containing passwords or other information critical to system operation (M4)

Measures
--------
* M1 = Boolean value indicating if the Penetration Testing Program document requires tests to discover unprotected network diagrams; 1 if so, 0 otherwise
* M2 = Boolean value indicating if the Penetration Testing Program document requires tests to discover unprotected configuration files; 1 if so, 0 otherwise
* M3 = Boolean value indicating if the Penetration Testing Program document requires tests to discover unprotected penetration test reports; 1 if so, 0 otherwise
* M4 = Boolean value indicating if the Penetration Testing Program document requires tests to discover unprotected emails or documents containing passwords or other critical system information; 1 if so, 0 otherwise

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Does the Penetration Testing Program Includes Tests for the Presence of Unprotected
	    | System Information and Artifacts?
	* - **Calculation**
	  - :code:`(M1 + M2 + M3 + M4) / 4`

.. history
.. authors
.. license
