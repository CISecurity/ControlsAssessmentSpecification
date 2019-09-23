10.5: Ensure All Backups Have at Least One Offline Backup Destination
=====================================================================
Ensure that all backups have at least one offline (i.e., not accessible via a network connection) backup destination.

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
* Sub-control 5.1: Establish Secure Configurations

Inputs
-----------
#. EI: List of endpoints
#. Backup configuration policy assuming inclusion of "offline" backup destination

Operations
----------
#. Collect list of endpoints matching/not-matching policy specified by Input 2

Measures
--------
* M1 = List of endpoints
* M2 = Count of M1
* M3 = List of endpoints matching policy
* M4 = Count of M3
* M5 = List of endpoints not matching policy
* M6 = Count of M5

Metrics
-------

Coverage
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - What is the ratio of endpoints matching the backup configuration policy to the total number of endpoints?
	* - **Calculation**
	  - :code:`M4 / M2`

Lack of Coverage
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - What is the ratio of endpoints *not* matching the backup configuration policy to the total number of endpoints?
	* - **Calculation**
	  - :code:`M5 / M2`

.. history
.. authors
.. license
