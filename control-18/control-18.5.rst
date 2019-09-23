18.5: Use only Standardized and Extensively Reviewed Encryption Algorithms
==========================================================================
Use only standardized, currently accepted, and extensively reviewed encryption algorithms.

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
#. List of encryption algorithms used by the organization
#. Authoritative source that identifies which encryption algorithms are standardized, currently accepted, and extensively reviewed.

Operations
----------
#. For each encryption algorithm in Input 1, check Input 2 to see if that encryption algorithm is standardized, currently accepted, and extensively reviewed.
	#. Create a list of the encryption algorithms that meet all of these criteria (M1)
	#. Create a list of the encryption algorithms that do not meet all of these criteria (M2).

Measures
--------
* M1 = List of encryption algorithms used by the organization that are standardized, currently accepted, and extensively reviewed (compliant list)
* M2 = List of encryption algorithms used by the organization that do not meet these criteria (non-compliant list)
* M3 = Count of encryption algorithms used by the organization that are standardized, currently accepted, and extensively reviewed (count of M1)
* M4 = Total count of encryption algorithms used by the organization (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of encryption algorithms used by the organization that are standardized, 
	    | currently accepted, and extensively reviewed
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license