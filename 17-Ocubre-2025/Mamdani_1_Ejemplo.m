%% --------------------   Control difuso ----------------------------------

clear all; close all; clc;

%% -- universos de discurso y funciones de membresia para estudio y calif ---
x=0:0.01:10;   % horas de estudio al dia
y=0:0.01:10;   % calificacion obtenida

%A=trimf(x,[0 3 5]);
A=trapmf(x,[4 6 10 10]);
B=sigmf(y,[3 8]);
% -----------------   Graficar   -------------------------------
subplot(2,1,1),plot(x,A,'LineWidth',2),hold on
title('Conjunto para horas de estudio'),xlabel('horas'),ylabel('\mu(x)')

subplot(2,1,2),plot(y,B,'LineWidth',2),hold on
title('Conjunto para calificacion obtenida'),xlabel('calificacion'),ylabel('\mu(x)')

%% ----------------- producto cartesiano  -------------------------------

for i=1:length(x)
    for j=1:length(y)
        mR(i,j)=min(A(i),B(j));
    end
end

figure (2)
%[X Y]= meshgrid(y,x);
mesh(x,y,mR)%set(gca,'FontSize',10')

%% ---------------------  composicion -------------------------------------
h=3;
Ap=trimf(x,[h h h]);
%Ap=sigmf(x,[-3 4]);
%Ap=n*;
for j=1:size(mR,2)
    for i=1:size(mR,1)
        aux(i)=min(Ap(i),mR(i,j));
    end
    Bp(j)= max(aux);
end

figure()
subplot(2,1,1),plot(x,Ap,'LineWidth',3),set(gca,'FontSize',10)
title(['Conjunto para ',num2str(h),' horas de estudio exactas']),ylabel('\mu(x)')
%axis([0 10 0 1])
subplot(2,1,2),plot(y,Bp,'LineWidth',5),set(gca,'FontSize',10)
title('Conjunto Ser buen estudiante'),xlabel('buen estudiante'),ylabel('\mu(y)')
axis([0 10 0 1])

