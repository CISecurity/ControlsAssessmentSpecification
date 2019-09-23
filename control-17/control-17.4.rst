17.4: Update Awareness Content Frequently
=========================================================
Ensure that the organization’s security awareness program is updated frequently (at least annually) to address new technologies, threats, standards, and business requirements.

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
* TBD

Inputs
-----------
#. Date the organization's security awareness program was last updated
#. Maximum time allowed between updates to the organization's security awareness program

Operations
----------
#. Verify that the maximum time allowed between updates to the security awareness program (Input 2) is one year or less and set M1 accordingly.
#. Check the date that the security awareness program was last updated (Input 1) to make sure that it occurred within the required time frame (Input 2) and set M2 accordingly.

Measures
--------
* M1 = 1 if maximum time allowed between security awareness program updates is one year or less, 0 if greater than one year
* M2 = 1 if the last update to the security awareness program was within the required time frame, 0 otherwise

Metrics
-------

Update Timeliness
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Is the organization's security awareness program updated within acceptable time frame?
	* - **Calculation**
	  - :code:`M1 and M2`

.. history
.. authors
.. license