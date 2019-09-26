8.2: Ensure Anti-Malware Software and Signatures Are Updated
============================================================
Ensure that the organization’s anti-malware software updates its scanning engine and signature database on a regular basis.

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
* Sub-control 1.4: Integrate Software and Hardware Asset Inventories
* Sub-control 2.1: Maintain Inventory of Authorized Software
* Sub-control 2.4: Track Software Inventory Information

Inputs
-----------
#. EI: Endpoint inventory (with entry for each endpoint indicating whether that endpoint can support anti-malware software or not; sub-control 1.4)
#. Anti-malware software version information (this is a list of acceptable versions for the scanning engines and the signature databases for any anti-malware products in use on endpoints in Input 1; this version information needs to be updated frequently to reflect current version information and age off outdated versions; reference the ASL per sub-control 2.1 and ideally leverage the software inventory in sub-control 2.4)
#. Maximum time allowed for anti-malware software updates to be applied to endpoints

Assumptions
^^^^^^^^^^^
* Some endpoints, such as network devices, may not support anti-malware software. Whether an endpoint supports anti-malware software is provided as part of Input 1. Devices that cannot support anti-malware software are removed from the list of endpoints to be checked during Operation 1, and these devices are not counted in the metric below.

Operations
----------
#. Refine the endpoint inventory (Input 1) to only contain endpoints that can support anti-malware software endpoint inventory - this reduced list of endpoints becomes M1
#. For each endpoint in M1, generate a list of those endpoints that have an acceptable version of anti-malware software installed and enabled (both scanning engine and signature database) according to the information provided in Input 2 (M2) and a list of those endpoints that do not have an acceptable version of anti-malware software installed and enabled (M3).
#. For each endpoint in M1, generate a list of those endpoints that have been updated within the time frame specified by Input 3 (M4), and a list of those endpoints that have not been updated within that time-frame (M5)

Measures
--------
* M1 = List of endpoints capable of supporting anti-malware software
* M2 = List of endpoints with an acceptable version of anti-malware software installed and enabled (version compliant list)
* M3 = List of endpoints that do not have an acceptable version of anti-malware software installed and enabled (version non-compliant list)
* M4 = List of endpoints that have had their anti-malware software updated within the specified time-frame (time compliant list)
* M5 = List of endpoints that have not had their anti-malware software updated within the specified time-frame (time non-compliant list)
* M6 = Count of endpoints in M1 (number of endpoints capable of supporting anti-malware software)
* M7 = Count of endpoints in M2 (number of version compliant endpoints)
* M8 = Count of endpoints in M3 (number of version non-compliant endpoints)
* M9 = Count of endpoints in M4 (number of time compliant endpoints)
* M10 = Count of endpoints in M5 (number of endpoints that have not had updates within acceptable time frame)

Metrics
-------

Coverage
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of anti-malware software version compliant endpoints to the total number
	    | of endpoints capable of supporting anti-malware software?
	* - **Calculation**
	  - :code:`M7 / M9`

Freshness
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints whose anti-malware software has been updated within the specified
	    | timeframe?
	* - **Calculation**
	  - :code:`M9 / M6`

**NOTE**: Comparing the coverage metric to the freshness metric can serve as a useful check - for instance, if the coverage metric tends to be high, while the freshness metric is low, that would suggest that Input 2 might not have been updated recently enough (that is, outdated versions are being considered acceptable)?

.. history
.. authors
.. license
