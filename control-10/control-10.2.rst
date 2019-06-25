10.2: Perform Complete System Backups
======================================
Ensure that all of the organization’s key systems are backed up as a complete system, through processes such as imaging, to enable the quick recovery of an entire system.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 1, 2, 3

Status
------
Draft

Inputs
-----------
#. The list of "key systems" identified by the organization
#. The organization's backup/imaging configuration policy

Assumptions
^^^^^^^^^^^
* Backup software (either OS or 3d party) is installed and appropriately configured on "key systems" identified in Input 1

Operations
----------
#. Compare each "key system"'s backup configuration with available configuration policy.

Measures
--------
* M1 = 1 if "key system" backup configuration policy meets policy requirements; 0 otherwise
* M2 = The total number of endpoints defined as "key systems"


Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Question**
	  - What percentage of key systems are successfully backed up as a complete system?
	* - **Answer**
	  - 
	* - **Calculation**
	  - :code:`(SUM of M1 from 1..M2) / M2`

.. history
.. authors
.. license