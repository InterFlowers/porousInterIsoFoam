    MRF.correctBoundaryVelocity(U);


    // Original UEqn but with rhoPhi divided by face interpolated porosity
    // (see alphaEqn.H)
    fvVectorMatrix UEqn
    (
        fvm::ddt(rho, U) + fvm::div(rhoPhi, U)
      + MRF.DDt(rho, U)
      + turbulence->divDevRhoReff(rho, U)
     ==
        fvOptions(rho, U)
    );

    // Including porosity effects in UEqn
    // This could be put into an fvOption
    {
        // Generating Darcy-Forchheimer coefficient: F = rho*U*(a + b*|U|)
        // Shoud it be mu or muEff in the equation below?
        volScalarField a
        (
            alpha*sqr(1.0 - porosity)/pow3(porosity)*mixture.mu()/rho/sqr(d50)
        );
        volScalarField b
        (
            beta*(1.0 + pos(KC)*7.5/KC)*(1.0 - porosity)/pow3(porosity)/d50
        );
        // Generating added mass force coefficient: 
        volScalarField Cm
        (
            gamma_p*(1 - porosity)/porosity
        );

        // Dividing both matrix entries and source term by porosity
        UEqn *= (1.0/porosity);
        // Adding Darcy-Forchheimer term as implicit source term
        UEqn += fvm::Sp(rho*(a + b*mag(U)), U);
        // Expplicit variant also works:
//        UEqn += rho*(a + b*mag(U))*U;
        UEqn += Cm/porosity*fvm::ddt(rho, U);
        UEqn += Cm/porosity*MRF.DDt(rho, U);
    }

    UEqn.relax();

    fvOptions.constrain(UEqn);

    if (pimple.momentumPredictor())
    {
        solve
        (
            UEqn
         ==
            fvc::reconstruct
            (
                (
                    mixture.surfaceTensionForce()
                  - ghf*fvc::snGrad(rho)
                  - fvc::snGrad(p_rgh)
                ) * mesh.magSf()
            )
        );

        fvOptions.correct(U);
    }
