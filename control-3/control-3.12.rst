3.12: Segment Data Processing and Storage Based on Sensitivity
==================================
Segment data processing and storage, based on the sensitivity of the data. Do not process sensitive data on enterprise assets intended for lower sensitivity data.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 3.2: Establish and Maintain a Data Inventory
* Safeguard 12.4: Establish and Maintain Architecture Diagram(s)

Inputs
------
#. :code:`GV12`: Sensitive Data Inventory
#. :code:`GV4`: Enterprise Network Architecture

Assumptions
----------
#. An asset’s overall sensitivity level should be the highest sensitivity level of the data it stores/processes/transmits. If a system contains any sensitive information, that asset should be treated accordingly, and should be properly separated from networks or network segments that don’t have a need to access that type of sensitive information.

Operations
----------
#. For each item in :code:`GV12` identify the assets that store, process, or transmit sensitive data (:code:`GV18: M1)
#. Use the output of Operation 1 and :code:`GV4` to identify networks/VLANs connected to the assets
	#. Identify and enumerate any instances of properly seperated assets from less sensitive networks (M2)
	#. Identify and enumerate any instances of improperly seperated assets from less sensitive networks (M3)

Measures
--------
* M1 = Count of assets storing, processing, or transmitting sensitive data
* M2 = Count of sensitive assets properly seperated from less sensitive networks 
* M3 = Count of sensitive assets improperly seperated from less sensitive networks

Metrics
-------

Coverage
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of properly seperated sensitive assets.
	* - **Calculation**
	  - :code:`M2 / M1`


.. history
.. authors
.. license
