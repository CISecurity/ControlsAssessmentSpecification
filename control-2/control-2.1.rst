2.1: Maintain Inventory of Authorized Software
==============================================
Maintain an up-to-date list of all authorized software that is required in the enterprise for any business purpose on any business system.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Identify
	  - 1, 2, 3

Status
------
Draft

Inputs
------
#. The authorized software list (containing a timestamp indicating both last updated and last verified values).
#. An organizationally defined acceptable timeframe for "up-to-date"

Operations
----------
#. Test for the presence of the list; A TRUE/FALSE value (M1)
#. (Optional) If specific attributes of the software are deemed required, test for those (vendor, product name, version, business case, etc.)
#. Compare the timestamp of Input 1 against the current date to determine if the most recent update/verification is within the timeframe specified by Input 2; A TRUE/FALSE value (M2).

Measures
--------
* M1 = TRUE if authorized software list is present and in the proper format, FALSE otherwise
* M2 = TRUE if the most recent update/verification is within the "up-to-date" threshold; FALSE otherwise


Metrics
-------

Update Quality
^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | Is the authorized software list present and up-to-date?
	* - **Answer**
	  - | This metric is a boolean indicator describing that the authorized software list 
	    | is both present and up-to-date within a certain time threshold.
	* - **Calculation**
	  - :code:`M1 AND M2`

.. history
.. authors
.. license