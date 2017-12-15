settings.outformat = "pdf";
unitsize(1cm);
defaultpen(fontsize(10pt));
currentpen=linewidth(0.5);
draw((0, 0) -- (5, 0), arrow=Arrow);
draw((5, 0) -- (5, 0.5));
draw((5, 0.5) -- (0, 0.5), arrow=Arrow);
draw((0, 0.5) -- (0, 1.0));
draw((0, 1.0) -- (5, 1.0), arrow=Arrow);
draw((5, 1.0) -- (5, 1.5));
draw((5, 1.5) -- (0, 1.5), arrow=Arrow);
draw((0, 1.5) -- (0, 2.0));
draw((0, 2.0) -- (5, 2.0), arrow=Arrow);
draw((5, 2.0) -- (5, 2.5));
draw((5, 2.5) -- (0, 2.5), arrow=Arrow);
draw((0, 2.5) -- (0, 3.0));
draw((0, 0.25) -- (5, 0.25), currentpen+dashed);
draw((0, 0.75) -- (5, 0.75), currentpen+dashed);
draw((0, 1.25) -- (5, 1.25), currentpen+dashed);
draw((0, 1.75) -- (5, 1.75), currentpen+dashed);
draw((0, 2.25) -- (5, 2.25), currentpen+dashed);