4.6: Securely Manage Enterprise Assets and Software
============================================================
Securely manage enterprise assets and software. Example implementations include managing configuration through version-controlled-infrastructure-as-code and accessing administrative interfaces over secure network protocols, such as Secure Shell (SSH) and Hypertext Transfer Protocol Secure (HTTPS). Do not use insecure management protocols, such as Telnet (Teletype Network) and HTTP, unless operationally essential.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
-----------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV5`: Authorized software inventory
#. :code:`GV3`: Configuration standard

Operations
----------
#. Using :code:`GV5` identify and enumerate authorized management software (M1)
#. Using :code:`GV1` identify and enumerate assets capable of supporting management software (M2)
#. Using the output of Operations 1 and 2, identify and enumerate assets with authorized management software installed (M3)
#. Using configuration standards :code:`GV3` to check if management software is configured properly
	#. Enumerate assets from Operation 3 with properly configured management software (M4)
	#. Enumerate assets from Operation 1 with improperly configured mangement software (M5)

Measures
--------
* M1 = Count of authorized management software
* M2 = Count of enterprise assets capable of supporting management software
* M3 = Count of assets with authorized management software installed
* M4 = Count of assets with properly configured management software
* M5 = Count of assets with improperly configured management software

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets with properly configured authorized management software
	* - **Calculation**
	  - :code:`M4 / M2`

.. history
.. authors
.. license
