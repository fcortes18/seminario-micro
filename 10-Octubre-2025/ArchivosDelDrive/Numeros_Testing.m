clear all; close all; clc;

load('Pesos_Neurona_Numeros.mat')

img_ent = imread('cinco.jpg');

img_ent = im2double(img_ent);

img_gris = rgb2gray(img_ent);

img_gris = imadjust(img_gris, [0.2 0.5]);

img_com = imcomplement(img_gris);

img_test = imresize(img_com, [28 28]);

imshow(img_test, 'InitialMagnification', 800)

size(img_test)

P1 = [img_test(:)];

net = W*P1 + b;

[a win] = max(net);

net'

NumeroReconocido = win - 1;

NumeroReconocido