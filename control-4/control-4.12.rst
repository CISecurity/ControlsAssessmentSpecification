4.12: Separate Enterprise Workspaces on Mobile End-User Devices
===============================================================
Ensure separate enterprise workspaces are used on mobile end-user devices, where supported. Example implementations include using an Apple® Configuration Profile or Android™ Work Profile to separate enterprise applications and data from personal applications and data.

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
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
------
#. :code:`GV21`: Portable end-user devices
#. :code:`GV5`: Authorized software inventory
#. :code:`GV3`: Configuration standards

Operations
----------
#. Use :code:`GV5` to identify and enumerate authorized mobile device management software (M1)
#. Use :code:`GV21` to identify mobile devices capable of supporting mobile device management software (M2)
#. Compare the output of Operations 1 and 2
	#. Identify and enumerate mobile devices with authorized mobile device management software (M3)
	#. Identify and enumerate mobile devices without authorized mobile device management software (M4)
#. Use :code:`GV3` to check configurations of mobile devices with mobile device management software
	#. Identify and enumerate mobile devices with properly configured mobile device management software to seperate enterprise workspace (M5)
	#. Identify and enumerate mobile devices with improperly configured mobile device management sotware (M6)

Measures
--------
* M1 = Count of authorized mobile device management software
* M2 = Count of mobile devices capable of supporting mobile device management software
* M3 = Count of mobile devices with mobile device management software
* M4 = Count of mobile devices without mobile device management software
* M5 = Count of asssets with properly configured mobile device management software
* M6 = Count of asssets with improperly configured mobile device management software


Metrics
-------

Compliance of Seperation of Enterprise Workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of mobile devices with properly seperated enterprise
	  - | workspace.
	* - **Calculation**
	  - :code:`M5 / M2`


.. history
.. authors
.. license
