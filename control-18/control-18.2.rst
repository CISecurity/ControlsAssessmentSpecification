18.2: Ensure That Explicit Error Checking Is Performed for All In-House Developed Software
==========================================================================================
For in-house developed software, ensure that explicit error checking is performed and documented for all input, including for size, data type, and acceptable ranges or formats.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - N/A
	  - 2, 3

Dependencies
------------
* Sub-control 18.1: Establish Secure Coding Practices

Inputs
-----------
#. List of in-house developed software
#. Documentation for in-house developed software
#. Code for in-house developed software (the software itself)

Operations
----------
#. For each piece of in-house developed software in Input 1, identify all of the inputs for that software and associated properties of those inputs including size, data type, and acceptable ranges or formats (M1).
#. For each piece of in-house developed software, review the associated documentation provided in Input 2 to ensure that each of the inputs and associated properties identified in M1 are properly documented.
	#. Create a list of the software for which all inputs and associated properties are properly documented (M2)
	#. Create a list of software for which at least one input and/or associated properties is not properly documented noting which inputs/properties are insufficiently documented (M3).
#. For each piece of in-house developed software, review the associated code provided in Input 3 to ensure that explicit error checking is performed for each of the inputs identified in M1 to ensure that those inputs are of acceptable sizes, data types, formats, and within the proper ranges.
	#. Create a list of the software for which all inputs have explicit error checking for the identified properties (M4)
	#. Create a list of software for which at least one of the inputs/properties is not properly checked (M5) noting the improperly checked inputs/properties and why they are deficient.
#. Compare M2 and M4 to generate the count of which pieces of in-house developed software are in both lists (M6).

Measures
--------
* M1 = List of all inputs for each piece of in-house developed software and associated properties of those inputs including size, data type, and acceptable ranges or formats
* M2 = List of the software for which all inputs and associated properties are properly documented (compliant documentation list)
* M3 = List of software for which at least one input and/or associated properties is not properly documented (non-compliant documentation list)
* M4 = List of the software for which all inputs have explicit error checking for the identified properties (compliant code list)
* M5 = List of software for which at least one of the inputs/properties is not properly checked (non-compliant code list)
* M6 = Count of compliant software (count of intersection of M2 and M4)
* M7 = Total count of in-house developed software (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of software that contains proper error checking of inputs and is properly
	    | documented
	* - **Calculation**
	  - :code:`M6 / M7`

.. history
.. authors
.. license
