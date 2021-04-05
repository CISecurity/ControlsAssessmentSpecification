12.8: Establish and Maintain Dedicated Computing Resources for All Administrative Work
==============================================================
Establish and maintain dedicated computing resources, either physically or logically separated, for all administrative tasks or tasks requiring administrative access. The computing resources should be segmented from the enterprise's primary network and not be allowed internet access.

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
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 4.2: Establish and Maintain a Secure Configuration Process for Network Infrastructure

Inputs
-----------
#. :code:`GV1`: Enterprise Asset Inventory
#. :code:`GV37`: Network infrastructure configuration standards

Operations
----------
#. Use Input 1 :code:`GV1` to identify and enumerate assets used for administrative purposes (M1)
#. For each asset identified in Operation 1, use Input 2 :code:`GV37` to check configurations
	#. Identify and enumerate assets that do not have internet access (M2)
	#. Identify and enumerate assets that have internet access (M3)
	#. Identify and enumerate assets that are physically or logically seperated from the primary network (M4)
	#. Identify and enumerate assets that are not physically or logically seperated from the primary network (M5)
#. Compare the ouput of Operation 2.1 and 2.3
	#. Identify and enumerate assets that do not have internet access and are physically or logically seperated (M6)

Measures
--------
* M1 = Count of assets used for administrative purposes
* M2 = Count of assets configured to not allow internet access
* M3 = Count of assets configured to allow internet access
* M4 = Count of assets physically or logically seperated from the primary network
* M5 = Count of assets not physically or logically seperated from the primary network
* M6 = Count of assets configured to not allow internet acces and are physically or logically seperated


Metrics
-------

Compliance
^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of properlu configured administrative assets 
	* - **Calculation**
	  - :code:`M6 / M1`

.. history
.. authors
.. license
