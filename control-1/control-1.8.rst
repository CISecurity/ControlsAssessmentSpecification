1.8: Utilize Client Certificates to Authenticate Hardware Assets
================================================================
Use client certificates to authenticate hardware assets connecting to the organization’s trusted network.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
------
#. :code:`GV1`: Hardware Asset Inventory
#. :code:`GV2`: Count of Hardware Asset Inventory

Operations
----------
#. For each endpoint in the hardware asset inventory, examine the endpoint's client authentication certificate configuration noting appropriate (becomes M1) and inappropriate (becomes M2) configurations

Measures
--------
* M1 = List of appropriately configured endpoints (operation 2)
* M2 = List of inappropriately configured endpoints (operation 2)
* M3 = Count of appropriately configured hardware devices (count of M1)
* M4 = Count of inappropriately configured hardware devices (count of M2)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured hardware devices to the number of hardware devices
	* - **Calculation**
	  - :code:`M4 / GV2`

.. history
.. authors
.. license
