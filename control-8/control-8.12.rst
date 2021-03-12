8.12: Collect Service Provider Logs
=========================================================
Collect service provider logs, where supported. Example implementations include collecting authentication and authorization events, data creation and disposal events, and user management events

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Detect
	  - 3

Dependencies
------------
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process
* Safeguard 15.1: Establish and Maintain an Inventory of Service Providers

Inputs
------
#. :code:`GV29`: Inventory of service providers
#. :code:`GV3`: Configuration standard

Operations
----------
#. For each service provided in :code:`GV29` identify and enumerate service providers that supports logging (M1)
#. Use service provider identified in Operation 1, use :code:`GV3` to check configurations
	#. Identify and enumerate service providers properly configured to collect logs (M2)
	#. Identify and enumerate service providers not properly configured to collect logs (M3)

Measures
--------
* M1 = Count of service providers that support logging
* M2 = Count of service providers configured to collect logs
* M3 = Count of service providers not configured to collect logs

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of service providrs proverly configured 
	    | to collect logs
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
