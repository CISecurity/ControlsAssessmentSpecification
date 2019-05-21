1.1: Utilize an Active Discovery Tool
=====================================

Utilize an active discovery tool to identify devices connected to the organization’s network and update the hardware asset inventory.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Identify
	  - 2, 3

Status
------
Draft

Assumptions
-----------
These measurements assume the total number of assets for a given enterprise is known, and that an active discovery tool is being utilized.

Measures
--------
* M1 = number of assets discovered
* M2 = total number of assets (given)
* M3 = time asset discovered
* M4 = time asset appeared
* M5 = max time discovery (given)

Metrics
-------

Coverage (Quality Measure)
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - Given the total inventory of assets, what percentage of those assets are discovered in the enterprise?
	* - **Answer**
	  - This metric intends to determine the percentage of discovered assets in the enterprise that are accounted for in that enterprise's asset inventory.
	* - **Calculation**
	  - :code:`(M1/M2) * 100`

Freshness (Time to Discover)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - How quickly are new assets discovered, once added to the enterprise's network?
	* - **Answer**
	  - This metric will yield a positive value, generally between 0 and 1 but potentially greater than 1.  A value of 0 indicates the asset was immediately discovered, while a value greater than or equal to 1 indicates the asset requried at least the current maximium time to discover the asset.
	* - **Calculation**
	  - :code:`(M3-M4)/M5`

.. history
.. authors
.. license