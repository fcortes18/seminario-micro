%% ----------  Adaline -----------------------------------
clear all; close all; clc;

%% ---------------  inicializacon -----------------------------------------
Q=4;        % dimension de las entradas

p0=[1 1 1 1];   % patron de bias
p1=[0 0 1 1];   % patron uno de entrada
p2=[0 1 0 1];   % patron dos de entrada

yd1 = [0 0 0 1]; % AND normal
yd2 = [-1 -1 -1 1]; % AND modificada
yd3 = [0 1 1 1]; % OR normal
yd4 = [-1 1 1 1]; % OR modificada (salen mejor las modificadas

yd = yd2;

R = zeros(3,3);
h = zeros(3,1);

for k=1:Q
    z = [p1(k) p2(k) p0(k)];
    R1 = z'*z;
    R = R + R1;

    h1 = yd(k)*z';
    h = h + h1;
end

Ri = inv(R);
x = (Ri*h);
xm = (1/Q)*x;

plot(p1(1),p2(1),'bo')
grid on, hold on
plot(p1(2),p2(2),'bo')
plot(p1(3),p2(3),'bo')
plot(p1(4),p2(4),'bo')
axis([-0.5 1.5 -0.5 1.5])

pr=-0.5:0.01:2;
H=plot(pr, -xm(3)/xm(2)- xm(1)/xm(2)*pr);
