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

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 5.1: Establish Secure Configurations

Inputs
-----------
#. KS: The list of "key systems" identified by the organization, as derived from the endpoint inventory (see sub-control 1.4)
#. The organization's backup/imaging configuration policy

Assumptions
^^^^^^^^^^^
* Backup software (either OS or 3d party) is installed and appropriately configured on "key systems" identified in Input 1

Operations
----------
#. For each endpoint in the list of "key systems", examine its backup configuration against the available backup configuration policy, noting appropriately and inappropriately configured endpoints along the way.

Measures
--------
* M1 = List of "key system" endpoints
* M2 = Count of M1
* M3 = List of appropriately configured "key systems"
* M4 = Count of M3
* M5 = List of inappropriately configured "key systems"
* M6 = Count of M5

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - What percentage of key systems are successfully backed up as a complete system?
	* - **Calculation**
	  - :code:`M4 / M2`

.. history
.. authors
.. license
