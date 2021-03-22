11.3: Protect Recovery Data
=====================================================================================
Protect recovery data with equivalent controls to the original data. Reference encryption or data separation, based on requirements.

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
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
------
#. :code:`GV33`: Assets that are in-scope for automated backups
#. :code:`GV34`: Assets with authorized backup software installed
#. :code:`GV3`: Configuration Standard

Operations
----------
#. For each asset with backup software installed, use :code:`GV3` to check if encryption is configured for backups
	#. Identify and enumerate assets with software configured to encrypt backups (M2)
	#. Identify and enumerate assets with software not configured to encrypt backups (M3)
 
Measures
--------
* M1 = Count of Input 1: :code:`GV33`
* M2 = Count of software configured to encrypt backups
* M3 = Count of software not configured to encrypt backups

Metrics
-------

Coverage
^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of in-scope assets with backup software properly configured
	  - | to encrypt backups.
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
