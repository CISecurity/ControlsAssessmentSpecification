16.7: Use Standard Hardening Configuration Templates for Application Infrastructure
=========================================================
Use standard, industry-recommended hardening configuration templates for application infrastructure components. This includes underlying servers, databases, and web servers, and applies to cloud containers, Platform as a Service (PaaS) components, and SaaS components. Do not allow in-house developed software to weaken configuration hardening.

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
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process
* Safeguard 4.2: Establish and Maintain a Secure Configuration Process for Network Infrastructure

Inputs
-----------
#. :code:`GV1`: Enterprise Asset Inventory
#. :code:`GV37`: Network infrastructure configuration standards


Operations
----------
#. Use Input 1 :code:`GV1` to identify and enumerate application infrastructure components :code:`GV50` (M1)
#. For each infastructure component identified in Operation 1, check configurations using Input 2 :code:`GV37` and determine if they meet industry recommended hardening configuraion standards
	#. Identify and enumerate infrastructure components that meet industry standards (M2)
	#. Identify and enumerate infrastructure components that do not meet industry standards (M3)

Measures
--------
* M1 = Count of application infrastructure components
* M2 = Count of components that meet industry standards
* M3 = Count of components that do not meet industry standards

Metrics
-------

Compliance
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of application infrastructure components that meet
	    | industry configuration standards
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
