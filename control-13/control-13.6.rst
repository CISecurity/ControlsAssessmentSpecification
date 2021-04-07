13.6: Collect Network Traffic Flow Logs 
=========================================================
Collect network traffic flow logs and/or network traffic to review and alert upon from network devices.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Detect
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 4.2: Establish and Maintain a Secure Configuration Process for Network Infrastructure
* Safeguard 12.4: Establish and Maintain Architecture Diagram(s)

Inputs
-----------
#. :code:`GV35`: Assets that are part of the network infrastructure
#. :code:`GV37`: Network infrastructure configuration standards

Operations
----------
#. Use Input 1 :code:`GV35` to identify and enumerate network boundary assets (M1)
#. For each network boundary asset identified in Operation 1, check configurations :code:`GV37` to determine if network traffic or network traffic flow loggins is enabled
	#. Identify and enumerate assets with either network traffic flow or network traffic logging enabled (M2)
	#. Identify and enumerate assets that have neither network traffic flow or network traffic logging enabled (M3)

Measures
--------
* M1 = Count of network boundary assets
* M2 = Count of properly configured network boundary assets
* M3 = Count of improperly configured network boundary assets


Metrics
-------

Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of network boundary assets properly configured to log
	    | network traffic flow or network traffic
	* - **Calculation**
	  - :code:`M2 / M1`


.. history
.. authors
.. license
