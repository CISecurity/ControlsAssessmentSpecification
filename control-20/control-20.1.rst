20.1: Establish a Penetration Testing Program
=========================================================
Establish a program for penetration tests that includes a full scope of blended attacks, such as wireless, client-based, and web application attacks.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - N/A
	* - N/A
	  - 2, 3

Status
------
Draft

Dependencies
------------
* None

Inputs
-----------
#. A Penetration Testing Program document

Operations
----------
#. Determine whether the Penetration Testing Program document exists. If the document exists, set M1 equal to 1. If it does not exist, set M1 equal to 0 and skip the remaining operations.
#. Manually review the Penetration Testing Program document to determine if it addresses a full scope of blended attacks (including wireless, client-based, and web application). If the document adequately addresses a full scope of attacks, set M2 equal to 1. If it does not, set M2 equal to 0.

Measures
--------
* M1 = Boolean value indicating if the Penetration Testing Program document exists; 1 if it exists, 0 otherwise
* M2 = Boolean value indicating if the Penetration Testing Program document adequately addresses a full scope of attacks; 1 if it does, 0 otherwise

Metrics
-------

.. list-table::

	* - **Metric**
	  - | Does a penetration testing program document exist and adequately address a full scope
	    | of attacks?
	* - **Calculation**
	  - :code:`	M1 AND M2`

.. history
.. authors
.. license