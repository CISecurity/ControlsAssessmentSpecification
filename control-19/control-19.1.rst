19.1: Document Incident Response Procedures
=========================================================
Ensure that there are written incident response plans that define roles of personnel as well as phases of incident handling/management.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - N/A
	  - 1, 2, 3

Status
------
Draft

Dependencies
------------
* None

Inputs
-----------
#. Incident response plan

Operations
----------
#. Determine whether incident response plan exists (becomes M1)
#. If it exists, then manual review of incident response plan (determine M2 and M3)

Measures
--------
* M1 = A plan exists
* M2 = The plan defines incident response roles
* M3 = The plan defines incident handling/management phases

Metrics
-------

Existence
^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ensure that there are written incident response plans that define roles of personnel
	    | as well as phases of incident handling/management.
	* - **Calculation**
	  - :code:`M1 AND M2 AND M3`

.. history
.. authors
.. license
