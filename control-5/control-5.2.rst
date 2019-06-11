5.2: Maintain Secure Images
=========================================================
Maintain secure images or templates for all systems in the enterprise based on the organization’s approved configuration standards.  Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 2, 3

Status
------
In Development

Inputs
------
#. 

Assumptions
^^^^^^^^^^^
* Documented, standard security configuration standards exist per control 5.1
* Images/templates for a given system could encompass one-to-many security configuration standards, i.e. an operating system configuration standard plus a browser configuration standard

Operations
----------
#. 

Measures
--------
* M1 = # of systems with image taken
* M2 = # of total system
* M3 = # of system with approved configuration

Metrics
-------

Coverage (Quality Measure)
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - Determine the percentage of total systems from which an image has been taken.
	* - **Answer**
	  - | The calculation will yield a percentage, from 0 to 100, indicating the ratio of
	    | total systems to those with images taken.
	* - **Calculation**
	  - :code:`(M1/M2) * 100`

Configuration Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | Determine the percentage of total systems to which approved configurations have
	    | been applied.
	* - **Answer**
	  - | The calculation will yield a percentage, from 0 to 100, indicating the ratio of total
	    | systems to those with approved configurations applied.
	* - **Calculation**
	  - :code:`(M3/M2) * 100`

.. history
.. authors
.. license