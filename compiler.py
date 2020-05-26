reserved_words = ['sub','print','call','set']
var_value = {}
fun_commands = {}
fun_start_line = {}
fun_name = 'none'
trace_stack = []

def bounds(fun):
    def wrapper(*args, **kwargs):
        print('\n=====')
        result = fun(*args)
        print('=====')
        return result
    return wrapper

@bounds
def print_all_vars():
    for (var,value) in var_value.items():
        print("{} = {} |".format(var,value))

@bounds
def print_trace():
    for line in trace_stack:
        print(line)

def query(line_num):
    print("Now we at line {}, enter some command:".format(line_num))
    command = input()
    if command == 'i':
        return 'pass'
    if command == 'o':
        return 'skip'
    if command == 'var':
        print_all_vars()
        return 'repeat'
    if command == 'trace':
        print_trace()
        return 'repeat'


def compile(fun_name):
    fun_commands_iter = iter(fun_commands[fun_name])
    for (idx,command) in enumerate(fun_commands_iter):
        should_continue = 0
        line_num = fun_start_line[fun_name]+idx+1
        while 1:
            todo = query(line_num)
            if todo == 'repeat':
                continue
            if todo == 'skip':
                should_continue = 1
            break
        if should_continue:
            continue
        if command == 'set':
            var = next(fun_commands_iter)
            value = next(fun_commands_iter)
            var_value[var] = value
            trace_stack.append('{}. set {} {}'.format(line_num,var,value))
            continue
        if command == 'print':
            var = next(fun_commands_iter)
            print(var_value[var])
            trace_stack.append('{}. print {}'.format(line_num,var))
            continue
        if command == 'call':
            fun = next(fun_commands_iter)
            trace_stack.append('{}. call {}'.format(line_num,fun))
            compile(fun)
            continue

@bounds
def parse_program(file_name):
    file = open(file_name,"r")
    parsed_program = []
    for (idx,line) in enumerate(file):
        line_commands = str(line).split()
        print("{}   |   {}".format(idx+1,str(line)))
        parsed_program+=line_commands
        if len(line_commands) == 0:
            continue
        if line_commands[0] == 'sub':
            fun_name = line_commands[1]
            fun_start_line[fun_name] = idx+1
    file.close()
    return parsed_program

code = parse_program('program.txt')
code_iter = iter(code)

for command in code_iter:
    if not command in reserved_words:
        var = command
        next(code_iter)
        value = next(code_iter)
        var_value[var] = value
        continue
    if command == 'sub':
        fun_name = next(code_iter)
        fun_commands[fun_name] = []
        continue
    if command == 'print' or command == 'call':
        fun_commands[fun_name].append(command)
        fun_commands[fun_name].append(next(code_iter))
        continue
    if command == 'set':
        fun_commands[fun_name].append(command)
        fun_commands[fun_name].append(next(code_iter))
        fun_commands[fun_name].append(next(code_iter))
        continue

trace_stack.append('{}. call {}'.format(fun_start_line['main'],'main'))
compile('main')
