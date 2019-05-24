2.5: Integrate Software and Hardware Asset Inventories
=========================================================
The software inventory system should be tied into the hardware asset inventory so all devices and associated software are tracked from a single location.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Identify
	  - 3

Status
------
Draft

Assumptions
-----------
* Subcontrol 1.1 has been implemented, allowing for a queryable hardware inventory
* Subcontrol 2.1 has been implemented, allowing for a queryable software inventory
* If there are two separate systems for hardware and software inventory, then there needs to be a link, or relationship, between the two. Then, we need: 1) software inventory, 2) hardware inventory, and a reconciliation between them.

Measures
--------
* M = list of s/w reported by subcontrol 2.1
* N = list of h/w reported by subcontrol 1.1
* M1 = # of s/w without hardware association reported by PUT
* M2 = # of h/w without software association reported by PUT
* untracked s/w: s/w inventory that has no associated h/w

Metrics
-------

Hardware Association Ratio
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - 
	* - **Answer**
	  - The result of the calculation is the percentage of hardware assets in the hardware inventory with associated software in the software inventory.
	* - **Calculation**
	  - :code:`((N - M2) / N) * 100`

Software Association Ratio
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - 
	* - **Answer**
	  - The result of the calculation is the percentage of software assets in the software inventory with associated hardware in the hardware inventory.
	* - **Calculation**
	  - :code:`((M - M1) / M) * 100`

.. history
.. authors
.. license