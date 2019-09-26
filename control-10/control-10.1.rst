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

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 5.1: Establish Secure Configurations

Inputs
-----------
#. EI: Endpoint Inventory
#. Backup configuration policy is available
#. Backup software (either OS or 3d party) configuration is available and able to be queried
#. Backup software logs are available and can be queried
#. Successful backup staleness threshold is defined (a maximum time period allowed between backups; recommended value of at least weekly)

Operations
----------
#. For each endpoint, examine its backup configuration with the available configuration policy (noting appropriately configured and inappropriately configured endpoints along the way), and examine its logs to determine the most recent successful backup completion time (noting whether it was run within the enterprise-defined staleness threshold).
# Enumerate the endpoints that are both appropriately configured and do not have stale backups

#. Compare an endpoints backup configuration with available configuration policy
#. Interrogate logs to determine most recent successful backup completion time

Measures
--------
* M1 = List of endpoints
* M2 = Count of M1
* M3 = List of appropriately configured endpoints
* M4 = Count of M3
* M5 = List of inappropriately configured endpoints
* M6 = Count of M5
* M7 = List of endpoints both appropriately configured and without stale backups
* M8 = Count of M7
* M9 = List of endpoints either inappropriately configured or without stale backups
* M10 = Count of M9

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - What percentage of endpoints are successfully backing up system data on a regular basis?
	* - **Calculation**
	  - :code:`M8 / M2`

.. history
.. authors
.. license
