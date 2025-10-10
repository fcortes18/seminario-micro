Q = 4;

p = [ 0 0 1 1;
      0 1 0 1];

z = [p; 1 1 1 1];
Yd = [-1  1  1 1;
      -1 -1 -1 1];

R = z*z'/Q;
H = z*Yd'/Q;
X = inv(R)*H;
W = X(1:2, :)';
b = X(3, :)';

for q = 1:Q
    e(:,q) = Yd(:, q) - (W*p(:,q) + b);
end

e




