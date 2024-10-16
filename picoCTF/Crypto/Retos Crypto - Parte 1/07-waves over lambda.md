## Objetivo
We made a lot of substitutions to encrypt this. Can you decrypt it? Connect with `nc jupiter.challenges.picoctf.org 13758`.

## Solución
Utilizo el comando `nc jupiter.challenges.picoctf.org 13758` y nos da lo siguiente
```text
-------------------------------------------------------------------------------
gudnwsob kzwz fb xuqw ypsn - ywzrqzdgx_fb_g_uczw_pseavs_vdcoywosxq
-------------------------------------------------------------------------------
kscfdn ksv buez ofez so ex vfbmubsp lkzd fd pudvud, f ksv cfbfozv okz awfofbk eqbzqe, sdv esvz bzswgk seudn okz auuib sdv esmb fd okz pfawswx wznswvfdn owsdbxpcsdfs; fo ksv bowqgi ez okso buez yuwzidulpzvnz uy okz guqdowx guqpv kswvpx ysfp ou kscz buez femuwosdgz fd vzspfdn lfok s duapzesd uy okso guqdowx. f yfdv okso okz vfbowfgo kz dsezv fb fd okz zjowzez zsbo uy okz guqdowx, tqbo ud okz auwvzwb uy okwzz bosozb, owsdbxpcsdfs, eupvscfs sdv aqiucfds, fd okz efvbo uy okz gswmsokfsd euqdosfdb; udz uy okz lfpvzbo sdv pzsbo iduld muwofudb uy zqwumz. f lsb duo sapz ou pfnko ud sdx esm uw luwi nfcfdn okz zjsgo pugspfox uy okz gsbopz vwsgqps, sb okzwz swz du esmb uy okfb guqdowx sb xzo ou guemswz lfok uqw uld uwvdsdgz bqwczx esmb; aqo f yuqdv okso afbowfoh, okz mubo ould dsezv ax guqdo vwsgqps, fb s ysfwpx lzpp-iduld mpsgz. f bkspp zdozw kzwz buez uy ex duozb, sb okzx esx wzywzbk ex ezeuwx lkzd f ospi uczw ex owsczpb lfok efds.

```

Intentaremos resolverlo por sustitución apoyandonos de la web guballa, la cual nos regresa el siguiente código:
```text
-------------------------------------------------------------------------------
congrats here is your flag - frequency_is_c_over_lambda_dnvtfrtayu
-------------------------------------------------------------------------------
having had some time at my disposal when in london, i had visited the british museum, and made search among the books and maps in the library regarding transylvania; it had struck me that some foreknowledge of the country could hardly fail to have some importance in dealing with a nobleman of that country. i find that the district he named is in the extreme east of the country, just on the borders of three states, transylvania, moldavia and bukovina, in the midst of the carpathian mountains; one of the wildest and least known portions of europe. i was not able to light on any map or work giving the exact locality of the castle dracula, as there are no maps of this country as yet to compare with our own ordnance survey maps; but i found that bistritz, the post town named by count dracula, is a fairly well-known place. i shall enter here some of my notes, as they may refresh my memory when i talk over my travels with mina.

```

en donde ya nos da la flag directamente:
frequency_is_c_over_lambda_dnvtfrtayu

## Notas Adicionales


## Referencias
https://www.guballa.de/substitution-solver