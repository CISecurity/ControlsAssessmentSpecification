10.3: Disable Autorun and Autoplay for Removable Media
=========================================================
Disable autorun and autoplay auto-execute functionality for removable media.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 1, 2, 3

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
#. Use :code:`GV1` to identify and enumerate enterprise assets capable of performing autorun, autoplay, and auto-execute functions (M1)
#. Check the configurations :code:`GV3` of each asset identified in Operation 1 to see if the autorun, autoplay, and auto-execute functions are disabled
	#. Identify and enumerate properly configured assets (M2)
	#. Identify and enumerate improperly configured assets (M3)

Measures
--------
* M1 = Count of assets capable of performing autorun, autoplay, and auto-excecute functions
* M2 = Count of assets properly configured to disable functions
* M3 = Count of assets not properly configured to disable functions


Metrics
-------

Compliance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets properly configured to disable autorun, autoplay
	  - | and autoexecute functions.
	* - **Calculation**
	  - :code:`M2 / M1` 

.. history
.. authors
.. license
