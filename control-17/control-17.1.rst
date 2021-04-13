17.1: Designate Personnel to Manage Incident Handling
===================================
Designate one key person, and at least one backup, who will manage the enterprise’s incident handling process. Management personnel are responsible for the coordination and documentation of incident response and recovery efforts and can consist of employees internal to the enterprise, third-party vendors, or a hybrid approach. If using a third-party vendor, designate at least one person internal to the enterprise to oversee any third-party work. Review annually, or when significant enterprise changes occur that could impact this Safeguard.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - Respond
	  - 1, 2, 3

Dependencies
------------
* None

Inputs
-----------
#. :code:`GV51`: Enterprise Incident Response Documentation
#. Date of last update or review of the documentation

Operations
----------
#. Determine whether the enterprise documents designated personnel to manage incident handling by reviewing Input 1 :code:`GV51`. Input 1 can be an incident response plan or other documentation.
	#. If documentation designating personnel exists, M1 = 1
	#. If documentation designating personnel does not exist, M1 = 0
#. Determine whether the documentation, at a minimum, outlines the following components: primary personnel, backup personnel, roles and responsibilities of each
	#. For each component included, assign a value of 1. Sum the values. (M2)
#. Compare Input 2 to current date and capture timeframe in months (M3)

Measures
--------
* M1 = Output of Operation 1
* M2 = Count of components included for designated personnel documentation
* M3 = Timeframe since last update or review of documentation in months

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
* If M3 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Completeness
^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of components included in documentation for 
	    | designated incident handling personnel 
	* - **Calculation**
	  - :code:`M2 / 3`

.. history
.. authors
.. license
