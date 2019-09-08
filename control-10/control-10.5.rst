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
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. List of endpoints
#. Backup configuration policy assuming inclusion of "offline" backup destination

Operations
----------
#. Collect list of endpoints matching/not-matching policy specified by Input 2

Measures
--------
* M1 = count of endpoints matching
* M2 = count of endpoints not matching
* M3 = total count of endpoints (M1 + M2 needs to equal M3)

Metrics
-------

Coverage
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - What is the ratio of endpoints matching the backup configuration policy to the total number of endpoints?
	* - **Calculation**
	  - :code:`M1 / M3`

Lack of Coverage
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - What is the ratio of endpoints *not* matching the backup configuration policy to the total number of endpoints?
	* - **Calculation**
	  - :code:`M2 / M3`

.. history
.. authors
.. license