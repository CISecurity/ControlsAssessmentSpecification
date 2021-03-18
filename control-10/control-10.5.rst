10.5: Enable Anti-Exploitation Features
=====================================================================
Enable anti-exploitation features on enterprise assets and software, where possible, such as Microsoft® Data Execution Prevention (DEP), Windows® Defender Exploit Guard (WDEG), or Apple® System Integrity Protection (SIP) and Gatekeeper™.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
-----------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV3`: Configuration standards

Operations
----------
#. For each asset in :code:`GV1`, use configuration standards :code:`GV3` to determine if it is propely configured to enable anti-exploitation features
	#. Identify and enumerate assets properly configured to enable anti-exploitation features (M2)
	#. Identify and enumerate assets not properly configured to enable anti-exploitation features (M3)

Measures
--------
* M1 = Count of :code:`GV1`
* M2 = Count of assets properly configured to enable anti-exploitation feautures
* M3 = Count of assets not properly configured to enable anti-exploitation features


Metrics
-------

Coverage
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets properly configured to enable 
	  - | anti-exploitation features.
	* - **Calculation**
	  - :code:`M2 / M1`


.. history
.. authors
.. license
