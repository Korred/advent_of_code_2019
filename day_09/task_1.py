import sys

sys.path.append("..")
from utils.utils import IntComputer, Program


mem = list(map(int, open('task_1_input.txt', 'r').readline().split(',')))

int_comp = IntComputer()
int_comp.add_program(Program(mem, [2]))
int_comp.run_prog()
