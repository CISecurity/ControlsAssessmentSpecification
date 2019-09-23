20.6: Use Vulnerability Scanning and Penetration Testing Tools in Concert
==========================================================================
Use vulnerability scanning and penetration testing tools in concert. The results of vulnerability scanning assessments should be used as a starting point to guide and focus penetration testing efforts.

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
* Subcontrol 20.1: Establish a Penetration Testing Program

Inputs
-----------
#. Penetration Testing Program document

Operations
----------
#. Manually review the Penetration Testing Program document (Input 1) to verify that it instructs the organization to use vulnerability scan results to inform penetration testing efforts. The presence or absence of this instruction becomes M1.

Measures
--------
* M1 = Boolean value indicating if the Penetration Testing Program document includes instructions for using vulnerability scan results to inform penetration testing efforts; 1 if instructions are included, 0 otherwise.

Metrics
-------

Presence
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Presence or absence of instructions to use vulnerability scan results to inform 
	    | penetration testing efforts
	* - **Calculation**
	  - :code:`M1`

.. history
.. authors
.. license