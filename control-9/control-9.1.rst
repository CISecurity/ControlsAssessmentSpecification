9.1: Ensure Use of Only Fully Supported Browsers and Email Clients
=======================================================================
Ensure only fully supported browsers and email clients are allowed to execute in the enterprise, only using the latest version of browsers and email clients provided through the vendor.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
------
#. :code:`GV5`: Authorized software inventory
#. Authoritative source of information indicating supported/unsupported details by product.

Operations
----------
#. Use :code:`GV5` to identify and enumerate web browser and email client software (M1)
#. Compare each software identified in Operation 1 to Input 2
	#. Identify and enumerate software labeled as "supported" that is currently supported (M2)
	#. Identify and enumerate software labeled as "supported" that is currently unsupported (M3)
	#. Identify and enumerate software labeled as "unsupported" that is currently unsupported (M4)
	#. Identify and enumerate software labeled as "unsupported" that is currently supported (M5)

Measures
--------
* M1 = Count of authorized web browser and email client software
* M2 = Count of software labeled as "supported" and currently supported
* M3 = Count of software labeled as "supported" and currently unsupported
* M4 = Count of software labeled as "unsupported" and currently unsupported
* M5 = Count of software labeled as "unsupported" and currently supported

Metrics
-------

Percentage of Unsupported Web Browser/Email Client Software in Use
^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of unsupported web browser and email client software in use
	* - **Calculation**
	  - :code:`(M3 + M4) / M1`


Rate of False Positives
^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of authorized web browser and email client software labeled as 
	  - | "supported" but found to be unsupported.
	* - **Calculation**
	  - :code:`M3 / M1`

Rate of False Negatives
^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of authorized web browser and email client software labeled as 
	  - | "unsupported" but found to be supported.
	* - **Calculation**
	  - :code:`M5 / M1`

.. history
.. authors
.. license
