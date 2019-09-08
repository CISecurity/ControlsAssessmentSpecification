10.1: Ensure Regular Automated Backups
=======================================
Ensure that all system data is automatically backed up on a regular basis.

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

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. Backup configuration policy is available
#. Backup software (either OS or 3d party) configuration is available and queryable
#. Backup software logs are available and queryable
#. Successful backup "staleness" threshold is defined (a maximum time period allowed between backups)

Operations
----------
#. Compare an endpoints backup configuration with available configuration policy
#. Interrogate logs to determine most recent successful backup completion time

Measures
--------
* M1(i) = (For each endpoint "i") 1 if endpoint backup configuration policy meets policy requirements; 0 otherwise
* M2(i) = (For each endpoint "i") 1 if last successful backup is within the "staleness" threshold; 0 otherwise
* M3 = Total number of endpoints

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - What percentage of endpoints are successfully backing up system data on a regular basis?
	* - **Calculation**
	  - :code:`(SUM from i=1..M3 (M1(i) AND M2(i))) / M3`

.. history
.. authors
.. license