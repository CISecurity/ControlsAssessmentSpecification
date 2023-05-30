11.2: Perform Automated Backups 
=========================================================
Perform automated backups of in-scope enterprise assets. Run backups weekly, or more frequently, based on the sensitivity of the data.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Recover
	  - 1, 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV5`: Authorized software inventory
#. :code:`GV3`: Configuration standards


Operations
----------
#. For each asset in :code:`GV1` identify and enumerate assets that are in-scope for automated backups: :code:`GV33` (M1) 
#. Use :code:`GV5` to identify authorized backup software and for each asset identified in Operation 1
	#. Identify and enumerate assets covered by at least one authorized backup software: :code:`GV34` (M2)
	#. Identify and enumerate assets not covered by at least one authorized backup software (M3)
#. Use :code:`GV3` to check if the software on assets identifed in Operation 2.1 is configured correctly
	#. Identify and enumerate assets with properly configured backup software (M4)
	#. Identify and enumerate assets with improperly configured backup software (M5)
#. For each asset with backup software identified in Operation 2.1, examine logs to determine the most recent successful backup date. Compare that date to current date and capture timeframe in days.
	#. Identify and enumerate assets that have been backed up within seven days or less (M6) 
	#. Identify and enumerate assets that have been backed up outside of a seven days window (M7)


Measures
--------
* M1 = Count of assets within scope for automated backups
* M2 = Count of in-scope assets with authorized backup software installed
* M3 = Count of in-scope assets without authorized backup software installed
* M4 = Count of in-scope assets with properly configured backup software
* M5 = Count of in-scope assets with improperly configured backup software
* M6 = Count of in-scope assets backed up within a week
* M7 = Count of in-scope assets not backed up within a week

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of in-scoope assets with properly configured authorized
	    | backup software
	* - **Calculation**
	  - :code:`M4 / M1`

Compliance
^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of in-scope assets backed up within a week timeframe
	* - **Calculation**
	  - :code:`M6 / M1`

.. history
.. authors
.. license
