10.1: Deploy and Maintain Anti-Malware Software
=======================================
Deploy and maintain anti-malware software on all enterprise assets.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
-----------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV5`: Authorized sofware inventory
#. :code:`GV3`: Configuration standards

Operations
----------
#. Use :code:`GV1` to identify and enumerate assets capable of supporting anti-malware software: :code:`GV30` (M1)
#. Use :code:`GV5` to identify authorized anti-malware software: :code:`GV31`
#. For each asset identified in Operation 1, use the output of Operation 2
	#. Identify and enumerate assets with at least one authorized anti-malware software intalled: :code:`GV32` (M2)
	#. Identify and enumerate assets with only unauthorized anti-malware software installed (M3)
	#. Identify and enumerate assets without any anti-malware software installed (M4)
#. For each asset wih a least one authorized anti-malware software installed from Operation 3.1, use :code:`GV3` to check configurations
	#. Identify and enumerate assets with properly configured anti-malware software (M5)
	#. Identify and enumerate assets with improperly configured anti-malware software (M6)


Measures
--------
* M1 = Count of assets capable of supporting anti-malware software
* M2 = Count of assets with at least one authorized anti-malware software installed
* M3 = Count of assets with only unauthorized anti-malware software installed
* M4 = Count of assets without any anti-malware software installed
* M5 = Count of assets with properly configured authorized anti-malware software installed
* M6 = Count of assets with improperly configured authorized anti-malware software installed


Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets with properly configured authorized 
	  - | anti-malware installed
	* - **Calculation**
	  - :code:`M5 / M1`

.. history
.. authors
.. license
