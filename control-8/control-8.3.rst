8.3: Ensure Adequate Audit Log Storage
=========================================================================================
Ensure that logging destinations maintain adequate storage to comply with the enterprise’s audit log management process.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory

Inputs
-----------
#. :code:`GV27`: Assets capable of supporting logging
#. :code:`GV26`: Enterprise's audit log management process

Assumptions
----------
#. It is assumed that if the an asset is properly configured to meet the retention policy, that would include log rotation, maximum storage size, etc.

Operations
----------
#. For each asset in :code:`GV27` collect the asset's logging configuration 
#. Compare the output of Operation 1 and the retention portion of :code:`G26`
	#. Identify and enumerate assets configured to comply with the retention portion of the process (M2)
	#. Identify and enumerate assets not configured to comply with the retention portion of the process (M3)

Measures
--------
* M1 = Count of :code:`GV27` assets capable of supporting logging
* M2 = Count of assets properly configured to meet retention requirements
* M3 = Count of assets not properly configured to meet retention requirements

Metrics
-------

Logging Storage Coverage
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets compliant with the organization's logging 
	  - |  policy
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
