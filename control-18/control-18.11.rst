18.11: Use Standard Hardening Configuration Templates for Databases
====================================================================
For applications that rely on a database, use standard hardening configuration templates.  All systems that are part of critical business processes should also be tested.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - N/A
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information
* Subcontrol 2.1: Maintain Inventory of Authorized Software
* Subcontrol 2.5: Integrate Software and Hardware Asset Inventories
* Subcontrol 5.1: Establish Secure Configurations

Inputs
-----------
#. The list of database management software being used in the organization
#. The list of systems on which database instances reside
#. The list of enterprise security configuration standards

Operations
----------
#. Determine, from the list of enterprise security configuration standards, which are applicable to database management software (M1)
#. From the list of enterprise security configuration standards, calculate the number of database management software that are covered by the standards (perform the intersection of the results of Operation 1 with Input 1; the result is M2)

Measures
--------
* M1 = The number of enterprise security configuration standards specific to database management software
* M2 = The number of database management software covered by applicable enterprise security configuration standards

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of database management software covered by applicable enterprise security 
	    | configuration standards to the total number of database management software
	* - **Calculation**
	  - :code:`?`

**NOTE**: The second ask of this sub-control speaks to assessment of Input 2 against security configuration standards determined by Operation 1.

.. history
.. authors
.. license