#GG here is your flag:AlphaCTF{M4G1C_WI7h_SYMB0L1C_EXECUTION}
import angr
import claripy
import sys

project = angr.Project('../challenge/chall')

flag = claripy.BVS("flag", 8 * 60)
state = project.factory.entry_state(stdin = flag, remove_options={angr.options.LAZY_SOLVES})

for i in range(60):
    state.solver.add(flag.get_byte(i) >= 32)
    state.solver.add(flag.get_byte(i) != ord('`'))
    state.solver.add(flag.get_byte(i) != ord(']'))
    state.solver.add(flag.get_byte(i) != ord('^'))
    state.solver.add(flag.get_byte(i) != ord('['))
    state.solver.add(flag.get_byte(i) != ord('&'))
    state.solver.add(flag.get_byte(i) != ord(','))
    state.solver.add(flag.get_byte(i) != ord('$'))
    state.solver.add(flag.get_byte(i) != ord('-'))
    state.solver.add(flag.get_byte(i) != ord('"'))

def is_successful(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return b"GG, You got it!" in stdout_output

def should_abort(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return b"WRONG!" in stdout_output

sm = project.factory.simulation_manager(state)
sm.explore(find=is_successful, avoid=should_abort)
sm.run()
if sm.found:
    sol = sm.found[0]
    print(sol.posix.dumps(sys.stdin.fileno()))
else:
    print("no sol")
