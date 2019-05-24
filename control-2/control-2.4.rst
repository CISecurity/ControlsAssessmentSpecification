2.4: Track Software Inventory Information
=========================================================
The software inventory system should track the name, version, publisher, and install date for all software, including operating systems authorized by the organization.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Identify
	  - 2, 3

Status
------
Draft

Assumptions
-----------
* Need to define what "weight" is in this context

Measures
--------
* w(i) = weight of software i
* d(i) = tracked information for software i is detailed (1) or not detailed (0); "detailed" if and only if all specified information is present for software i.
* n = # of software for a specific machine

Metrics
-------

Inventory Quality
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - What percentage of the software inventory tracks appropriate information about the software?
	* - **Answer**
	  - A percentage value, between 0 and 100%, indicating the quality of information tracked in an organization's software inventory.
	* - **Calculation**
	  - :code:`((SUM from i to n of (w(i) * d(i))) / n) * 100`

.. history
.. authors
.. license