% ---------------- Red neuronal perceptron ------------%

clear all; close all; clc;

N = 10000; % Epocas
Q = 4; % Dimensiones de las entradas


p0 = [1 1 1 1]; % Patron de bias
p1 = [0 0 1 1]; % Patron uno de entrada
p2 = [0 1 0 1]; % Patron dos de entrada

% y = [0 0 0 1; % Salidas deseadas % compuerta AND
%     0 1 1 1]; % Salidas deseadas % compuerta OR

%y = [0 0 0 1]'; % Salidas deseadas % compuerta AND

y = [-1 1 1 1]'; % Salidas deseadas % compuerta OR


alfa = 0.1;

w = 2*rand(1,2) - 1; % Valor random de una fila, 2 columnas
b = 2*rand - 1;

pr = -0.5:0.01:2;

H = plot(pr, -b/w(2) - w(1)/w(2)*pr);

% ----------------- Proceso de entrenamiento ---------------%

for Epocas=1:N
    for q = 1:Q
        a(q) = hardlims(w*[p1(q) p2(q)]' + b*p0(q));
        e(q) = y(q) - a(q);
        w(1) = w(1) + alfa * (e(q))*p1(q);
        w(2) = w(2) + alfa * (e(q))*p2(q);
        b = b + e(q);
    end

% --------------- Grafica de la frontera de decision -------%

delete(H)
plot(p1(1), p2(1), 'bo')
grid on, hold on

plot(p1(2), p2(2), 'bo')
plot(p1(3), p2(3), 'bo')
plot(p1(4), p2(4), 'bo')

H = plot(pr, -b/w(2) - w(1)/w(2)*pr);
pause(0.4);


end

