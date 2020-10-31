clc;
close all;
clear all;

org = randi([0,255],10);
zoomed = zeros(19,19);

for i=1:10
    k = 0;
    for j=1:10
        zoomed(i,j+k) = org(i,j);
        k = k + 1;
    end
end
for i=1:10
    for j=2:2:18
        zoomed(i,j) = int64((zoomed(i,j-1) + zoomed(i,j+1))/2);
    end
end
k = 0;
result = zoomed;
for j=1:19
    k = 0;
    for i=1:10
        result(i+k,j) = zoomed(i,j);
        k = k + 1;
    end
end
for j=1:19
    for i=2:2:18
        result(i,j) = int64((result(i-1,j) + result(i+1,j))/2);
    end
end
figure;
image(org);
title('Original Image');
figure;
image(result);
title('Zoomed Image');