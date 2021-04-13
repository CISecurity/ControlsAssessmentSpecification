16.14: Conduct Threat Modeling
=========================================================
Conduct threat modeling. Threat modeling is the process of identifying and addressing application security design flaws within a design, before code is created. It is conducted through specially trained individuals who evaluate the application design and gauge security risks for each entry point and access level. The goal is to map out the application, architecture, and infrastructure in a structured way to understand its weaknesses.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 3

Dependencies
------------
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
-----------
#. :code:`GV5`: Authorized Software Inventory
#. Threat Modeling Process for the enterprise 

Operations
----------
#. Determine whether Input 2 exists for the enterprise
	#. If the process exists, M1 = 1
	#. If the process does not exist, M1 = 0
#. Use Input 1 :code:`GV5` to identify and enumerate all in-house developed applications (M2)
#. For each application identified in Operation 2, determine whether the threat modeling process was followed
	#. Identify and enumerate applications for which threat modeling was conducted (M3)
	#. Identify and enumerate applications for which threat modeling was not conducted (M4)

Measures
--------
* M1 = Output of Operation 1
* M2 = Count of in-house developed applications
* M3 = Count of in-house developed applications that underwent threat modeling
* M4 = Count of in-house developed applications that did not undergo threat modeling

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.

Compliance
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of in-house developed applications that 
	    | underwent threat modeling
	* - **Calculation**
	  - :code:`M3 / M2`


.. history
.. authors
.. license
