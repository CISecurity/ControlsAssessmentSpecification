20.2: Conduct Regular External and Internal Penetration Tests
=============================================================
Conduct regular external and internal penetration tests to identify vulnerabilities and attack vectors that can be used to exploit enterprise systems successfully.

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
#. Penetration Testing Report for most recent external penetration test
#. Penetration Testing Report for most recent internal penetration test
#. Penetration Testing Program document

Operations
----------
#. Examine the Penetration Testing Reports (Inputs 1 and 2) to determine the dates that the most recent penetration tests of each type (external and internal) occurred. Examine the Penetration Testing Program document (Input 3) to determine how frequently the organization is required to conduct external and internal penetration tests, and use those required time frames to determine:
	#. if the most recent external penetration test was within the required time frame (M1)
	#. if the most recent internal penetration test was within the required time frame (M2)
#. Manually review the Penetration Testing Reports to confirm that they contain any discovered vulnerabilities and attack vectors that can be used to successfully exploit the organization's systems (M3); or, if none were successful, verify that the documentation describes those that were attempted but were unsuccessful.

Measures
--------
* M1 = Boolean value indicating if the most recent external penetration test was within the required time frame; 1 if so, 0 otherwise
* M2 = Boolean value indicating if the most recent internal penetration test was within the required time frame; 1 if so, 0 otherwise
* M3 = Boolean value indicating if the Penetration Testing Reports contain discovered vulnerabilities and attack vectors that were successful against the organization's systems; 1 if so, 0 otherwise

Metrics
-------

Penetration Testing Reports
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Are both internal and external penetration tests conducted regularly?
	* - **Calculation**
	  - :code:`M1 AND M2`

Vulnerability Discovery
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Do penetration testing reports document discovered vulnerabilities?
	* - **Calculation**
	  - :code:`M3`

.. history
.. authors
.. license
