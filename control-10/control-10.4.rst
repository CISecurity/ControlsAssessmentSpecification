10.4: Protect Backups
=====================
Ensure that backups are properly protected via physical security or encryption when they are stored, as well as when they are moved across the network. This includes remote backups and cloud services.

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
#. The list of endpoints configured for periodic backup
#. The organization's backup configuration policy

Assumptions
^^^^^^^^^^^
* Backup software (either OS or 3d party) is installed and appropriately configured on endpoints identified in Input 1

Operations
----------
#. Interrogate the organization's backup configuration policy to determine if backups are configured to be encrypted
#. Compare each endpoint's backup configuration with available configuration policy.

Measures
--------
* M1 = 1 if an endpoint's backup configuration policy ensures the backup is encrypted; 0 otherwise
* M2 = The total number of endpoints configured for periodic backup

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Question**
	  - What percentage backups are protected via physical security/encryption?
	* - **Answer**
	  - 
	* - **Calculation**
	  - :code:`(SUM of M1 from 1..M2) / M2`

.. history
.. authors
.. license