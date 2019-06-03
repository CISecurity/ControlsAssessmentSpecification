5.1: Establish Secure Configurations
=====================================
Maintain documented security configuration standards for all authorized operating systems and software.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 1, 2, 3

Status
------
Draft

Assumptions
-----------
* Documentation of secure configuration standards should include any approved deviations/exceptions from industry-standard security baselines such as CIS benchmarks, DISA Security Technical Implementation Guides (STIGs), or U.S. government configuration baselines (USGCB).

Measures
--------
* M1 = # of software and OS with security configuration standards
* M2 = total OS and software

Metrics
-------

Coverage (Quality Measure)
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - For what percentage of the total OS/Software in an enterprise are security configuration standards documented and maintained?
	* - **Answer**
	  - Coverage is measured as a percentage of total OS/Software assets for which security configuration standards are documented by an enterprise.
	* - **Calculation**
	  - :code:`(M1/M2) * 100`

.. history
.. authors
.. license