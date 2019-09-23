18.1: Establish Secure Coding Practices
=========================================================
Establish secure coding practices appropriate to the programming language and development environment being used.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - N/A
	  - 2, 3

Status
------
Draft

Dependencies
------------
* None

Inputs
-----------
#. List of programming languages and development environments that the organization uses for software development
#. The organization's secure coding guides, with each guide tagged with the programming languages and development environments that it covers

Operations
----------
#. For each programming language and development environment in Input 1, check to see if it is covered by at least one secure coding guide in Input 2.
	#. Create a list of the programming languages and development environments that are covered by secure coding guide (M1)
	#. Create a list of programming languages and development environments that are not covered by at least one secure coding guide (M2)
#. (Optional) Manually review the secure coding guides to ensure that they cover all the needed aspects of secure coding for the programming languages and development environments in question, noting any topics or sections that need improvement (M3).

Measures
--------
* M1 = List of programming languages and development environments covered by at least one secure coding guide (compliant list)
* M2 = List of programming languages and development environments not covered by at least one secure coding guide (non-compliant list)
* M3 = (Optional) From optional manual review, list/description of topics or sections that need to be improved
* M4 = Count of programming languages and development environments covered by at least one secure coding guide (count of M1)
* M5 = Total count of programming languages and development environments that the organization uses for software development (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of programming languages and development environments covered by a secure
	    | coding guide
	* - **Calculation**
	  - :code:`M4 / M5`

.. history
.. authors
.. license