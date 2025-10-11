clear all; close all; clc;

load('xTrainImages.mat')
num = 3000;

imshow(xTrainImages{num}, 'InitialMagnification', 600);
size(xTrainImages{num})

yd(:, num)

clf

for k = 1:30
    subplot(6,5,k)
    imshow(xTrainImages{k+1000})
end

for j = 1:5000
    A = xTrainImages{j};
    B = [A(:)];
    P(:,j) = B;
end

Q = size(P, 2);
b = ones(1, Q);
Z = [P; b];

Y = yd - ones(10, Q) + yd;

R = Z*Z'/Q;
H = Z*Y'/Q;
X = pinv(R)*H;
W = X(1:784,:)';
b = X(785,:)';

for q=1:Q
    net = W*P(:, q) + b;
    [a(q) iwin(q)] = max(net);

    y(q) = find(yd(:, q) == 1);
end

Numaciertos = sum(y == iwin);
Porcentaciertos = (Numaciertos/5000)*100;

save('Pesos_Neurona_Numeros.mat', 'W', 'b')
    
