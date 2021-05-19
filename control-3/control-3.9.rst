3.9: Encrypt Data on Removable Media
==================================
Encrypt data on removable media.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV5`: Authorized software inventory
#. :code:`GV3`: Configuration Standards

Assumptions
----------
#. Enterprise asset inventory includes removable media

Operations
----------
#. Use :code:`GV1` to identify and enumerate assets authorized to support removeable media (M1)
#. Use :code:`GV5` to identify encryption software installed on assets identified in Operation 1 (M1)
	#. Enumerate the number of assets with encryption software installed (M2)
	#. Enumerate the number of assets without encryption software installed (M3)
#. For assets identified in Operation 2.1, use :code:`GV3` to check configurations of encryption software
	#. Enumerate assets that have properly configured encryption software (M4)
	#. Enumerate assets that have improperly configured encryption software(M5)

Measures
--------
* M1 = Count of assets authorized to support removeable media
* M2 = Count of authorized assets with encryption software installed
* M3 = Count of authorized assets without encryption software installed
* M4 = Count of authorized assets with properly configured encryption software
* M5 = Count of authorized assets with improperly configured encryption software

Metrics
-------

Coverage
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of appropriately configured assets to support removeable media.
	* - **Calculation**
	  - :code:`M4 / M1`


.. history
.. authors
.. license
