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

Dependencies
------------
* Sub-control 2.1: Maintain Inventory of Authorized Software

Inputs
------
#. ASL: The list of authorized software (sub-control 2.1).
#. SCS: The list of enterprise security configuration standards.

Assumptions
^^^^^^^^^^^
* Documentation of secure configuration standards should include any approved deviations/exceptions from industry-standard security baselines such as CIS benchmarks, DISA Security Technical Implementation Guides (STIGs), or U.S. government configuration baselines (USGCB).

Operations
----------
#. Perform a set calculation, computing the Intersection (M1) of Input 1 and Input 2

Measures
--------
* M1 = The list of authorized software with associated enterprise security configuration standards
* M2 = Count of M1
* M3 = The list of authorized software without enterprise security configuration standards (the "left" side of the set calculation)
* M4 = Count of M3
* M5 = The list of enterprise security configuration standards without associated authorized software (the "right" side of the set calculation)
* M6 = Count of M5
* M7 = The list of authorized software
* M8 = Count of M7

Metrics
-------

Security Configuration Standards Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | For what percentage of the total OS/Software in an enterprise, are security configuration
	    | standards documented and maintained?
	* - **Calculation**
	  - :code:`(M8 - M4) / M8`

.. history
.. authors
.. license
