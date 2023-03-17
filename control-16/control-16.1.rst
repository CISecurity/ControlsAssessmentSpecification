16.1: Establish and Maintain a Secure Application Development Process
=========================================================
Establish and maintain a secure application development process. In the process, address such items as: secure application design standards, secure coding practices, developer training, vulnerability management, security of third-party code, and application security testing procedures. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard.

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
* None

Inputs
-----------
#. :code:`GV49`: Secure Application Development Process
#. Date of last update or review of the secure application development process

Operations
----------
#. Determine whether Input 1 exists within the enterprise
	#. If Input 1 exists, M1 = 1
	#. If Input 1 does not exist, M1 = 0
#. Review Input 1 and dermine whether it includes, at a minimum, the following components: secure application design standards, secure coding practices, developer training, vulnerability management, security of third-party code, and application security testing procedures
	#. For each component included in the process, assign a value of 1.  Sum all values. (M2)
#. Compare Input 2 to current date and capture timeframe in months (M3)


Measures
--------
* M1 = Output of Operation 1
* M2 = Count of components included in the process
* M3 = Timeframe in months since last review or update

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
* If M3 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Completeness
^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percent of components included in the secure application 
	  - | development process
	* - **Calculation**
	  - :code:`M2 / 6`


.. history
.. authors
.. license
