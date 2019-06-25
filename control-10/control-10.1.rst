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
* M1 = 1 if endpoint backup configuration policy meets policy requirements; 0 otherwise
* M2 = 1 if last successful backup is within the "staleness" threshold; 0 otherwise
* M3 = Total number of endpoints

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Question**
	  - What percentage of endpoints are successfully backing up system data on a regular basis?
	* - **Answer**
	  - 
	* - **Calculation**
	  - :code:`(SUM from 1..M3 (M1 AND M2)) / M3`

.. history
.. authors
.. license