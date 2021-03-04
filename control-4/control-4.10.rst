4.10: Enforce Automatic Device Lockout on Portable End-User Devices
===============================================================
Enforce automatic device lockout following a predetermined threshold of local failed authentication attempts on portable end-user devices, where supported. For laptops, do not allow more than 20 failed authentication attempts; for tablets and smartphones, no more than 10 failed authentication attempts. Example implementations include Microsoft® InTune Device Lock and Apple® Configuration Profile maxFailedAttempts.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Respond
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safegaurd 4.1: Establish and Maintain a Secure Configuration Process

Inputs
------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV3`: Configuration standards

Operations
----------
#. Use :code:`GV1` to identify and enumerate all portable devices (M1)
#. Use :code:`GV3` to check failed authentication configuration for all portable devices
	#. Identify and enumerate failed authentication on laptops that is properly configured (20 failed attempts or less) (M2)
	#. Identify and enumerate failed authentication on laptops that is not properly configured (greater than 20 failed attempts) (M3)
	#. Identify and enumerate failed authentication on mobile devices that is properly configured (10 failed attempts or less) (M4)
	#. Identify and enumerate failed authentication on mobile devices that is not properly configured (greater than 10 failed attempts) (M5)

Measures
--------
* M1 = Count of portable devices
* M2 = Count of properly configured laptops
* M3 = Count of improperly configured laptops
* M4 = Count of properly configured mobile devices
* M5 = Count of improperly configured mobile devices

Metrics
-------

Compliance of Default Lockout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of portable devices with properly configured 
	    | failed authentication.
	* - **Calculation**
	  - :code:`(M2 + M4) / M1`


.. history
.. authors
.. license
