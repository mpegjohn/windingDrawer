
settings.render = 16;
defaultpen(fontsize(10pt));
unitsize(1cm);

currentpen = linewidth(0.5);

draw((0, 0) -- (5, 0), arrow=Arrow);
draw((5, 0) -- (5, 0.5));
draw((5, 0.5) -- (0, 0.5), arrow=Arrow);

draw((0, 0.25) -- (5, 0.25), currentpen + dashed);

