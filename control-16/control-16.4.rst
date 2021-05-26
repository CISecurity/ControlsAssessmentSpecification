16.4: Establish and Manage an Inventory of Third-Party Software Components
=========================================================
Establish and manage an updated inventory of third-party components used in development, often referred to as a “bill of materials,” as well as components slated for future use. This inventory is to include any risks that each third-party component could pose. Evaluate the list at least monthly to identify any changes or updates to these components, and validate that the component is still supported. 

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
#. :code:`GV47`: Inventory of Third-Party Software Components 
#. Date of last review or update of the inventory

Operations
----------
#. Determine whether Input 1 exists within the enterprise
	#. If Input 1 exists, M1 = 1
	#. If Input 1 does not exist, M1 = 0
#. Use Input 1 and dermine whether each software component listed includes, at a minimum, the following information: risk associated with components, whether component is supported 
	#. Identify and enumerate software components with complete information (M3)
	#. Identify and enumerate software components with missing information (M4) 
#. Compare date of Input 2 to current date and capture timeframe in days (M5)


Measures
--------
* M1 = Output of Operation 1
* M2 = Count of Input 1
* M3 = Count of software components with complete information
* M4 = Count of software components with missing information
* M5 = Timeframe since last review or update of the inventory 

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
* If M5 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Completeness of Inventory
^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percent of components included in the secure application 
	  - | development process
	* - **Calculation**
	  - :code:`M3 / M2`


.. history
.. authors
.. license
