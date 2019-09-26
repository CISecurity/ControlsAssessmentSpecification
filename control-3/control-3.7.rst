3.7: Utilize a Risk-Rating Process
==================================
Utilize a risk-rating process to prioritize the remediation of discovered vulnerabilities.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Respond
	  - 2, 3

Dependencies
------------
* None

Inputs
------
#. Security program vulnerability management policy

Operations
----------
#. Review vulnerability management policy for risk-rating process description
#. Review risk-rating process description to ensure risk-rating is used for prioritization

Measures
--------
* M1 (Boolean) = Risk-rating process exists or does not exist
* M2 (Boolean) = Risk-rating process is used for prioritization

Metrics
-------

Risk-Rating Process
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Manual review: Does a risk-rating process exist and is it utilized for prioritization?
	* - **Calculation**
	  - :code:`M1 AND M2`

.. history
.. authors
.. license
