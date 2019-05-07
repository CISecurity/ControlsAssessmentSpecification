CIS Control 5: Secure Configuration for Hardware and Software on Mobile Devices, Laptops, Workstations and Servers
==================================================================================================================

Establish, implement, and actively manage (track, report on, correct) the security configuration
of mobile devices, laptops, servers, and workstations using a rigorous configuration
management and change control process in order to prevent attackers from exploiting
vulnerable services and settings.

**Why is this CIS Control Critical?**

As delivered by manufacturers and resellers, the default configurations for operating systems
and applications are normally geared towards ease-of-deployment and ease-of-use – not
security. Basic controls, open services and ports, default accounts or passwords, older (vulnerable)
protocols, and pre-installation of unneeded software can be exploitable in their default state.

Developing configuration settings with good security properties is a complex task beyond the
ability of individual users, requiring analysis of potentially hundreds or thousands of options
in order to make good choices (the Procedures and Tools section below provides resources for
secure configurations). Even if a strong initial configuration is developed and installed, it must be
continually managed to avoid security “decay” as software is updated or patched, new security
vulnerabilities are reported, and configurations are “tweaked” to allow the installation of new
software or support new operational requirements. If not, attackers will find opportunities to
exploit both network accessible services and client software.

.. toctree::
   :maxdepth: 1
   :name: toc-control-5

   5.1: Establish Secure Configurations <control-5.1>
   5.2: Maintain Secure Images <control-5.2>
   5.3: Securely Store Master Images <control-5.3>
   5.4: Deploy System Configuration Management Tools <control-5.4>
   5.5: Implement Automated Configuration Monitoring Systems <control-5.5>
   
.. history
.. authors
.. license