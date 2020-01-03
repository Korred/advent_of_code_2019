class IntComputer:
    def __init__(self):
        self.programs = []
        # self.running = []

    def run_prog(self, idx=0):
        prog = self.programs[0]

        while prog.status != 0 and prog.status != 1:
            self.programs[0].run()

        # print(f'OUTPUTS: {prog.outputs}')

    def add_program(self, prog):
        self.programs.append(prog)


class Program:
    def __init__(self, memory, inputs=None, instruction_pointer=0, relative_base=0):

        self.init_memory = memory[:] + [0] * 10000
        self.curr_memory = memory[:] + [0] * 10000

        if inputs is None:
            self.inputs = []
        elif not isinstance(inputs, list):
            self.inputs = [inputs]
        else:
            self.inputs = inputs

        self.operands_num = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]

        self.ip = instruction_pointer
        self.relative_base = relative_base

        self.outputs = []

        self.status = -1

    def add_input(self, data):
        if isinstance(data, list):
            self.inputs.extend(data)
        else:
            self.inputs.append(data)

        self.status = -1

    def reset_output(self):
        self.outputs = []

    def get_last_output(self):
        return self.outputs[-1]

    def run(self):
        mem = self.curr_memory

        while True:
            # pad istruction_code with zeros
            ic = '0' * (5 - len(str(mem[self.ip]))) + str(mem[self.ip])
            op_code = int(ic[-2:])
            param_modes = [int(mode) for mode in ic[:-2][::-1]]

            # print(op_code)
            # print(param_modes)
            # print(self.inputs)
            # print(self.ip)
            # input()

            if op_code == 99:
                # exit code 0 = success/completed
                self.status = 0
                break

            base_tmp = [self.relative_base if param_modes[x] == 2 else 0 for x in range(self.operands_num[op_code])]
            operands = [
                mem[self.ip + x + 1] if param_modes[x] == 1 else mem[base_tmp[x] + mem[self.ip + x + 1]]
                for x in range(self.operands_num[op_code])
            ]

            # addition
            if op_code == 1:
                mem[base_tmp[2] + mem[self.ip + 3]] = operands[0] + operands[1]
                # increase instruction pointer by 4
                self.ip += 4

            # multiplication
            if op_code == 2:
                mem[base_tmp[2] + mem[self.ip + 3]] = operands[0] * operands[1]

                # increase instruction pointer by 4
                self.ip += 4

            # read input and save
            if op_code == 3:
                if len(self.inputs) == 0:
                    # exit code 1 = running/waiting for input
                    self.status = 1
                    break

                mem[base_tmp[0] + mem[self.ip + 1]] = self.inputs.pop(0)

                # increase instruction pointer by 2
                self.ip += 2

            # read data and output
            if op_code == 4:
                output = operands[0]

                self.outputs.append(output)

                # increase instruction pointer by 2
                self.ip += 2

                # exit code 2 = running/providing output
                self.status = 2
                break

            # jump-if-true
            if op_code == 5:

                if operands[0] != 0:
                    self.ip = operands[1]
                else:
                    self.ip += 3

            # jump-if-false
            if op_code == 6:
                if operands[0] == 0:
                    self.ip = operands[1]
                else:
                    self.ip += 3

            # less than
            if op_code == 7:
                mem[base_tmp[2] + mem[self.ip + 3]] = int(operands[0] < operands[1])

                self.ip += 4

            # equals
            if op_code == 8:
                mem[base_tmp[2] + mem[self.ip + 3]] = int(operands[0] == operands[1])

                self.ip += 4

            # adjust relative base
            if op_code == 9:
                self.relative_base += operands[0]
                self.ip += 2

