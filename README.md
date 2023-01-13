# README #

# What is this repository for? #

Extension of interIsoFoam and geometricVoF to include porous media
-------------------------------------------------------------------

Momentum equation formulation based on:
"Investigations on the porous media equations and resistance coefficients for 
coastal structures", Jensen et al. 2014, DOI: 10.1016/j.coastaleng.2013.11.004

Compared to original UEqn.H we the modified equation is divided through by the
porosity, rhoPhi is replaced by rhoPhi/fvc::interpolate(porosity) in the 
convective term (see alphaEqen.H) and the extended Darcy-Forchheimer forces 
(including added mass) are added to the equation.

The modifications of the UEqn.H has been done in such a way as to make it 
straight forward to place the modifications in a 

The snGrad(p_rgh), gfh*sngrad(rho) etc. are not divided by porosity and the 
pEqn.H is left unaltered compared to the interIsoFoam file.

The porosity and the coefficients going into the Darcy-Forchheimer forces are
currently defined as fields which are read in the createFields.H file to allow
several different porous regions potentially with spatially varying values.
To avoid writing the field out in every time folder they are currently read as
NO_WRITE. This means that a restart from a later time will not work. 

As for the isoAdvection the class has been extended to take the porosity as an
argument in its constructor. Basically the velocity field relevant for interface
advection is U/porosity since this is the Lagragian velocity of fluid particles.
Also the update of alpha must take into account that only a fraction of the cell
volumes given by the porosity are available for the fluid flow. Thus alpha = 1
corresponds to cellVolume*porosity m^3 water/heavy fluid in the cell.


Both the Courant number (CounrantNo.H) and the alpha Courant number 
(alphaCouranNo.H) calucaltion are modified to account for the faster fluid
particle velocity in the porous material.

Also the calcualtion of the total Phase-1 volume in alphaEqn.H is changed to 
account for the porous material.

Compatibility with OpenFOAM-v2012

### How do I get set up? ###

* Installation: ./Allwmake (to $FOAM_USER_*BIN)
* Tutorials: ./Allrun
    * discInConstantPorousFlow (pure advection test case)
    * porousDamBreak (full solver test with experimental data for comparison)
* Dependencies: OpenFOAM-v2012 and an installation of python3 is required to fully run the post processing. 

### Who do I talk to? ###

* Konstantinos Missios (missios@ruc.dk or missios.konstantinos@gmail.com)
* Niels Gjoel Jacobsen (coastalof@gmail.com)
* Johan Roenby (johan@ruc.dk)


