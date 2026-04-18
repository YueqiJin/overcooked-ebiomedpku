ucircfull
============

About
-----------

The ucircfull package is a UMI-guided tool for identifying and quantifying circRNAs from UMI-tagged full-length circRNA sequencing (ucircFL-seq) data. It is designed to handle the challenges of low read depth and high sequencing error rates in ucircFL-seq data, and to provide accurate quantification of circRNA abundance.

Pipeline
----------

.. image:: /images/ucircfull.png
   :align: center
   :alt: ucircfull pipeline

Usage overview
----------------

.. code-block:: bash

    Usage: ucircfull [--help] [--version] {circ_call,clust_umi,extract_umi}

    Optional arguments:
       -h, --help    shows help message and exits
       -v, --version prints version information and exits

    Subcommands:
       circ_call     circRNA identification.
       clust_umi     UMI clusting guided consensus generation.
       extract_umi   Extract UMI sequence and identify strand from ucircFL-seq raw fastq

Guide
-----------

.. toctree::
   :maxdepth: 2

   installation
   umi-extraction
   umi-clustering
   circrna-identification

