
clear;
clc;
close all;
 
train_log_file = '190413.txt';
 
 
[~, string_output] = dos(['cat ', train_log_file, ' | grep "avg," | awk ''{print $3}''']);
train_loss1 = str2num(string_output);
n = 1:length(train_loss1);
idx_train = (n-1);
figure;plot(idx_train, train_loss1);
grid on;
ylim([0 0.5])
legend('Train Loss');
xlabel('iterations');
ylabel('avg loss');
title(' Train Loss Curve')