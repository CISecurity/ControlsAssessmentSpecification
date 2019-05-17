1.4: Maintain Detailed Asset Inventory
======================================

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Identify
	  - 1, 2, 3

**Description**

Maintain an accurate and up-to-date inventory of all technology assets with the potential to store or process information. This inventory shall include all assets, whether connected to the organization’s network or not.

**Status**: Draft

**Measures**

* M1 = number of assets discovered
* M2 = total number of assets (given)
* M3 = time asset discovered
* M4 = time asset appeared (given)
* M5 = Max time discovery (given)

**Assumptions**

This subcontrol requires an enterprise to:

* Have an inventory of all technology assets capable of storing or processing information, 
* Ensure the inventory is accurate, and
* Ensure the inventory is up-to-date.


**Metrics**

.. list-table:: Coverage 
	:widths: 20 40

	* - *Question*
	  - What percentage of assets discovered on the network are accounted for in the organization's asset inventory?
	* - *Answer*
	  - A positive percentage value greater than or equal to 0, and less than or equal to 100%  A value of "0" would indicate that none of the discovered assets have been inventoried; a value of "100" indicates that all assets connected to the organization's network are accounted for in the asset inventory.
	* - *Calculation*
	  - :code:`(M1/M2) * 100%`

--------

*Question*: How long does it take for an organization to discover a new asset on its network?

*Answer*: The "freshness" metric is a positive decimal value that is greater than or equal to zero. A value of "0" indicates hypothetical instant detection.

*Calculation*: ((M3-M4) / M5)

.. history
.. authors
.. license