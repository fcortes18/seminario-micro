% ---------------- Red neuronal perceptron ------------%

clear all; close all; clc;

N = 100; % Epocas
Q = 4; % Dimensiones de las entradas

p0 = [1 1 1 1]; % Patron de bias

p = [0 0 1 1
    0 1 0 1
    ];

y = [0 0 0 1; % Salidas deseadas % compuerta AND
     0 1 1 1]; % Salidas deseadas % compuerta OR

alfa = 0.1;

w = 2*rand(2,2) - 1; % Valor random de una fila, 2 columnas
b = 2*rand(2, 1) - 1;

pr = -0.5:0.01:2;

H1 = plot(pr, -b(1)/w(1,2) - w(1,1)/w(1,2)*pr);
H2 = plot(pr, -b(2)/w(2,2) - w(2,1)/w(2,2)*pr);

% ----------------- Proceso de entrenamiento ---------------%

for Epocas=1:N
    for q = 1:Q
        net = w * p(:, q) + b;

        a = hardlim(net);
        e(:,q) = y(:, q) - a;
        w = w + alfa*e(:, q) * p(:, q)';
        b = b + alfa*e(:, q);
    end

% --------------- Grafica de la frontera de decision -------%
delete(H1)
delete(H2)

plot(p(1,1), p(2,1), 'bo')
grid on, hold on

plot(p(1,2), p(2,2), 'bo')
plot(p(1,3), p(2,3), 'bo')
plot(p(1,4), p(2,4), 'bo')

H1 = plot(pr, -b(1)/w(1,2) - w(1,1)/w(1,2)*pr);
H2 = plot(pr, -b(2)/w(2,2) - w(2,1)/w(2,2)*pr);
pause(0.4);

end
