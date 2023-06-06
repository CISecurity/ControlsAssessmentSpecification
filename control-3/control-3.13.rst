3.13: Deploy a Data Loss Prevention Solution
==================================
Implement an automated tool, such as a host-based Data Loss Prevention (DLP) tool to identify all sensitive data stored, processed, or transmitted through enterprise assets, including those located onsite or at a remote service provider, and update the enterprise's sensitive data inventory.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 3

Dependencies
------------
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 3.2: Establish and Maintain a Data Inventory

Inputs
------
#. :code:`GV18`: Enterprise assets storing, processing, or transmitting sensitive data
#. :code:`GV5`: Authorized Software inventory
#. :code:`GV3`: Configuration Standards

Operations
----------
#. Use :code:`GV5` to identify and enumerate all data loss prevention software 
#. Compare :code:`GV18` and the output of Operation 1 
	#. Identify and enumerate each asset in :code:`GV18` with data loss prevention software installed (M2)
	#. Identify and enumerate each asset in :code:`GV18` without data loss prevention software installed (M3)
#. For assets with data loss prevention installed from Operation 2.1 check :code:`GV3` for configuration information
	#. Identify and enumerate assets with properly configured data loss prevention software (M4)
	#. Identify and enumerate assets with improperly configured data loss prevention software (M5)


Measures
--------
* M1 = Count of :code:`GV18`
* M2 = Count of assets with data loss prevention software
* M3 = Count of assets without data loss prevention software
* M4 = Count of assets with properly configured data loss prevention software
* M5 = Count of assets with improperly configured data loss prevention software

Metrics
-------

Coverage
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets covered by at least one properly configured 
	    | data loss prevention software instance.
	* - **Calculation**
	  - :code:`M4 / M1`


.. history
.. authors
.. license
