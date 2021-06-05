F = [1.63706579e-07, -3.96912267e-07, -3.27074941e-03;
    3.36171365e-06,  1.50871730e-06, -6.26674935e-02;
    1.45926029e-03,  6.12286740e-02,  1.00000000e+00];

x1 = [107, 151, 1];
x2 = [17, 166, 1];

K1 = [692.781, 0, 287.833;
    0, 693.371, 238.478;
    0, 0, 1];
      

K2 = [696.816, 0, 331.137;
    0, 698.445, 260.819;
    0, 0, 1];

E = transpose(K1)*F*K2;

[U,S,V] = svd(E);

diag_110 = [1 0 0; 0 1 0; 0 0 0];
newE = U*diag_110*transpose(V);
[U,S,V] = svd(newE); %Perform second decompose to get S=diag(1,1,0)

W = [0 -1 0; 1 0 0; 0 0 1];

R1 = U*W*transpose(V);
R2 = U*transpose(W)*transpose(V);
t1 = U(:,3); %norm = 1
t2 = -U(:,3); %norm = 1

R1axang = rotm2axang(R1)
R2axang = rotm2axang(R2)