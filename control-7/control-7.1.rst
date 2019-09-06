7.1: Ensure Use of Only Fully Supported Browsers and Email Clients
==================================================================
Ensure that only fully supported web browsers and email clients are allowed to execute in the organization, ideally only using the latest version of the browsers and email clients provided by the vendor.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 1, 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 2.1: Maintain Inventory of Authorized Software

Inputs
------
#. From the authorized software list, the inventory of web browser and email client software with a notation of "supported" or "unsupported" for each entry.
#. Access to an authoritative source of information indicating supported/unsupported details by product.

Operations
----------
#. For each entry in Input 1, perform a lookup in Input 2 to verify.
#. For each entry in Input 1 labeled "supported", perform a lookup in Input 2.  From these lookups, note the list of authorized software labeled "supported" but are actually not supported based on the authoritative source lookup.
#. For each entry in Input 1 labeled "unsupported", perform a lookup in Input 2.  From these lookups, note the list of authorized software labeled "unsupported" but are actually supported based on the authoritative source lookup.

Measures
--------
* M1 = # of items in Input 1 that are unsupported (combination of Operation 1 results and those initially marked as unsupported in Input 1)
* M2 = Total # of authorized web browser/email client software (from Input 1)
* M3 = The number of items from Input 1 labeled "supported" but are actually not supported (from Operation 2)
* M4 = The number of items from Input 1 labeled "unsupported" but are actually supported (from Operation 3)

Metrics
-------

Percentage of Unsupported Web Browser/Email Client Software in Use
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The calculation of this metric is determined by the ratio of unsupported web
	    | browser/email client software to the total authorized web browser/email client software
	    | in use.
	* - **Calculation**
	  - :code:`(M2 - M1) / M2`

Rate of False Positives
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The calculation of this metric is determined by the ratio of web browser/email client
	    | software labeled "supported" but found to be unsupported, to the total authorized web
	    | browser/email client software in use.
	* - **Calculation**
	  - :code:`(M2 - M3) / M2`

Rate of False Negatives
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The calculation of this metric is determined by the ratio of web browser/email client
	    | software labeled "unsupported" but found to be supported, to the total authorized web
	    | browser/email client software in use.
	* - **Calculation**
	  - :code:`(M2 - M4) / M2`
.. history
.. authors
.. license