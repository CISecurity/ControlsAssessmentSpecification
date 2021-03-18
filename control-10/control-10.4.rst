10.4: Configure Automatic Anti-Malware Scanning of Removable Media
=====================
Configure anti-malware software to automatically scan removable media.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Detect
	  - 2, 3

Dependencies
------------
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process
* Safeguard 10.1: Deploy and Maintain Anti-Malware Software

Inputs
-----------
#. :code:`GV30`: Assets capable of supporting anti-malware software
#. :code:`GV32`: Assets with at least one authorized anti-malware software intalled
#. :code:`GV3`: Configuration standards

Operations
----------
#. For each asset in Input 2 :code:`GV32`, use configurations :code:`GV3` to identify if software is configured to automatically scan removable media
	#. Identify and enumerate assets with properly configured software (M2)
	#. Identify and enumerate assets with improperly configured software (M3)

Measures
--------
* M1 = Count of :code:`GV30`
* M2 = Count of assets with anti-malware properly configured to scan removable media
* M3 = Count of assets with anti-malware not properly configured to scan removable media

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets with properly configured software to automatically 
	  - | scan removable media.
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
