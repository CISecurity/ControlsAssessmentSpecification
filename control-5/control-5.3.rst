5.3: Securely Store Master Images
=========================================================
Store the master images and templates on securely configured servers, validated with integrity monitoring tools, to ensure that only authorized changes to the images are possible.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 2, 3

Status
------
In Development

Inputs
------
#. A "securely configured server" assumes the application of numerous subcontrols governing deployment of secure configuration settings, proper administrative access, and network isolation.

Operations
----------
#. 

Measures
--------
* M1 = # of validated images
* M2 = # of total images

Metrics
-------

Validated Image Ratio
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | Determine the percentage of total images which are valid according to integrity
	    | monitoring tools.
	* - **Answer**
	  - | The calculation will yield a percentage, from 0 to 100, indicating the ratio of
	    | total images to those images deemed valid.
	* - **Calculation**
	  - :code:`(M1/M2) * 100`

.. history
.. authors
.. license