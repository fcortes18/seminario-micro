clear all; close all; clc;

alfa = 0.01;

P = [0 0 1 1;
     0 1 0 1];

Yd1 = [0 0 0 1]; % and normal
Yd2 = [-1 -1 -1 1]; % and modificada
Yd3 = [-1 1 1 -1]; % XOR

Q = length(P);
n1 = 20; % Numero de neuronas

W1 = 2*rand(n1, 2) - 1;
W2 = 2*rand(1, n1) - 1;
b1 = 2*rand(n1, 1) - 1;
b2 = 2*rand -1;

for epocas = 1:10000
    sum = 0;
    for q = 1:Q
        % propagacion de la entrada hacia la salida
        a1 = tansig(W1*P(:, q) + b1);
        a2(q) = tansig(W2*a1 + b2);

        % retropropagacion de la sensibilidad
        e = Yd3(q) - a2(q);
        s2 = -2 *(1-a2(q)^2)*e;
        s1 = diag(1 - a1.^2)*W2'*s2;

        % actualizacion de los pesos sinapticos y bias
        W1 = W1 - alfa*s1*P(:,q)';
        W2 = W2 - alfa*s2*a1';
        b1 = b1 - alfa*s1;
        b2 = b2 - alfa*s2;

        % sumando el error cuadratico
        sum = e^2 + sum;
    end

    em(epocas) = sum/Q;

end

plot(em) % grafica del error

for q=1:Q
    a(q) = tansig(W2*tansig(W1*P(:,q) + b1) + b2); % feedforward con pesos calculados
end

pt1 = linspace(-2, 2, 100);
pt2 = linspace(-2, 2, 100);

for i=1:length(pt1)
    for j=1:length(pt2)
        z(i,j) = tansig(W2*tansig(W1*[pt1(i);pt2(j)] + b1) + b2);
    end
end

figure, contour(pt1, pt2, z', [0, 0, 0], 'LineWidth', 2), hold on,

plot(P(1, 1), P(2, 1), 'bo')
grid on, hold on

plot(P(1, 2), P(2, 2), 'bo')
plot(P(1, 3), P(2, 3), 'bo')
plot(P(1, 4), P(2, 4), 'bo')
