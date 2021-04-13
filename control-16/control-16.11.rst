16.11: Leverage Vetted Modules or Services for Application Security Components
=========================================================
Leverage vetted modules or services for application security components, such as identity management, encryption, and auditing and logging. Using platform features in critical security functions will reduce developers’ workload and minimize the likelihood of design or implementation errors. Modern operating systems provide effective mechanisms for identification, authentication, and authorization and make those mechanisms available to applications. Use only standardized, currently accepted, and extensively reviewed encryption algorithms. Operating systems also provide mechanisms to create and maintain secure audit logs.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
-----------
#. :code:`GV5`: Authorized Software Inventory

Operations
----------
#. Use Input 1 :code:`GV5` to identify and enumerate application security components (M1)
#. For each application security component identifed in Operation 1, determine whether custom code exists
	#. Identify and enumerate components that contain custom code (M2)
	#. Identify and enumerate components that do not contain custom code (M3)
#. For each application security component identifed in Operation 2.1, determine whether vetted modules or services exist
	#. Identify and enumerate components for which vetted modules or services exist (M4)
	#. Identify and enumerate components for which vetted modules or services do not exist (M5)

Measures
--------
* M1 = Count of application security components 
* M2 = Count of application security components containing custom code
* M3 = Count of application security components not containing custom code
* M4 = Count of application security components containing custom code and vetted modules or services do exist
* M5 = Count of application security components containing custom code and vetted modules or services do not exist

Metrics
-------

Compliance
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of application security components using vetted modules
	    | or services when available
	* - **Calculation**
	  - :code:`(M3 + M5) / M1`


.. history
.. authors
.. license
