4.11: Enforce Remote Wipe Capability on Portable End-User Devices
===============================================================
Remotely wipe enterprise data from enterprise-owned portable end-user devices when deemed appropriate such as lost or stolen devices, or when an individual no longer supports the enterprise.

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
* Safegaurd 4.1: Establish and Maintain a Secure Configuration Process

Inputs
------
#. :code:`GV21: Portable end-user devices
#. :code:`GV3`: Configuration standards

Operations
----------
#. Use :code:`GV21` to identify and enumerate portable end-user devices that support remote wipe (M1)
#. Use :code:`GV3` to check configuration for remote wipe on portable devices capable of supporting as identified in Operation 1
	#. Identify and enumerate portable devices with properly configured remote wipe (M2)
	#. Identify and enumerate portable devices with improperly configured remote wipe (M3)

Measures
--------
* M1 = Count of portable devices capable of supporting remote wipe
* M2 = Count of properly configured portable devices
* M3 = Count of improperly configured portable devices

Metrics
-------

Compliance of Remote Wipe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of portable devices with properly configured 
	    | remote wipe.
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
