8.4: Standardize Time Synchronization
=========================================================
Standardize time synchronization. Configure at least two synchronized time sources across enterprise assets, where supported.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory

Inputs
-----------
#. :code:`GV27`: Assets capable of supporting logging
#. List of approved network time sources/NTP servers


Operations
----------
#. Using :code:'GV27`, identify and enumerate assets capable of supporting time synchronization (M1)
#. Check the configurations of the assets identified in Operation 1
	#. Identify and enumerate the assets configured using at least two approved time sources from Input 2 (M2)
	#. Identify and enumerate the assets configured using time sources not on the approved list (M3)
	#. Identify and enumerate the assets not configured using time sources (M4)

Measures
--------
* M1 = Count of logging capable assets that support time synchronization
* M2 = Count of properly configured assets using at least two approve time sources
* M3 = Count of assets configured using non-approved time sources
* M4 = Count of assets not configured to use time sources

Metrics
-------

NTP Compliance Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets propery configured to with at least two 
	    | approved synchronized time sources.
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
