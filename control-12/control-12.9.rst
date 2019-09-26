12.9: Deploy Application Layer Filtering Proxy Server
=========================================================
Ensure that all network traffic to or from the Internet passes through an authenticated application layer proxy that is configured to filter unauthorized connections.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Detect
	  - 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 2.1: Maintain Inventory of Authorized Software
* Sub-control 2.5: Integrate Software and Hardware Asset Inventories

Inputs
-----------
#. The list of endpoints
#. The list of authorized software
#. The list of unauthorized connections

Operations
----------
#. Enumerate network devices guarding Internet network boundaries
#. Enumerate application-layer proxies
#. For each application-layer proxy
	#. Enumerate the network boundary devices it covers
	#. For each Internet network boundary device it covers
		#. Ensure it is appropriately configured to filter against the list of unauthorized connections
#. Enumerate the set of covered Internet network boundary devices

Measures
--------
* M1 = List of Internet network boundary devices
* M2 = List of application-layer proxies
* M3 = List of appropriately configured application-layer proxies
* M4 = List of inappropriately configured application-layer proxies
* M5 = List of covered Internet network boundary devices
* M6 = Count of Internet network boundary devices (count of M1)
* M7 = Count of application-layer proxies (count of M2)
* M8 = Count of appropriately configured application-layer proxies (count of M3)
* M9 = Count of inappropriately configured application-layer proxies (count of M4)
* M10 = Count of covered Internet network boundary devices (count of M5)

Metrics
-------

Proxy Coverage
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured application-layer proxies to the total number
	    | of application-layer proxies.
	* - **Calculation**
	  - :code:`M8 / M7`

Internet Network Boundary Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of covered Internet network boundary devices to the total number of Internet
	    | network boundary devices
	* - **Calculation**
	  - :code:`M10 / M6`

.. history
.. authors
.. license
