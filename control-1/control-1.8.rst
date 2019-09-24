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

Status
------
Draft

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
------
#. The list of endpoints

Operations
----------
#. Enumerate hardware devices (physical and virtual) from the endpoint inventory
#. For each hardware device, examine device client authentication certificate configuration noting appropriate and inappropriate configurations

Measures
--------
* M1 = List of hardware devices (operation 1)
* M2 = List of appropriately configured hardware devices (operation 2)
* M3 = List of inappropriately configured hardware devices (operation 2)
* M4 = Count of hardware devices (count of M1)
* M5 = Count of appropriately configured hardware devices (count of M2)
* M6 = Count of inappropriately configured hardware devices (count of M3)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured hardware devices to the number of hardware devices
	* - **Calculation**
	  - :code:`M5 / M4`

.. history
.. authors
.. license
