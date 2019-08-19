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

Inputs
------
#. The list of authorized software, per Control 2.
#. The list of enterprise security configuration standards.

Assumptions
^^^^^^^^^^^
* Documentation of secure configuration standards should include any approved deviations/exceptions from industry-standard security baselines such as CIS benchmarks, DISA Security Technical Implementation Guides (STIGs), or U.S. government configuration baselines (USGCB).

Operations
----------
#. Perform a set calculation, computing the Intersection (M1) of Input 1 and Input 2

Measures
--------
* M1 = The intersection of Input 1 and Input 2.  This intersection measures those authorized software with security configuration standards.
* M2 = The "left" side of the set calculation measures the number of authorized software without security configuration standards.
* M3 = The "right" side of the set calculation measures the number of security configuration standards without any authorized software to which they are associated.
* M4 = The number of authorized software.

Metrics
-------

Security Configuration Standards Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | For what percentage of the total OS/Software in an enterprise, are security configuration
	    | standards documented and maintained?
	* - **Calculation**
	  - :code:`(M4 - M2) / M4`

.. history
.. authors
.. license