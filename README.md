I use [Anaconda](https://www.anaconda.com/) as my Python installation.

Start by setting up a conda environment (this doesn't work on the NREL network):

    conda env create -f environment.yml
    
And activate it:

    conda activate rex-test
    
You'll need to [register for an NREL API key](https://developer.nrel.gov/signup/), and configure hsds (as described [here](https://github.com/openEDI/documentation/blob/master/US_Wave.md)).

Now you should be able to run the script.
