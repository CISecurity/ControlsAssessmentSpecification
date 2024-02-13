3.11: Encrypt Sensitive Data At Rest 
==================================
Encrypt sensitive data at rest on servers, applications, and databases containing sensitive data. Storage-layer encryption, also known as server-side encryption, meets the minimum requirement of this Safeguard. Additional encryption methods may include application-layer encryption, also known as client-side encryption, where access to the data storage device(s) does not permit access to the plain-text data. 

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
------
#. :code:`GV12`: Sensitive data inventory
#. :code:`GV4`: Enterprise Network Architecture Documentation
#. :code:`GV18`: Enterprise assets storing sensitive data

Operations
----------
#. Use :code:`GV5` to identify and enumerate all encryption tools requiring secondary authentication systems (M1)
#. Use :code:`GV12` and :code:`GV1` to identify and enumerate all enterprise assets storing sensitive data (:code:`GV19`: M2)
#. Compare the output of Operation 1 and Operation 2
	#. Identify and enumerate assets with at least one encryption tool from M1 installed (M4)
	#. Identify and enumerate assets without at least one encryption tool from M1 installed (M5)

Measures
--------
* M1 = Count of authorized encryption tools requiring secondary authentication systems
* M2 = Count of enterprise assets storing sensitive data
* M3 = Count of assets with at least one encryption tool installed
* M4 = Count of assets without at least one encryption tool installed

Metrics
-------

Coverage
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets storing sensitive data covered by an encryption 
	  - | tool.
	* - **Calculation**
	  - :code:`M3 / M2`


.. history
.. authors
.. license
