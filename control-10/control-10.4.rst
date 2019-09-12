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

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. The list of endpoints configured for periodic backup, derived from the endpoint inventory (see sub-control 1.4)
#. The organization's backup configuration policy

Assumptions
^^^^^^^^^^^
* Backup software (either OS or 3d party) is installed and appropriately configured on endpoints identified in Input 1

Operations
----------
#. Interrogate the organization's backup configuration policy to determine if backups are configured to be encrypted
#. For each endpoint, examine its backup configuration policy to ensure that encrypted backups are configured, noting appropriately and inappropriately configured endpoints along the way.

Measures
--------
* M1 = List of endpoints
* M2 = Count of M1
* M3 = List of appropriately configured endpoints
* M4 = Count of M3
* M5 = List of inappropriately configured endpoints
* M6 = Count of M5

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - What percentage backups are protected via physical security/encryption?
	* - **Calculation**
	  - :code:`M6 / M2`

.. history
.. authors
.. license
