# SomeProgramm
Vars can be only upper than first entry of 'sub'

Syntax:
sub (fun_name): new function definition  
print (var_name): print var to console  
set (var_name) (value): set value to (var_name)  
call (fun_name): obvious

+++++++++++++  
sub main  
set a 1  
call foo  
print a  
sub foo  
set a 2  
// programm print 1  
+++++++++++++  

Interpreter:  
i - step in, debugger goes inside the call (subname).  
o - step over, debugger does not go inside the call.  
trace - print stack trace of the execution with line numbers starting with main...  
var - printing the values of all declared variables.  
