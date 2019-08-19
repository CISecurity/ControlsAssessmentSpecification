1.2: Use a Passive Asset Discovery Tool
=======================================

Utilize a passive discovery tool to identify devices connected to the organization’s network and automatically update the organization’s hardware asset inventory.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Identify
	  - 3

Status
------
In Development

Inputs
-----------
#. These measurements assume the total number of assets for a given enterprise is known (M2), and that the max asset discovery time (M5) is known.

Operations
----------

Measures
--------
* M1 = number of assets discovered
* M2 = total number of assets (given)
* M3 = time asset discovered
* M4 = time asset appeared (given)
* M5 = max time discovery (given)

Metrics
-------

Coverage (Quality Measure)
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Given the total inventory of assets, what percentage of those assets are discovered
	    | in the enterprise?
	* - **Calculation**
	  - :code:`M1 / M2`

Freshness (Time to Discover)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | How quickly are new assets discovered, once added to the enterprise's network?
	* - **Calculation**
	  - :code:`(M3 - M4) / M5`

.. history
.. authors
.. license