8.4: Configure Anti-Malware Scanning of Removable Media
=========================================================
Configure devices so that they automatically conduct an anti-malware scan of removable media when inserted or connected.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Detect
	  - 1, 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 2.5: Integrate Software and Hardware Asset Inventories

Inputs
-----------
#. Endpoint inventory (with entry for each endpoint indicating whether that endpoint can support anti-malware software or not)
#. Desired anti-malware configuration (to automatically scan removable media when inserted/connected)
Assumption: Some endpoints, such as network devices, may not support anti-malware software. Whether an endpoint supports anti-malware software is provided as part of Input 1. Devices that cannot support anti-malware software are removed from the list of endpoints to be checked during Operation 1, and these devices are not counted in the metric below.

Operations
----------
#. Refine the endpoint inventory (Input 1) to only contain endpoints that can support anti-malware software endpoint inventory - this reduced list of endpoints becomes M1
#. Of the set of endpoints that can support anti-malware software (M1), generate a list of those endpoints that actually have anti-malware software installed, enabled, and adhere to the configuration specified in Input 2 (M2) and a list of the endpoints that do not adhere to the specified configuration (M3). Note: Endpoints in M1 that do not have anti-malware installed and enabled, are considered non-compliant and added to M3.

Measures
--------
* M1 = List of endpoints capable of supporting anti-malware software
* M2 = List of endpoints with anti-malware software installed, enabled, and properly configured to scan removable media (compliant list)
* M3 = List of endpoints not adhering to the specified configuration (non-compliant list)
* M4 = Number of endpoints in M1 (number of endpoints capable of supporting anti-malware software)
* M5 = Number of endpoints in M2 (number of compliant endpoints)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What is the ratio of endpoints compliant with the desired anti-malware configuration
	    | to the total number of endpoints capable of supporting anti-malware software?
	* - **Calculation**
	  - :code:`M5 / M4`

.. history
.. authors
.. license