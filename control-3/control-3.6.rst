3.6: Compare Back-to-Back Vulnerability Scans
=============================================
Regularly compare the results from consecutive vulnerability scans to verify that vulnerabilities have been remediated in a timely manner.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Respond
	  - 2, 3

Status
------
In Development

Inputs
------
#. 

Operations
----------
#. 

Measures
--------
We need to know how many of the discovered vulnerabilities been fixed/patched and how soon these are fixed.

* V : Number of all discovered vulnerabilities in the last scan
* v_i: 1 if a vulnerability is patched, otherwise 0
* p_i: patch time for vulnerability i
* t_i: discovery time of vulnerability i

Metrics
-------

Patching Quality
^^^^^^^^^^^^^^^^

.. list-table::

	* - **Question**
	  - How well are vulnerabilities covered based on time and coverage?
	* - **Answer**
	  - TBD
	* - **Calculation**
	  - :code:`(\sum v_i*(1-p_i - t_i)) / V`

.. history
.. authors
.. license
