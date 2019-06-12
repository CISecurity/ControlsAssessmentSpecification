3.4: Deploy Automated Operating System Patch Management Tools
=============================================================
Deploy automated software update tools in order to ensure that the operating systems are running the most recent security updates provided by the software vendor.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 1, 2, 3

Status
------
Draft

Inputs
------
#. The required OS auto-update configuration (this could vary by organization, by product, by security tool, etc.). It could be 1 setting or multiple settings. It would need to be determined if partial settings are creditable, potential weighting of settings, any dependencies, etc. Such logic should all be part of Input 1.
#. The list of required updates (this could be pulled from the vendor's website, or could be an organization's selected subset of updates). *Optional Field*: If time metrics are desired, this list would also need a date when each update on the list was released by the vendor.
#. The list of endpoints to be checked.
#. *Optional*: If time metrics are desired, the allowable timeframe for installation of an update after its release.

Operations
----------
#. For each endpoint in Input 3, compare that endpoint's auto-update configuration to that provided in Input 1 and generate a score based on the logic provided by Input 1 (M1).
#. For each endpoint in Input 3, retrieve a list of installed OS updates (M2) and compare that endpoint's installed updates to the required updates provided by Input 2.  The list of matching updates is M3.
#. 

Measures
--------
* M1 = Endpoint-specific auto-update configuration score as determined in Operation 1.
* M2 = Endpoint-specific list of installed updates as determined in Operation 2.
* M3 = Endpoint-specific list of required updates that are installed, as determined in Operation 2.
* M4 = The number of required OS updates per Input 2.
* M5 = The number of required OS updates that are installed on the endpoint, per M3.

Metrics
-------

Update Ratio
^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - TBD
	* - **Answer**
	  - TBD
	* - **Calculation**
	  - :code:`?`

Freshness
^^^^^^^^^
.. list-table:

* - **Question**
	- TBD
* - **Answer**
	- TBD
* - **Calculation**
	- :code:`?`

.. history
.. authors
.. license
