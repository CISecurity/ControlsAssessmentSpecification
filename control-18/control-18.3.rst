18.3: Remediate Penetration Test Findings
=========================================================
Remediate penetration test findings based on the enterprise’s policy for remediation scope and prioritization.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 18.2: Perform Periodic External Penetration Tests

Inputs
-----------
#. :code:`GV53: Penetration Testing Program Documentation
#. :code:`GV54`: Most Recent External Penetration Report
#. External penetration report prior to most recent report

Operations
----------
#. Use the findings in Input 3 to identify and enumerate the vulnerabilities outlined (M1)
#. Use the findings in Input 2 :code:`GV54` to identify the vulnerabilites outlined 
#. Compare the output of Operation 1 and Operation 1
	#. Identify and enumerate vulnerabilities found in Input 3 that continue to be in Input 2 (M2)
	#. Identify and enumerate vulnerabilities found in Input 3 that no longer appear in Input 2 (M3)
#. Using the program documentation from Input 1 :code:`GV53` determine whether the ouput of Operation 3.2 is still within scope based on enterprise's policy
	#. Identify and enumerate vulnerabilities within scope (M4)
	#. Identify and enumerate vulnerabilities out of scope (M5)

Measures
--------
* M1 = Count of initial vulnerabilities identified by penetration test
* M2 = Count of successfully remediated vulnerabilities 
* M3 = Count of vulnerabilities that have not been remediated
* M4 = Count of unremediated vulnerabilities still in scope
* M5 = Count of unremediated vulnerabilities out of scope

Metrics
-------

Compliance
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percent of successfully remediated or still within scope vulnerabilities 
	    | identified in the intial penetration test findings
	* - **Calculation**
	  - :code:`(M3 + M4) / M1`

.. history
.. authors
.. license
