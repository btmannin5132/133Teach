function out1 = functionTest(a,b,c)

    x = -5:c;
    y = a.*(x.^2) + b;

    out1 = 2.5*a + 8*b + 4*c;

    plot(x,y);

end