11.4: Establish and Maintain an Isolated Instance of Recovery Data 
==============================================================================================
Establish and maintain an isolated instance of recovery data. Example implementations include, version controlling backup destinations through offline, cloud, or off-site systems or services.

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
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
-----------
#. :code:`GV33`: Assets that are in-scope for automated backups
#. :code:`GV34`: Assets with authorized backup software installed
#. :code:`GV3`: Configuration standards

Assumptions
----------
#. Configuration for backups will contain information about destination of backups

Operations
----------
#. For each asset in Input 2 :code:`GV34`, use configuration standards in :code:`GV3` to check destination of backups
	#. Identify and enumerate assets properly configured to send backups to an isolated instance (M2)
	#. Identify and enumerate assets not properly configured to send backups to an isolated instance (M3)

Measures
--------
* M1 = Count of Input 1 :code:`GV33`
* M2 = Count of assets with backups sent to an isolated instance 
* M3 = Count of assets with backups not sent to an isolated instance

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets configured to send backups to an isolated instance
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
